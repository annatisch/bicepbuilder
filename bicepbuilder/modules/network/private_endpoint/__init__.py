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


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to. If used with private link service connection, this property must be defined as empty string."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to. If used with private link service connection, this property must be defined as empty string."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManualPrivateLinkServiceConnection(TypedDict, total=False):
    """A grouping of information about the connection to the remote resource. Used when the network admin does not have access to approve connections to the remote resource."""
    name: Required[str]
    """The name of the private link service connection."""


class ManualPrivateLinkServiceConnectionProperties(TypedDict, total=False):
    """Properties of private link service connection."""
    groupIds: Required[List[object]]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to. If used with private link service connection, this property must be defined as empty string array """
    privateLinkServiceId: Required[str]
    """The resource id of private link service."""
    requestMessage: str
    """A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS zone group to configure for the private endpoint."""
    name: str
    """The name of the Private DNS Zone Group."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


class PrivateLinkServiceConnection(TypedDict, total=False):
    """A grouping of information about the connection to the remote resource."""
    name: Required[str]
    """The name of the private link service connection."""


class PrivateLinkServiceConnectionProperties(TypedDict, total=False):
    """Properties of private link service connection."""
    groupIds: Required[List[object]]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to. If used with private link service connection, this property must be defined as empty string array """
    privateLinkServiceId: Required[str]
    """The resource id of private link service."""
    requestMessage: str
    """A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars."""


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


class PrivateEndpoint(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the private endpoint resource to create."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the private endpoint IP configuration is included."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the private endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all Resources."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class PrivateEndpointOutputs(TypedDict, total=False):
    """Outputs for PrivateEndpoint"""
    customDnsConfig: Output[Literal['array']]
    """The custom DNS configurations of the private endpoint."""
    groupId: Output[Literal['string']]
    """The group Id for the private endpoint Group."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the private endpoint."""
    networkInterfaceResourceIds: Output[Literal['array']]
    """The resource IDs of the network interfaces associated with the private endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the private endpoint was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the private endpoint."""


class PrivateEndpointBicep(Module):
    outputs: PrivateEndpointOutputs


def private_endpoint(
        bicep: IO[str],
        /,
        *,
        params: PrivateEndpoint,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/private-endpoint',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> PrivateEndpointBicep:
    symbol = "private_endpoint_" + generate_suffix()
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
    output = PrivateEndpointBicep(symbol)
    output.outputs = {
            'customDnsConfig': Output(symbol, 'customDnsConfig', 'array'),
            'groupId': Output(symbol, 'groupId', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'networkInterfaceResourceIds': Output(symbol, 'networkInterfaceResourceIds', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
