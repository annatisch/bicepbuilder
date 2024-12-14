
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


class BicepExpression:
    def __init__(self, value: str, /) -> None:
        self._value = value

    def resolve(self) -> str:
        return self._value
    
    def format(self) -> str:
        return f"${{{self.resolve()}}}"


OutputType = TypeVar("OutputType", bound=Literal["string", "array", "object"])

class Output(BicepExpression, Generic[OutputType]):
    type: OutputType

    def __init__(self, symbol: str, name: str, type: OutputType) -> None:
        self._resource = symbol
        self._name = name
        self.type = type

    def resolve(self) -> str:
        return f"{self._resource}.outputs.{self._name}"


class ResourceId(BicepExpression):
    def __init__(self, value: str, /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{self._resource}.id"


class ResourceName(BicepExpression):
    def __init__(self, value: str, /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{self._resource}.name"


class ResourceLocation(BicepExpression):
    def __init__(self, value: str, /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{self._resource}.location"


class ResourceGroup(BicepExpression):
    def __init__(self, resource_group: Optional[str] = None, /):
        self._rg = resource_group

    def resolve(self) -> str:
        if self._rg:
            return f"resourceGroup('{self._rg}')"
        return "resourceGroup()"

    @property
    def location(self) -> BicepExpression:
        return ResourceLocation(self.resolve())

    @property
    def id(self) -> BicepExpression:
        return ResourceId(self.resolve())

    @property
    def name(self) -> BicepExpression:
        return ResourceName(self.resolve())


class Subscription(BicepExpression):
    def __init__(self, subscription: Optional[str] = None, /):
        self._sub = subscription

    def resolve(self) -> str:
        if self._sub:
            return f"subscription('{self._sub}')"
        return f"subscription()"

    @property
    def id(self) -> BicepExpression:
        return ResourceId(self.resolve())

    @property
    def subscription_id(self) -> ResourceId:
        return BicepExpression(f"{self.resolve()}.subscriptionId")

    @property
    def tenant_id(self) -> ResourceId:
        return BicepExpression(f"{self.resolve()}.tenantId")

    @property
    def display_name(self) -> BicepExpression:
        return BicepExpression(f"{self.resolve()}.displayName")

class PrincipalId(BicepExpression):
    def __init__(self, symbol: Optional[str] = None) -> None:
        self.resource = symbol

    def resolve(self) -> str:
        if self.resource:
            return f"{self.resource}.properties.principalId"
        return "principalId"


class BoolLogic(BicepExpression):
    def __init__(self, a_value: Any, b_value: Any, operator: Literal['==', '!=', '<', '>', '<=', '>=']):
        self._a = a_value
        self._b = b_value
        self._op = operator

    def resolve(self) -> str:
        return f"{resolve_value(self._a)} {self._op} {resolve_value(self._b)}"


class UniqueName(BicepExpression):
    def __init__(self, prefix: str, length: int, basestr: Optional[Any] = None) -> None:
        self._prefix = prefix
        self._length = length
        if basestr:
            self._basestr = resolve_value(basestr)
        else:
            self._basestr = "resourceGroup().id"

    def resolve(self) -> str:
        return f"take('{self._prefix}${{uniqueString({self._basestr})}}', {self._length})"


class GuidName(BicepExpression):
    def __init__(self, basestr: str, *args: str) -> None:
        self._args = [basestr] + list(args)

    def resolve(self) -> str:
        arg_str = ", ".join([resolve_value(a) for a in self._args])
        return f"guid({arg_str})"


class SubscriptionResourceId(BicepExpression):
    def __init__(self, resourcetype: str, name: Enum) -> None:
        self._resource = resourcetype
        self._name = name.value

    def resolve(self) -> str:
        return f"subscriptionResourceId('{self._resource}', '{self._name}')"


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
