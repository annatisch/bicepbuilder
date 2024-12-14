
import re

def singular_name(name: str) -> str:
    name = name.replace(" ", "")
    if name.endswith("ies"):
        name = name[:-3] + 'y'
    else:
        name = name.rstrip('s')
    return name[0].capitalize() + name[1:]

def class_name(*names: str) -> str:
    if names[-1] == "properties":
        return f"{singular_name(names[-2])}Properties"
    else:
        return singular_name(names[-1])

def build_resource_name(name: str):
    name = singular_name(name)
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

def param_name(name: str) -> str:
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name
