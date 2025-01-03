from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class KeyValue(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the key."""
    value: Required[str]
    """The value of the key-value."""
    contentType: str
    """The content type of the key-values value. Providing a proper content-type can enable transformations of values when they are retrieved by applications."""
    tags: Dict[str, object]
    """Tags of the resource."""


class KeyValueOutputs(TypedDict, total=False):
    """Outputs for KeyValue"""
    name: Output[Literal['string']]
    """The name of the key values."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the batch account was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the key values."""


class KeyValueModule(Module):
    outputs: KeyValueOutputs

