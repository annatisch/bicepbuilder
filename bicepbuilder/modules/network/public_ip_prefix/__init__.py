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


class IpTag(TypedDict, total=False):
    """The list of tags associated with the public IP prefix."""
    ipTagType: Required[str]
    """The IP tag type."""
    tag: Required[str]
    """The IP tag."""


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
    roleDefinitionIdOrName: Required[str]
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


class NetworkPublicIpPrefix(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Public IP Prefix."""
    prefixLength: Required[int]
    """Length of the Public IP Prefix."""
    customIPPrefix: Dict[str, object]
    """The custom IP address prefix that this prefix is associated with. A custom IP address prefix is a contiguous range of IP addresses owned by an external customer and provisioned into a subscription. When a custom IP prefix is in Provisioned, Commissioning, or Commissioned state, a linked public IP prefix can be created. Either as a subset of the custom IP prefix range or the entire range."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipTags: List['IpTag']
    """The list of tags associated with the public IP prefix."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    publicIPAddressVersion: Literal['IPv4', 'IPv6']
    """The public IP address version."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tier: Literal['Global', 'Regional']
    """Tier of a public IP prefix SKU. If set to """
    zones: Literal[1, 2, 3]
    """A list of availability zones denoting the IP allocated for the resource needs to come from. This is only applicable for regional public IP prefixes and must be empty for global public IP prefixes."""


class NetworkPublicIpPrefixOutputs(TypedDict, total=False):
    """Outputs for NetworkPublicIpPrefix"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the public IP prefix."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the public IP prefix was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the public IP prefix."""


class NetworkPublicIpPrefixBicep(Module):
    outputs: NetworkPublicIpPrefixOutputs


def network_public_ip_prefix(
        bicep: IO[str],
        params: NetworkPublicIpPrefix,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkPublicIpPrefixBicep:
    symbol = "network_public_ip_prefix_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/public-ip-prefix:{tag}' = {{\n")
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
    output = NetworkPublicIpPrefixBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
