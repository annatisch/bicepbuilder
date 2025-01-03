from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class StaticRoute(TypedDict, total=False):
    """The static route configuration for the P2S VPN Gateway."""
    addressPrefixes: List[object]
    """The address prefixes of the static route."""
    name: str
    """The name of the static route."""
    nextHopIpAddress: str
    """The next hop IP of the static route."""


class StaticRoutesConfig(TypedDict, total=False):
    """The static route configuration for the P2S VPN Gateway."""
    vnetLocalRouteOverrideCriteria: str
    """Determines whether the NVA in a SPOKE VNET is bypassed for traffic with destination in spoke."""


class VnetRoutesStaticRoute(TypedDict, total=False):
    """The routes from the virtual hub to virtual network connections."""
    staticRoutes: List['StaticRoute']
    """The static route configuration for the P2S VPN Gateway."""
    staticRoutesConfig: 'StaticRoutesConfig'
    """The static route configuration for the P2S VPN Gateway."""


class NetworkP2SVpnGateway(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the P2S VPN Gateway."""
    virtualHubResourceId: Required[str]
    """The resource ID of the gateways virtual hub."""
    associatedRouteTableName: Literal['defaultRouteTable', 'noneRouteTable']
    """The name of the associated route table. Required if deploying in a Secure Virtual Hub; cannot be a custom route table."""
    customDnsServers: List[object]
    """The custom DNS servers for the P2S VPN Gateway."""
    enableInternetSecurity: bool
    """Enable/Disable Internet Security; "Propagate Default Route"."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    inboundRouteMapResourceId: str
    """The Resource ID of the inbound route map."""
    isRoutingPreferenceInternet: bool
    """The routing preference for the P2S VPN Gateway, Internet or Microsoft network."""
    location: str
    """Location where all resources will be created."""
    lock: 'Lock'
    """The lock settings of the service."""
    outboundRouteMapResourceId: str
    """The Resource ID of the outbound route map."""
    p2SConnectionConfigurationsName: str
    """The name of the P2S Connection Configuration."""
    propagatedLabelNames: List[object]
    """The Labels to propagate routes to."""
    propagatedRouteTableNames: List[object]
    """The names of the route tables to propagate to the P2S VPN Gateway."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vnetRoutesStaticRoutes: 'VnetRoutesStaticRoute'
    """The routes from the virtual hub to virtual network connections."""
    vpnClientAddressPoolAddressPrefixes: List[object]
    """The address prefixes for the VPN Client Address Pool."""
    vpnGatewayScaleUnit: int
    """The scale unit of the VPN Gateway."""
    vpnServerConfigurationResourceId: str
    """The resource ID of the VPN Server Configuration."""


class NetworkP2SVpnGatewayOutputs(TypedDict, total=False):
    """Outputs for NetworkP2SVpnGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the user VPN configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the user VPN configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the user VPN configuration."""


class NetworkP2SVpnGatewayModule(Module):
    outputs: NetworkP2SVpnGatewayOutputs

