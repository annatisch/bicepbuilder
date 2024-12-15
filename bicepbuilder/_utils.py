
from enum import Enum
from typing import IO, Any, Dict, Generic, List, Literal, Optional, TypeVar
import json
import random
import string


def resolve_value(value: Any) -> str:
    try:
        return value.resolve()
    except AttributeError:
        return json.dumps(value).replace('"', "'")


def resolve_key(key: Any) -> str:
    try:
        return key.resolve()
    except AttributeError:
        if key.isidentifier():
            return key
        return f"'{key}'"


def generate_suffix() -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)).lower()


def serialize(bicep: IO[str], value: Any, indent: str = "") -> None:
    if isinstance(value, dict):
        bicep.write("{\n")
        serialize_dict(bicep, value, indent=indent + "  ")
        bicep.write(indent + "}\n")
    elif isinstance(value, list):
        bicep.write("[\n")
        serialize_list(bicep, value, indent=indent + "  ")
        bicep.write(indent + "]\n")
    else:
        bicep.write(resolve_value(value))


def serialize_list(bicep: IO[str], list_val: List[Any], indent: str) -> None:
    for item in list_val:
        if isinstance(item, dict):
            bicep.write(f"{indent}{{\n")
            serialize_dict(bicep, item, indent + '  ')
            bicep.write(f"{indent}}}\n")
        elif isinstance(item, list):
            bicep.write(f"{indent}[\n")
            serialize_list(bicep, item, indent + '  ')
            bicep.write(f"{indent}]\n")
        else:
            bicep.write(f"{indent}{resolve_value(item)}\n")


def serialize_dict(bicep: IO[str], dict_val: Dict[str, Any], indent: str) -> None:
    for key, value in dict_val.items():
        if isinstance(value, dict) and value:
            bicep.write(f"{indent}{key}: {{\n")
            serialize_dict(bicep, value, indent + '  ')
            bicep.write(f"{indent}}}\n")
        elif isinstance(value, list) and value:
            bicep.write(f"{indent}{key}: [\n")
            serialize_list(bicep, value, indent + '  ')
            bicep.write(f"{indent}]\n")
        else:
            bicep.write(f"{indent}{resolve_key(key)}: {resolve_value(value)}\n")
