
import re

def singular_name(name: str) -> str:
    if name.endswith("ies"):
        return name[:-3] + 'y'
    else:
        return name.rstrip('s')

def singular_class_name(name: str) -> str:
    name = singular_name(name.replace(" ", ""))
    return name[0].capitalize() + name[1:]

def singular_module_name(name: str) -> str:
    return singular_name(name.replace(" ", "_"))

def class_name(*names: str) -> str:
    if names[-1] == "properties":
        return f"{singular_class_name(names[-2])}Properties"
    else:
        return singular_class_name(names[-1])

# def build_resource_name(name: str):
#     name = singular_class_name(name)
#     return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

def param_name(name: str) -> str:
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name

def combined_module_name(module_name: str, func_name: str) -> str:
    if func_name[0:len(module_name)] == module_name:
        return func_name
    last_section = module_name.split('_')[-1]
    if func_name.startswith(last_section):
        spliced = module_name.rpartition('_')[0]
        spliced = spliced + "_" if spliced else spliced
        return f"{spliced}{func_name}"
    singular = singular_name(last_section)
    if func_name.startswith(singular):
        spliced = module_name.rpartition('_')[0]
        spliced = spliced + "_" if spliced else spliced
        return f"{spliced}{func_name}"
    return f"{module_name}_{func_name}"

def camelcase(name: str) -> str:
    return "".join(s.title() for s in name.split('_'))
