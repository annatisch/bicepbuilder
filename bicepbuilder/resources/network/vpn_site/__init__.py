from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
    Output,
)


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    name: str
    """The name (as GUID) of the role assignment. If not provided, a GUID will be generated."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class NetworkVpnSite(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the VPN Site."""
    virtualWanId: Required[str]
    """Resource ID of the virtual WAN to link to."""
    addressPrefixes: List[object]
    """An array of IP address ranges that can be used by subnets of the virtual network. Required if no bgpProperties or VPNSiteLinks are configured."""
    bgpProperties: Dict[str, object]
    """BGP settings details. Note: This is a deprecated property, please use the corresponding VpnSiteLinks property instead. Required if no addressPrefixes or VPNSiteLinks are configured."""
    deviceProperties: Dict[str, object]
    """List of properties of the device."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipAddress: str
    """The IP-address for the VPN-site. Note: This is a deprecated property, please use the corresponding VpnSiteLinks property instead."""
    isSecuritySite: bool
    """IsSecuritySite flag."""
    location: str
    """Location where all resources will be created."""
    lock: 'Lock'
    """The lock settings of the service."""
    o365Policy: Dict[str, object]
    """The Office365 breakout policy."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vpnSiteLinks: List[object]
    """List of all VPN site links."""


class NetworkVpnSiteOutputs(TypedDict, total=False):
    """Outputs for NetworkVpnSite"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the VPN site."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the VPN site was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the VPN site."""


class NetworkVpnSiteModule(Module):
    outputs: NetworkVpnSiteOutputs


def _network_vpn_site(
        bicep: IO[str],
        params: NetworkVpnSite,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkVpnSiteModule:
    symbol = "network_vpn_site_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/vpn-site:{tag}' = {{\n")
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
    output = NetworkVpnSiteModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
