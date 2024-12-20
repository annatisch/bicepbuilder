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


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class VnetRoutesStaticRoute(TypedDict, total=False):
    """The routes from the virtual hub to virtual network connections."""


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


class P2SVpnGateway(TypedDict, total=False):
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
    vpnClientAddressPoolAddressPrefixes: List[object]
    """The address prefixes for the VPN Client Address Pool."""
    vpnGatewayScaleUnit: int
    """The scale unit of the VPN Gateway."""
    vpnServerConfigurationResourceId: str
    """The resource ID of the VPN Server Configuration."""


class P2SVpnGatewayOutputs(TypedDict, total=False):
    """Outputs for P2SVpnGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the user VPN configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the user VPN configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the user VPN configuration."""


class P2SVpnGatewayBicep(Module):
    outputs: P2SVpnGatewayOutputs


def p2s_vpn_gateway(
        bicep: IO[str],
        /,
        *,
        params: P2SVpnGateway,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/p2s-vpn-gateway',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> P2SVpnGatewayBicep:
    symbol = "p2s_vpn_gateway_" + generate_suffix()
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
    output = P2SVpnGatewayBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
