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


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class VpnClientIpsecPolicy(TypedDict, total=False):
    """The IPsec policies for the configuration."""
    dhGroup: str
    """The Diffie-Hellman group used in IKE phase 1. Required if using IKEv2."""
    ikeEncryption: str
    """The encryption algorithm used in IKE phase 1. Required if using IKEv2."""
    ikeIntegrity: str
    """The integrity algorithm used in IKE phase 1. Required if using IKEv2."""
    ipsecEncryption: str
    """The encryption algorithm used in IKE phase 2. Required if using IKEv2."""
    ipsecIntegrity: str
    """The integrity algorithm used in IKE phase 2. Required if using IKEv2."""
    pfsGroup: str
    """The Perfect Forward Secrecy (PFS) group used in IKE phase 2. Required if using IKEv2."""
    saDataSizeKilobytes: int
    """The size of the SA data in kilobytes. Required if using IKEv2."""
    salfetimeSeconds: int
    """The lifetime of the SA in seconds. Required if using IKEv2."""


class NetworkVpnServerConfiguration(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the user VPN configuration."""
    aadAudience: str
    """The audience for the AAD/Entra authentication. Required if configuring Entra ID authentication."""
    aadIssuer: str
    """The issuer for the AAD/Entra authentication. Required if configuring Entra ID authentication."""
    aadTenant: str
    """The audience for the AAD/Entra authentication. Required if configuring Entra ID authentication."""
    radiusServerAddress: str
    """The address of the RADIUS server. Required if configuring a single RADIUS."""
    radiusServerSecret: str
    """The RADIUS server secret. Required if configuring a single RADIUS server."""
    vpnClientRootCertificates: List[object]
    """The VPN Client root certificate public keys for the configuration. Required if using certificate authentication."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location where all resources will be created."""
    lock: 'Lock'
    """The lock settings of the service."""
    p2sConfigurationPolicyGroups: List[object]
    """The P2S configuration policy groups for the configuration."""
    radiusClientRootCertificates: List[object]
    """The revoked RADIUS client certificates for the configuration."""
    radiusServerRootCertificates: List[object]
    """The root certificates of the RADIUS server."""
    radiusServers: List[object]
    """The list of RADIUS servers. Required if configuring multiple RADIUS servers."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vpnAuthenticationTypes: Literal['AAD', 'Certificate', 'Radius']
    """The authentication types for the VPN configuration."""
    vpnClientIpsecPolicies: List['VpnClientIpsecPolicy']
    """The IPsec policies for the configuration."""
    vpnClientRevokedCertificates: List[object]
    """The revoked VPN Client certificate thumbprints for the configuration."""
    vpnProtocols: Literal['IkeV2', 'OpenVPN']
    """The allowed VPN protocols for the configuration."""


class NetworkVpnServerConfigurationOutputs(TypedDict, total=False):
    """Outputs for NetworkVpnServerConfiguration"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the user VPN configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the user VPN configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the user VPN configuration."""


class NetworkVpnServerConfigurationBicep(Module):
    outputs: NetworkVpnServerConfigurationOutputs


def network_vpn_server_configuration(
        bicep: IO[str],
        params: NetworkVpnServerConfiguration,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkVpnServerConfigurationBicep:
    symbol = "network_vpn_server_configuration_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-server-configuration:{tag}' = {{\n")
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
    output = NetworkVpnServerConfigurationBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
