from collections import defaultdict
import json
from typing import IO, Dict, List, Optional, Tuple, Protocol
import re
import os

from ._utils import singular_class_name, class_name, param_name

TYPES = {
    "string": "str",
    "bool": "bool",
    "array": "List",
    "object": "Dict",
    "secureObject": "Dict",
    "securestring": "str",
    "int": "int"
}
HIDDEN_PARAM = "Required if the template is used in a standalone deployment"


class MarkdownNode(Protocol):
    type: str

    def add(self, node) -> None:
        ...

    def close(self) -> List['BicepObject']:
        ...


class ResourceMap(MarkdownNode):
    type: str = "ResourceMap"
    name: str = "ResourceMap"
    resources: Dict[str, str]
    versions: Dict[str, str]

    def __init__(self):
        self.resources = {}
        self.versions = {}
        self._current_resource: Optional[str] = None

    def add(self, node):
        if node.get_type() == "Paragraph":
            for child in node.children:
                if child.get_type() == "CodeSpan":
                    self._current_resource = child.children
                    self.resources[singular_class_name(self._current_resource.split('/')[-1])] = self._current_resource
                if child.get_type() == "Link":
                    self.versions[self._current_resource] = child.children[0].children

    def get_readme(self, objname):
        if not objname in self.resources:
            raise ValueError(f"No resource found with name '{objname}'")

    def close(self) -> List['BicepObject']:
        return []


class Outputs(MarkdownNode):
    type: str = "Outputs"
    name: str
    outputs: List[Tuple[str, str, str]]

    def __init__(self, name: str):
        self.name = name
        self.outputs = []

    def __str__(self):
        resource_str = f"class {self.name}Outputs(TypedDict, total=False):\n"
        resource_str += f"    \"\"\"Outputs for {self.name}\"\"\"\n"
        for name, type, description in self.outputs:
            resource_str += f"    {name}: Output[Literal['{type}']]\n"
            resource_str += f"    \"\"\"{description}\"\"\"\n"
        return resource_str

    def format(self) -> str:
        outputs_str = "{\n"
        for name, type, _ in self.outputs:
            outputs_str += f"            '{name}': Output(symbol, '{name}', '{type}'),\n"
        outputs_str += "        }\n"
        return outputs_str

    def add(self, node):
        try:
            if node.children[0].children == '| Output | Type | Description |':
                output_name = None
                output_type = None
                output_description = None
                for child in node.children[1:]:
                    if child.get_type() == "CodeSpan":
                        output_name = child.children
                    if child.get_type() == "RawText":
                        try:
                            output_type, output_description = [o.strip() for o in child.children.split(' |') if o]
                            if not output_type:
                                output_type = "object"
                            self.outputs.append((output_name, output_type, output_description))
                        except:
                            continue
        except:
            return

    def close(self) -> List['BicepObject']:
        return []


class BicepObject:
    name: str
    description: str
    resource: Optional[str]
    version: Optional[str]
    parameters: Dict[str, 'Parameter']
    objects: List['BicepObject']
    module: str
    imports: List['BicepObject']
    include: bool


    def __str__(self):
        resource_str = f"class {self.name}(TypedDict, total=False):\n"
        resource_str += f"    \"\"\"{self.description}\"\"\"\n"
        for param in self.parameters.values():
            if param.include:
                resource_str += str(param)
        return resource_str

    def __eq__(self, value):
        try:
            return self.parameters == value.parameters
        except AttributeError:
            return False

    def __init__(
            self,
            name: str,
            module: str,
            resource: Optional[str] = None,
            subresources: Optional[List['BicepObject']] = None
    ):
        self.name = name
        self.module = module
        self.resource = resource[1:-1] if resource else None
        self.version = None
        self.parameters = {}
        self.objects = []
        self.map: Optional[ResourceMap] = None
        self.description = ""
        self._current_param: Optional[Parameter] = None
        self.subresources = {r.name: r for r in subresources} if subresources else {}
        self.imports = []
        self.include = True
        self.outputs = None


    def _reset_current(self, name: Optional[str] = None):
        if self._current_param:
            if self._current_param.type == "ResourceMap":
                self.map = self._current_param
                self.version = self.map.versions.get(self.resource)
            elif self._current_param.type == "Outputs":
                self.outputs = self._current_param
            elif self._current_param.name:
                self.parameters[self._current_param.name] = self._current_param
            new_models = self._current_param.close()
            self.objects.extend(new_models)
        if name:
            self._current_param = Parameter(name, parent=self)

    def get_params(self) -> List[Tuple[str, str, str]]:
        params = []
        for param in self.parameters.values():
            if param.include:
                continue
            name = param_name(param.name)
            params.append((name, param.name, param.format_type()))
        return params

    def add(self, node):
        if node.get_type() == "Heading":
            header_content = node.children[0]
            if header_content.get_type() == "RawText":
                if header_content.children == "Resource Types":
                    self._current_param = ResourceMap()
                elif header_content.children == "Parameter: ":
                    param_name = node.children[1].children
                    if "." in param_name:
                        classname = class_name(*param_name.split('.')[:-1])
                        if classname == self.name:
                            self._reset_current(param_name.split('.')[-1])
                        else:
                            if "<" in param_name:
                                if classname == self._current_param.object.name:
                                    self._current_param.object.include = False
                            self._current_param.add(node)
                    else:
                        self._reset_current(param_name)
                elif header_content.children == "Outputs":
                    self._reset_current()
                    self._current_param = Outputs(name=self.name)
        elif self._current_param:
            self._current_param.add(node)

    def close(self) -> List['BicepObject']:
        self._reset_current()
        return self.objects


