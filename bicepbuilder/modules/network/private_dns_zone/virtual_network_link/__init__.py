from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class VirtualNetworkLink(TypedDict, total=False):
    """"""
    virtualNetworkResourceId: Required[str]
    """Link to another virtual network resource ID."""
    location: str
    """The location of the PrivateDNSZone. Should be global."""
    name: str
    """The name of the virtual network link."""
    registrationEnabled: bool
    """Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled?."""
    resolutionPolicy: str
    """The resolution policy on the virtual network link. Only applicable for virtual network links to privatelink zones, and for A,AAAA,CNAME queries. When set to """
    tags: Dict[str, object]
    """Tags of the resource."""


class VirtualNetworkLinkOutputs(TypedDict, total=False):
    """Outputs for VirtualNetworkLink"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed virtual network link."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed virtual network link."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed virtual network link."""


class VirtualNetworkLinkBicep(Module):
    outputs: VirtualNetworkLinkOutputs

