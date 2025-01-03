
from collections import defaultdict
import json
from typing import IO, Dict, List, Optional, Tuple
import os

import marko

from ._nodes import MarkdownNode, BicepObject
from ._utils import (
    class_name,
    combined_module_name,
    camelcase
)


_MODULE_TEMPLATE = """
def _{module_name}(
        bicep: IO[str],
        params: {resource_name},
        /,
        *,
        {params}scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '{module_version}',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> {resource_name}Module:
    symbol = "{module_name}_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{{description}}')\\n")
    if batch_size:
        bicep.write(f"@batchSize({{batch_size}})\\n")
    bicep.write(f"module {{symbol}} 'br/public:avm/res/{module_reference}:{{tag}}' = {{{{\\n")
    bicep.write(f"  name: {{resolve_value(name)}}\\n")
    if scope is not None:
        bicep.write(f"  scope: {{resolve_value(scope)}}\\n")
    bicep.write(f"  params: {{{{\\n")
    {bicep_params}
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}}}\\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\\n")
    bicep.write(f"}}}}\\n")
    output = {resource_name}Module(symbol)
    output.outputs = {outputs}
    return output
"""
_OVERLOAD_TEMPLATE = """
    @overload
    def add(
            self,
            resource: Literal['{module_name}'],
            params: {resource_name},
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            tag: str = '{module_version}',
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
    ) -> {resource_name}Module:
        ...
"""
def write_resource_module(
        pymodule: IO[str],
        overloads: List[str],
        *,
        resource: BicepObject,
        typed_objects: List[BicepObject],
        module_name: str,
        module_reference: str,
        module_version: str,
        relative_import: str
) -> Optional[str]:
    pymodule.write("from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional\n")
    pymodule.write("from typing_extensions import Required\n\n")
    pymodule.write(f"from {relative_import}._utils import (\n")
    pymodule.write("    generate_suffix,\n")
    pymodule.write("    resolve_value,\n")
    pymodule.write("    serialize_dict,\n")
    pymodule.write("    serialize_list,\n")
    pymodule.write(")\n")
    pymodule.write(f"from {relative_import}.expressions import (\n")
    pymodule.write("    BicepExpression,\n")
    pymodule.write("    Module,\n")
    pymodule.write("    Deployment,\n")
    pymodule.write("    Output,\n")
    pymodule.write(")\n\n")
    if resource.imports:
        importstatements = defaultdict(list)
        for subresource in resource.imports:
            importstatements[subresource.module].append(subresource.name)
        pymodule.write('if TYPE_CHECKING:\n')
        for import_module, classes in importstatements.items():
            pymodule.write(f"    from .{import_module} import {', '.join(classes)}\n")
        pymodule.write("\n")
    pymodule.write("\n")
    for object in typed_objects:
        pymodule.write(str(object))
        pymodule.write("\n\n")
    if resource.outputs:
        pymodule.write(str(resource.outputs))
        pymodule.write("\n\n")
    pymodule.write(f"class {resource.name}Module(Module):\n")
    if resource.outputs:
        pymodule.write(f"    outputs: {resource.name}Outputs\n")
    else:
        pymodule.write(f"    outputs: Dict[str, Output]\n")
    pymodule.write("\n")  
    pymodule.write(_MODULE_TEMPLATE.format(
        module_name=module_name,
        resource_name=resource.name,
        params="",
        bicep_params="",
        module_reference=module_reference,
        module_version=module_version,
        outputs=resource.outputs.format() if resource.outputs else "{}")
    )
    overloads.append(_OVERLOAD_TEMPLATE.format(
        module_name=module_name,
        resource_name=resource.name,
        module_version=module_version
    ))
    return module_name

