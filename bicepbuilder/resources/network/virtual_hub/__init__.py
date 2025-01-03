from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .hub_route_table import HubRouteTable
    from .hub_virtual_network_connection import HubVirtualNetworkConnection


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class NetworkVirtualHub(TypedDict, total=False):
    """"""
    addressPrefix: Required[str]
    """Address-prefix for this VirtualHub."""
    name: Required[str]
    """The virtual hub name."""
    virtualWanId: Required[str]
    """Resource ID of the virtual WAN to link to."""
    allowBranchToBranchTraffic: bool
    """Flag to control transit for VirtualRouter hub."""
    azureFirewallResourceId: str
    """Resource ID of the Azure Firewall to link to."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    expressRouteGatewayId: str
    """Resource ID of the Express Route Gateway to link to."""
    hubRouteTables: List['HubRouteTable']
    """Route tables to create for the virtual hub."""
    hubRoutingPreference: Literal['', 'ASPath', 'ExpressRoute', 'VpnGateway']
    """The preferred routing preference for this virtual hub."""
    hubVirtualNetworkConnections: List['HubVirtualNetworkConnection']
    """Virtual network connections to create for the virtual hub."""
    internetToFirewall: bool
    """Configures Routing Intent to forward Internet traffic (0.0.0.0/0) to Azure Firewall. Default is true."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    p2SVpnGatewayId: str
    """Resource ID of the Point-to-Site VPN Gateway to link to."""
    preferredRoutingGateway: Literal['', 'ExpressRoute', 'None', 'VpnGateway']
    """The preferred routing gateway types."""
    privateToFirewall: bool
    """Configures Routing Intent to forward Private traffic (RFC 1918) to Azure Firewall. Default is true."""
    routeTableRoutes: List[object]
    """VirtualHub route tables."""
    securityPartnerProviderId: str
    """ID of the Security Partner Provider to link to."""
    securityProviderName: str
    """The Security Provider name."""
    sku: Literal['Basic', 'Standard']
    """The sku of this VirtualHub."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualHubRouteTableV2s: List[object]
    """List of all virtual hub route table v2s associated with this VirtualHub."""
    virtualRouterAsn: int
    """VirtualRouter ASN."""
    virtualRouterIps: List[object]
    """VirtualRouter IPs."""
    vpnGatewayId: str
    """Resource ID of the VPN Gateway to link to."""


class NetworkVirtualHubOutputs(TypedDict, total=False):
    """Outputs for NetworkVirtualHub"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the virtual hub."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual hub was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual hub."""


class NetworkVirtualHubModule(Module):
    outputs: NetworkVirtualHubOutputs

