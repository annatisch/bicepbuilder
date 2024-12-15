
from collections import defaultdict
import json
from typing import IO, Dict, List, Optional, Tuple
import re
import os

import marko

from ._nodes import MarkdownNode, BicepObject
from ._utils import (
    class_name,
    param_name,
    combined_module_name,
    camelcase
)


_MODULE_TEMPLATE = """
def {module_name}(
        bicep: IO[str],
        /,
        *,
        params: {resource_name},
        scope: Optional[BicepExpression] = None,
        {params}depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '{module_version}',
        registry_prefix: str = 'br/public:avm/res',
        path: str = '{module_reference}',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> {resource_name}Bicep:
    symbol = "{module_name}_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{{description}}')\\n")
    if batch_size:
        bicep.write(f"@batchSize({{batch_size}})\\n")
    bicep.write(f"module {{symbol}} '{{registry_prefix}}/{{path}}:{{tag}}' = {{{{\\n")
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
    output = {resource_name}Bicep(symbol)
    output.outputs = {outputs}
    return output
"""
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
    pymodule.write("from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional\n")
    pymodule.write("from typing_extensions import Required\n\n")
    pymodule.write(f"from {relative_import}._utils import (\n")
    pymodule.write("    generate_suffix,\n")
    pymodule.write("    resolve_value,\n")
    pymodule.write("    resolve_key,\n")
    pymodule.write("    serialize_dict,\n")
    pymodule.write("    serialize_list,\n")
    pymodule.write(")\n")
    pymodule.write(f"from {relative_import}.expressions import (\n")
    pymodule.write("    BicepExpression,\n")
    pymodule.write("    Module,\n")
    pymodule.write("    ResourceId,\n")
    pymodule.write("    ResourceName,\n")
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
    pymodule.write(f"class {resource.name}Bicep(Module):\n")
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
        dir_level: str = "."
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

def resources_from_dir(
        base: str,
        root_dir: str,
        output_dir: str, 
        dir_level: str = "."
) -> List[str]:
    all_imports = []
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

        if not os.path.isdir(suboutput_dir):
            os.makedirs(suboutput_dir)
        with open(os.path.join(suboutput_dir, "__init__.py"), 'w') as pymodule:
            module_name = write_pymodule(
                pymodule,
                resource=subresource,
                typed_objects=objects,
                module_name=output_dirname,
                module_reference=f"{base}/{subdirname}",
                module_version=version,
                relative_import=dir_level
            )
            if module_name:
                all_imports.append(module_name)
    return all_imports

def resource_from_readme(root_dir: str) -> None:
    print("ROOT", root_dir)
    base = os.path.split(root_dir)[-1]
    output = os.path.join(root_dir, "bicepbuilder/modules")
    resources_from_dir(base, root_dir, output)
 

def run() -> None:
    cwd = os.path.abspath(os.curdir)
    output_dir = os.path.join(cwd, "bicepbuilder_modules")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    all_modules = []
    for basename in os.listdir(cwd):
        basedir = os.path.join(cwd, basename)
        if not os.path.isdir(basedir):
            continue
        print(f"Scanning {basename}")
        module_name = basename.replace("-", "_")
        module_output_dir = os.path.join(output_dir, module_name)
        output_funcs = resources_from_dir(basename, basedir, module_output_dir)
        print("Outputs: ", output_funcs)
        if output_funcs:
            module_init = os.path.join(module_output_dir, "__init__.py")
            with open(module_init, 'w') as initfile:
                for output in output_funcs:
                    initfile.write(f"from .{output} import {output}\n")
                initfile.write("\n")
                initfile.write("__all__ = [\n")
                for output in output_funcs:
                    initfile.write(f"    '{output}'\n")
                initfile.write("]\n")
            for output in output_funcs:
                combined_module = combined_module_name(module_name, output)
                combined_class = camelcase(combined_module)
                output_class = camelcase(output)
                all_modules.append(
                    (
                        f"from .{module_name}.{output} import {output} as {combined_module}, {output_class} as {combined_class}, {output_class}Bicep as {combined_class}Bicep\n",
                        f"    '{combined_module}'\n    '{combined_class}'\n    '{combined_class}Bicep'\n"))
    print("All outputs", len(all_modules))
    if all_modules:
        total_init = os.path.join(output_dir, "__init__.py")
        print("Adding", total_init)
        with open(total_init, 'w') as initfile:
            initfile.write("from typing import overload, Literal, Optional, Union, IO\n")
            initfile.write("from ..expressions import BicepExpression\n\n")
            for module in all_modules:
                initfile.write(module[0])
            initfile.write("\n")
            initfile.write("__all__ = [\n")
            for module in all_modules:
                initfile.write(module[1])
            initfile.write("]\n\n")
            initfile.write("class ResourceMixin:\n")
            initfile.write("    bicep: IO[str]\n\n")
            initfile.write("    def add(self, resource, params, **kwargs):\n")
            initfile.write("        return globals()[resource](self.bicep, params, **kwargs)\n")

        # outputs = []
        # for resourcename in os.listdir(basedir):
        #     resourcedir = os.path.join(basedir, resourcename)
        #     if not os.path.isdir(resourcedir):
        #         continue
        #     print(f"Scanning {basename}/{resourcename}")
        #     resources_from_dir(basename, resourcedir, os.path.join(output_dir, basename))
        

