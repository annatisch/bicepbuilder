from typing import List, TypeVar, Generic, Literal, Optional, Any, Union
from enum import Enum

from ._utils import resolve_value


def resolve_ref(self, expression: Union['BicepExpression', str]):
    try:
        return expression.resolve()
    except AttributeError:
        return expression


class BicepExpression:
    def __init__(self, value: Union['BicepExpression', str], /) -> None:
        self._value = value

    def resolve(self) -> str:
        return resolve_ref(self._value)
    
    def format(
            self,
            *,
            prefix: Union['BicepExpression', str],
            suffix: Union['BicepExpression', str],
    ) -> str:
        return f"{resolve_ref(prefix)}${{{self.resolve()}}}{resolve_ref(suffix)}"


OutputType = TypeVar("OutputType", bound=Literal["string", "array", "object"])
class Output(BicepExpression, Generic[OutputType]):
    type: OutputType

    def __init__(
            self,
            symbol: Union[BicepExpression, str],
            name: Union[BicepExpression, str],
            type: OutputType
    ) -> None:
        self._resource = symbol
        self._name = name
        self.type = type

    def resolve(self) -> str:
        return f"{resolve_ref(self._resource)}.outputs.{resolve_ref(self._name)}"


class Module(BicepExpression):
    def __init__(self, value: str, /) -> None:
        self._value = value

    def resolve(self) -> str:
        return self._value

    @property
    def id(self) -> BicepExpression:
        return ResourceId(self)

    @property
    def name(self) -> BicepExpression:
        return ResourceName(self)

    def get_output(self, name: Union[BicepExpression, str], type: OutputType) -> Output[OutputType]:
        return Output(self, name, type)


class ResourceId(BicepExpression):
    def __init__(self, value: Union[BicepExpression, str], /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{resolve_ref(self._resource)}.id"


class ResourceName(BicepExpression):
    def __init__(self, value: Union[BicepExpression, str], /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{resolve_ref(self._resource)}.name"


class ResourceLocation(BicepExpression):
    def __init__(self, value: Union[BicepExpression, str], /) -> None:
        self._resource = value

    def resolve(self) -> str:
        return f"{resolve_ref(self._resource)}.location"


class Deployment(BicepExpression):
    def __init__(self) -> None:
        ...

    def resolve(self) -> str:
        return "deployment()"

    @property
    def name(self) -> BicepExpression:
        return ResourceName(self)


class ResourceGroup(BicepExpression):
    def __init__(
            self,
            resource_group: Optional[Union[BicepExpression, str]] = None,
            subscription: Optional[Union[BicepExpression, str]] = None, /):
        self._rg = resource_group
        self._sub = subscription

    def resolve(self) -> str:
        if self._rg:
            if self._sub:
                return f"resourceGroup({resolve_value(self._sub)}, {resolve_value(self._rg)})"
            return f"resourceGroup({resolve_value(self._rg)})"
        return "resourceGroup()"

    @property
    def location(self) -> BicepExpression:
        if self._rg:
            raise ValueError("Named resource group can only be used for scope, not properties.")
        return ResourceLocation(self)

    @property
    def id(self) -> BicepExpression:
        if self._rg:
            raise ValueError("Named resource group can only be used for scope, not properties.")
        return ResourceId(self)

    @property
    def name(self) -> BicepExpression:
        if self._rg:
            raise ValueError("Named resource group can only be used for scope, not properties.")
        return ResourceName(self)


class Subscription(BicepExpression):
    def __init__(self, subscription: Optional[Union[BaseException, str]] = None, /):
        self._sub = subscription

    def resolve(self) -> str:
        if self._sub:
            return f"subscription({resolve_value(self._sub)})"
        return f"subscription()"

    @property
    def id(self) -> BicepExpression:
        if self._sub:
            raise ValueError("Named subscription can only be used for scope, not properties.")
        return ResourceId(self)

    @property
    def subscription_id(self) -> BicepExpression:
        if self._sub:
            raise ValueError("Named subscription can only be used for scope, not properties.")
        return BicepExpression(f"{self.resolve()}.subscriptionId")

    @property
    def tenant_id(self) -> BicepExpression:
        if self._sub:
            raise ValueError("Named subscription can only be used for scope, not properties.")
        return BicepExpression(f"{self.resolve()}.tenantId")

    @property
    def display_name(self) -> BicepExpression:
        if self._sub:
            raise ValueError("Named subscription can only be used for scope, not properties.")
        return BicepExpression(f"{self.resolve()}.displayName")


class PrincipalId(BicepExpression):
    def __init__(self, symbol: Union[BicepExpression, str], /) -> None:
        self._resource = symbol

    def resolve(self) -> str:
        if self.resource:
            return f"{resolve_ref(self._resource)}.properties.principalId"
        return "principalId"


class UniqueString(BicepExpression):
    def __init__(self, basestr: Union[BaseException, str], *args: Union[BicepExpression, str]) -> None:
        self._args = [basestr] + list(args)

    def resolve(self) -> str:
        arg_str = ", ".join([resolve_value(a) for a in self._args])
        return f"uniqueString({arg_str})"


class Take(BicepExpression):
    def __init__(self, value: Union[BicepExpression, str, List], take: int, /) -> None:
        self._value = value
        self._take = take

    def resolve(self) -> str:
        return f"take({resolve_value(self._value)}, {self._take})"


# class BoolLogic(BicepExpression):
#     def __init__(self, a_value: Any, b_value: Any, operator: Literal['==', '!=', '<', '>', '<=', '>=']):
#         self._a = a_value
#         self._b = b_value
#         self._op = operator

#     def resolve(self) -> str:
#         return f"{resolve_value(self._a)} {self._op} {resolve_value(self._b)}"


class Guid(BicepExpression):
    def __init__(self, basestr: Union[BicepExpression, str], *args: Union[BicepExpression, str]) -> None:
        self._args = [basestr] + list(args)

    def resolve(self) -> str:
        arg_str = ", ".join([resolve_value(a) for a in self._args])
        return f"guid({arg_str})"


class NewGuid(BicepExpression):
    def __init__(self):
        ...
    def resolve(self) -> str:
        return "newGuid()"


# class SubscriptionResourceId(BicepExpression):
#     def __init__(self, resourcetype: str, name: Enum) -> None:
#         self._resource = resourcetype
#         self._name = name.value

#     def resolve(self) -> str:
#         return f"subscriptionResourceId('{self._resource}', '{self._name}')"