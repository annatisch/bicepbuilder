from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class HubVirtualNetworkConnection(TypedDict, total=False):
    """"""
    name: Required[str]
    """The connection name."""
    remoteVirtualNetworkId: Required[str]
    """Resource ID of the virtual network to link to."""
    enableInternetSecurity: bool
    """Enable internet security."""
    routingConfiguration: Dict[str, object]
    """Routing Configuration indicating the associated and propagated route tables for this connection."""


class HubVirtualNetworkConnectionOutputs(TypedDict, total=False):
    """Outputs for HubVirtualNetworkConnection"""
    name: Output[Literal['string']]
    """The name of the virtual hub connection."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual hub connection was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual hub connection."""


class HubVirtualNetworkConnectionModule(Module):
    outputs: HubVirtualNetworkConnectionOutputs

