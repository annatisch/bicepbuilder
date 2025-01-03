from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class VirtualNetworkLink(TypedDict, total=False):
    """"""
    virtualNetworkResourceId: Required[str]
    """Link to another virtual network resource ID."""
    metadata: Dict[str, object]
    """Metadata attached to the forwarding rule."""
    name: str
    """The name of the virtual network link."""


class VirtualNetworkLinkOutputs(TypedDict, total=False):
    """Outputs for VirtualNetworkLink"""
    name: Output[Literal['string']]
    """The name of the deployed virtual network link."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed virtual network link."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed virtual network link."""


class VirtualNetworkLinkModule(Module):
    outputs: VirtualNetworkLinkOutputs