def write_pymodule(
        pymodule: IO[str],
        *,
        resource: BicepObject,
        typed_objects: List[BicepObject],
        module_name: str,
        module_reference: str,
        module_version: str,
        relative_import: str
) -> Optional[str]:
    pymodule.write("from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union\n")
    pymodule.write("from typing_extensions import Required\n\n")
    pymodule.write(f"from {relative_import}.expressions import (\n")
    pymodule.write("    BicepExpression,\n")
    pymodule.write("    Module,\n")
    pymodule.write("    Output,\n")
    pymodule.write(")\n\n")
    if resource.imports:
        importstatements = defaultdict(list)
        for subresource in resource.imports:
            importstatements[subresource.module].append(subresource.name)
        pymodule.write('if TYPE_CHECKING:\n')
        for import_module, classes in importstatements.items():
            pymodule.write(f"    from .{import_module} import {', '.join(classes)}\n")
        pymodule.write("\n")
    pymodule.write("\n")
    for object in typed_objects:
        pymodule.write(str(object))
        pymodule.write("\n\n")
    if resource.outputs:
        pymodule.write(str(resource.outputs))
        pymodule.write("\n\n")
    pymodule.write(f"class {resource.name}Module(Module):\n")
    if resource.outputs:
        pymodule.write(f"    outputs: {resource.name}Outputs\n")
    else:
        pymodule.write(f"    outputs: Dict[str, Output]\n")
    pymodule.write("\n")
    if module_version is None:
        return None
    extra_params = resource.get_params()
    func_params = ""
    bicep_params = ""
    if extra_params:
        for param in extra_params:
            func_params += f"{param[0]}: Union[{param[2]}, BicepExpression],\n        "
            bicep_params += f"file_handle.write(f\"    {{resolve_key('{param[1]}')}}: {{resolve_value({param[0]})}}\\n\")"
        
    pymodule.write(_MODULE_TEMPLATE.format(
        module_name=module_name,
        resource_name=resource.name,
        params=func_params,
        bicep_params=bicep_params,
        module_reference=module_reference,
        module_version=module_version,
        outputs=resource.outputs.format() if resource.outputs else "{}")
    )
    return module_name


def subresources_from_dirs(
        base: str,
        root_dir: str,
        output_dir: str, 
        dir_level: str
) -> List[BicepObject]:
    all_objects = []
    for subdirname in os.listdir(root_dir):
        subdir = os.path.join(root_dir, subdirname)
        subresource_readme = os.path.join(subdir, "README.md")
        subresource_version = os.path.join(subdir, "version.json")
        if os.path.isdir(subdir) and os.path.isfile(subresource_readme):
            version = None
            if os.path.isfile(subresource_version):
                with open(subresource_version) as version_json:
                    version = json.load(version_json)["version"]
                    if len(version.split('.')) == 2:
                        # Sometimes the version string is missing the patch number.
                        version += ".0"
            output_dirname = subdirname.replace('-', '_')
            suboutput_dir = os.path.join(output_dir, output_dirname)
            inherited_resources = subresources_from_dirs(
                base=base + "/" + subdirname,
                root_dir=subdir,
                output_dir=suboutput_dir,
                dir_level=dir_level + ".")
        else:
            continue
        with open(subresource_readme, "r") as md:
            try:
                content = md.read()
            except Exception as e:
                print(f"Couldn't read {subresource_readme}", str(e))
                continue
            document = marko.parse(content)
            resource_name = class_name(" ".join([n.title() for n in subdirname.split('-')]))
            resource_type = document.children[0].children[1].children
            subresource = BicepObject(
                name=resource_name,
                module=output_dirname,
                resource=resource_type,
                subresources=inherited_resources
            )
            for child in document.children:
                subresource.add(child)
            objects = subresource.close()
            objects.append(subresource)
            all_objects.extend(objects)

        if not os.path.isdir(suboutput_dir):
            os.makedirs(suboutput_dir)
        with open(os.path.join(suboutput_dir, "__init__.py"), 'w') as pymodule:
            write_pymodule(
                pymodule,
                resource=subresource,
                typed_objects=objects,
                module_name=output_dirname,
                module_reference=f"{base}/{subdirname}",
                module_version=version,
                relative_import=dir_level
            )
    return all_objects

