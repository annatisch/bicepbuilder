from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class VirtualHub(TypedDict, total=False):
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


class VirtualHubOutputs(TypedDict, total=False):
    """Outputs for VirtualHub"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the virtual hub."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual hub was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual hub."""


class VirtualHubBicep(Module):
    outputs: VirtualHubOutputs


def virtual_hub(
        bicep: IO[str],
        /,
        *,
        params: VirtualHub,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/virtual-hub',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> VirtualHubBicep:
    symbol = "virtual_hub_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} '{registry_prefix}/{path}:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = VirtualHubBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
