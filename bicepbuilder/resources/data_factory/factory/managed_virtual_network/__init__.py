from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .managed_private_endpoint import ManagedPrivateEndpoint


class ManagedVirtualNetwork(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Managed Virtual Network."""
    managedPrivateEndpoints: List['ManagedPrivateEndpoint']
    """An array of managed private endpoints objects created in the Data Factory managed virtual network."""


class ManagedVirtualNetworkOutputs(TypedDict, total=False):
    """Outputs for ManagedVirtualNetwork"""
    name: Output[Literal['string']]
    """The name of the Managed Virtual Network."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Managed Virtual Network was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Managed Virtual Network."""


class ManagedVirtualNetworkModule(Module):
    outputs: ManagedVirtualNetworkOutputs