class Parameter:
    type: str = "Param"
    name: str
    parent: BicepObject
    description: str
    required: bool
    type: str
    subtype: Optional[str]
    uniontype: Optional[str]
    parameters: Dict[str, 'Parameter']
    object: Optional[BicepObject]
    include: bool

    def format_type(self) -> str:
        type_str = ""
        subtype_str = self.subtype if self.subtype else ""
        if self.uniontype:
            subtype_str = f"Union[{subtype_str}, {self.uniontype}]"
        if self.type == "List":
            if self.subtype:
                type_str = f"List[{subtype_str}]"
            else:
                type_str = "List[object]"
        elif self.type == "Dict":
            if self.subtype:
                type_str = f"Dict[str, {subtype_str}]"
            else:
                type_str = "Dict[str, object]"
        else:
            type_str = self.type
        return type_str

    def __str__(self) -> str:
        type_str = self.format_type()
        if self.required:
            type_str = f"Required[{type_str}]"
        return f"    {self.name}: {type_str}\n    \"\"\"{self.description}\"\"\"\n"

    # def __bool__(self) -> bool:
    #     return self._include

    def __init__(self, name: str, parent: BicepObject) -> None:
        self.name = name
        self.parent = parent
        self.parameters = []
        self.type = "Any"
        self.subtype = None
        self.parameters = {}
        self.object = None
        self.uniontype = None
        self.include = True

    def add(self, node):
        if self.object:
            self.object.add(node)
        elif node.get_type() == "Paragraph":
            if node.children[0].get_type() == "RawText":
                description = node.children[0].children
                if "|" in description:
                    return
                if HIDDEN_PARAM in description:
                    self.include = False
                self.description = description
            if node.children[0].get_type() == "StrongEmphasis" and not self.object:
                classname = class_name(self.parent.name, self.name)
                self.object = BicepObject(name=classname, module=self.parent.module)
                self.object.description = self.description
                if self.type == "List":
                    self.subtype = f"'{self.object.name}'"
                else:
                    self.type = f"'{self.object.name}'"
        elif node.get_type() == "List":
            for listitem in node.children:
                child = listitem.children[0]
                if child.get_type() == "Paragraph" and child.children[0].get_type() == "RawText":
                    item = child.children[0].children
                    if item.startswith('Required:'):
                        self.required = "Yes" in item
                    elif item.startswith('Type:'):
                        self.type = TYPES[item.split(" ")[-1]]
                    elif item.startswith('Allowed:'):
                        values = listitem.children[1].children[0].children.strip('[]\n').split('\n')
                        self.type = f"Literal[{', '.join([v.strip() for v in values])}]"
                    elif item.startswith('Roles configurable by name:'):
                        values = [v.children[0].children[0].children for v in listitem.children[1].children]
                        self.uniontype = f"Literal[{', '.join(values)}]"
    
    def close(self) -> List[BicepObject]:
        if self.object:
            if self.object.include:
                objects = self.object.close()
                objects.append(self.object)
                return objects
            else:
                self.type = "Dict[str, object]"
        if self.type == "List" and not self.subtype:
            classname = singular_class_name(self.name)
            if classname in self.parent.subresources:
                self.parent.imports.append(self.parent.subresources[classname])
                self.subtype = f"'{classname}'"
        if self.type == "Dict" and not self.subtype:
            classname = singular_class_name(self.name)
            if classname in self.parent.subresources:
                self.parent.imports.append(self.parent.subresources[classname])
                self.type = f"'{classname}'"
        return []