def parse_resources(
        *,
        name: str,
        reference: str,
        root_dir: str,
        root_output_dir: str, 
        overloads: List[str],
) -> Dict[str, Tuple[str, str, str]]:
    imports = {}
    for dirname in os.listdir(root_dir):
        resource_dir = os.path.join(root_dir, dirname)
        resource_readme = os.path.join(resource_dir, "README.md")
        resource_version = os.path.join(resource_dir, "version.json")
        if os.path.isdir(resource_dir) and os.path.isfile(resource_readme):
            with open(resource_version) as version_json:
                version = json.load(version_json)["version"]
                if len(version.split('.')) == 2:
                    # Sometimes the version string is missing the patch number.
                    version += ".0"
            module_name = dirname.replace('-', '_')
            combined_module = combined_module_name(name, module_name)
            output_dir = os.path.join(root_output_dir, module_name)
            subresources = subresources_from_dirs(
                base=reference + "/" + dirname,
                root_dir=resource_dir,
                output_dir=output_dir,
                dir_level="....")
        else:
            continue
        with open(resource_readme, "r") as md:
            try:
                content = md.read()
            except Exception as e:
                print(f"Couldn't read {resource_readme}", str(e))
                continue
            document = marko.parse(content)
            resource_name = camelcase(combined_module)
            resource_type = document.children[0].children[1].children
            resource = BicepObject(
                name=resource_name,
                module=module_name,
                resource=resource_type,
                subresources=subresources
            )
            for child in document.children:
                resource.add(child)
            objects = resource.close()
            objects.append(resource)
            imports[module_name] = [combined_module, resource_name, resource_name + "Module"]

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        with open(os.path.join(output_dir, "__init__.py"), 'w') as pymodule:
            write_resource_module(
                pymodule,
                overloads,
                resource=resource,
                typed_objects=objects,
                module_name=combined_module,
                module_reference=f"{reference}/{dirname}",
                module_version=version,
                relative_import="..."
            )
    return imports
 

_BASEFUNC_TEMPLATE = """
    def add(self, resource: str, params: Dict[str, Any], **kwargs) -> Module:
        try:
            return globals()['_' + resource](self.bicep, params, **kwargs)
        except KeyError:
            raise ValueError(f"Unrecognized resource: '{resource}'.")

"""
def run() -> None:
    # TODO: parse args for working and output dirs
    cwd = os.path.abspath(os.curdir)
    output_dir = os.path.join(cwd, "bicepbuilder_modules")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    all_imports = []
    dunder_all = []
    overloads = []
    for basename in os.listdir(cwd):
        basedir = os.path.join(cwd, basename)
        if not os.path.isdir(basedir):
            continue

        module_name = basename.replace("-", "_")
        module_output_dir = os.path.join(output_dir, module_name)
        imports = parse_resources(
            name=module_name,
            reference=basename,
            root_dir=basedir,
            root_output_dir=module_output_dir,
            overloads=overloads
        )
        for key, (funcname, objname, bicepname) in imports.items():
            all_imports.append(
                f"from .{module_name}.{key} import _{funcname}, {objname}, {bicepname}\n"
            )
            dunder_all.extend([objname, bicepname])

    all_modules_init = os.path.join(output_dir, "__init__.py")
    with open(all_modules_init, 'w') as initfile:
        initfile.write("from typing import overload, Literal, Optional, Union, IO, Dict, Any\n\n")
        initfile.write("from ..expressions import BicepExpression, Module\n\n")
        for import_statement in all_imports:
            initfile.write(import_statement)
        initfile.write("\n")
        initfile.write("__all__ = [\n")
        for imported in dunder_all:
            initfile.write(f"    '{imported}'\n")
        initfile.write("]\n\n")
        initfile.write("class _AddResourceMixin:\n")
        initfile.write("    bicep: IO[str]\n")
        for overload in overloads:
            initfile.write(overload)
        initfile.write(_BASEFUNC_TEMPLATE)
