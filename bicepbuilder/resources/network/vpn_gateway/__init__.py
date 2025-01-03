from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .nat_rule import NatRule
    from .vpn_connection import VpnConnection


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class NetworkVpnGateway(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the VPN gateway."""
    virtualHubResourceId: Required[str]
    """The resource ID of a virtual Hub to connect to. Note: The virtual Hub and Gateway must be deployed into the same location."""
    bgpSettings: Dict[str, object]
    """BGP settings details."""
    enableBgpRouteTranslationForNat: bool
    """Enable BGP routes translation for NAT on this VPN gateway."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    isRoutingPreferenceInternet: bool
    """Enable routing preference property for the public IP interface of the VPN gateway."""
    location: str
    """Location where all resources will be created."""
    lock: 'Lock'
    """The lock settings of the service."""
    natRules: List['NatRule']
    """List of all the NAT Rules to associate with the gateway."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vpnConnections: List['VpnConnection']
    """The VPN connections to create in the VPN gateway."""
    vpnGatewayScaleUnit: int
    """The scale unit for this VPN gateway."""


class NetworkVpnGatewayOutputs(TypedDict, total=False):
    """Outputs for NetworkVpnGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the VPN gateway."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the VPN gateway was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the VPN gateway."""


class NetworkVpnGatewayModule(Module):
    outputs: NetworkVpnGatewayOutputs

