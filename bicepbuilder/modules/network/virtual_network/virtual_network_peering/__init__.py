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


class VirtualNetworkPeering(TypedDict, total=False):
    """"""
    remoteVirtualNetworkResourceId: Required[str]
    """The Resource ID of the VNet that is this Local VNet is being peered to. Should be in the format of a Resource ID."""
    allowForwardedTraffic: bool
    """Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network. Default is true."""
    allowGatewayTransit: bool
    """If gateway links can be used in remote virtual networking to link to this virtual network. Default is false."""
    allowVirtualNetworkAccess: bool
    """Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space. Default is true."""
    doNotVerifyRemoteGateways: bool
    """If we need to verify the provisioning state of the remote gateway. Default is true."""
    name: str
    """The Name of VNET Peering resource. If not provided, default value will be localVnetName-remoteVnetName."""
    useRemoteGateways: bool
    """If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway. Default is false."""


class VirtualNetworkPeeringOutputs(TypedDict, total=False):
    """Outputs for VirtualNetworkPeering"""
    name: Output[Literal['string']]
    """The name of the virtual network peering."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual network peering was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual network peering."""


class VirtualNetworkPeeringBicep(Module):
    outputs: VirtualNetworkPeeringOutputs

