from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class NetworkVpnGatewayBicep(Module):
    outputs: NetworkVpnGatewayOutputs


def network_vpn_gateway(
        bicep: IO[str],
        params: NetworkVpnGateway,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkVpnGatewayBicep:
    symbol = "network_vpn_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-gateway:{tag}' = {{\n")
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
    output = NetworkVpnGatewayBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
