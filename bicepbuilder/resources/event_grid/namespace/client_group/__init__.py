from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ClientGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Client Group."""
    query: Required[str]
    """The grouping query for the clients."""
    description: str
    """Description of the Client Group."""


class ClientGroupOutputs(TypedDict, total=False):
    """Outputs for ClientGroup"""
    name: Output[Literal['string']]
    """The name of the Client Group."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Client Group was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Client Group."""


class ClientGroupModule(Module):
    outputs: ClientGroupOutputs

