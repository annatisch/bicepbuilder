from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition. This parameter enables the encryption of Elastic SAN Volume Group using a customer-managed key. Currently, the only supported configuration is to use the same user-assigned identity for both 'managedIdentities.userAssignedResourceIds' and 'customerManagedKey.userAssignedIdentityResourceId'. Other configurations such as system-assigned identity are not supported. Ensure that the specified user-assigned identity has the 'Key Vault Crypto Service Encryption User' role access to both the key vault and the key itself. The key vault must also have purge protection enabled."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. The Elastic SAN Volume Group supports the following identity combinations: no identity is specified, only system-assigned identity is specified, only user-assigned identity is specified, and both system-assigned and user-assigned identities are specified. A maximum of one user-assigned identity is supported."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the Private Endpoint. This will be used to map to the first-party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""
    properties: Required['IpConfigurationProperties']
    """Properties of private endpoint IP configurations."""


class Lock(TypedDict, total=False):
    """Specify the type of lock."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS Zone Groups to associate the Private Endpoint. A DNS Zone Group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS Zone Group config."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS Zone Group to configure for the Private Endpoint."""
    privateDnsZoneGroupConfigs: Required[List['PrivateDnsZoneGroupConfig']]
    """The private DNS Zone Groups to associate the Private Endpoint. A DNS Zone Group can support up to 5 DNS zones."""
    name: str
    """The name of the Private DNS Zone Group."""


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
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the Private Endpoint IP configuration is included."""
    customDnsConfigs: List['CustomDnsConfig']
    """Custom DNS configurations."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the Private Endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipConfigurations: List['IpConfiguration']
    """A list of IP configurations of the Private Endpoint. This will be used to map to the first-party Service endpoints."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the Private Endpoint to."""
    lock: 'Lock'
    """Specify the type of lock."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the Private Endpoint."""
    privateDnsZoneGroup: 'PrivateDnsZoneGroup'
    """The private DNS Zone Group to configure for the Private Endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different Resource Group than the main resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    service: str
    """The subresource to deploy the Private Endpoint for. For example "vault" for a Key Vault Private Endpoint."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/Resource Groups in this deployment."""


class VirtualNetworkRule(TypedDict, total=False):
    """List of Virtual Network Rules, permitting virtual network subnet to connect to the resource through service endpoint. Each Elastic SAN Volume Group supports up to 200 virtual network rules."""
    virtualNetworkSubnetResourceId: Required[str]
    """The resource ID of the subnet in the virtual network."""


class Snapshot(TypedDict, total=False):
    """List of Elastic SAN Volume Snapshots to be created in the Elastic SAN Volume."""
    name: Required[str]
    """The name of the Elastic SAN Volume Snapshot. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""


class Volume(TypedDict, total=False):
    """List of Elastic SAN Volumes to be created in the Elastic SAN Volume Group. Elastic SAN Volume Group can contain up to 1,000 volumes."""
    name: Required[str]
    """The name of the Elastic SAN Volume. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""
    sizeGiB: Required[int]
    """Size of the Elastic SAN Volume in Gibibytes (GiB). The supported capacity ranges from 1 Gibibyte (GiB) to 64 Tebibyte (TiB), equating to 65536 Gibibytes (GiB)."""
    snapshots: List['Snapshot']
    """List of Elastic SAN Volume Snapshots to be created in the Elastic SAN Volume."""


class VolumeGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Elastic SAN Volume Group. The name can only contain lowercase letters, numbers and hyphens, and must begin and end with a letter or a number. Each hyphen must be preceded and followed by an alphanumeric character."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition. This parameter enables the encryption of Elastic SAN Volume Group using a customer-managed key. Currently, the only supported configuration is to use the same user-assigned identity for both 'managedIdentities.userAssignedResourceIds' and 'customerManagedKey.userAssignedIdentityResourceId'. Other configurations such as system-assigned identity are not supported. Ensure that the specified user-assigned identity has the 'Key Vault Crypto Service Encryption User' role access to both the key vault and the key itself. The key vault must also have purge protection enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. The Elastic SAN Volume Group supports the following identity combinations: no identity is specified, only system-assigned identity is specified, only user-assigned identity is specified, and both system-assigned and user-assigned identities are specified. A maximum of one user-assigned identity is supported."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    tags: Dict[str, object]
    """Tags of the Elastic SAN Volume Group resource."""
    virtualNetworkRules: List['VirtualNetworkRule']
    """List of Virtual Network Rules, permitting virtual network subnet to connect to the resource through service endpoint. Each Elastic SAN Volume Group supports up to 200 virtual network rules."""
    volumes: List['Volume']
    """List of Elastic SAN Volumes to be created in the Elastic SAN Volume Group. Elastic SAN Volume Group can contain up to 1,000 volumes."""


class VolumeGroupOutputs(TypedDict, total=False):
    """Outputs for VolumeGroup"""
    location: Output[Literal['string']]
    """The location of the deployed Elastic SAN Volume Group."""
    name: Output[Literal['string']]
    """The name of the deployed Elastic SAN Volume Group."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the Elastic SAN Volume Group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed Elastic SAN Volume Group."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Elastic SAN Volume Group."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity of the deployed Elastic SAN Volume Group."""
    volumes: Output[Literal['array']]
    """Details on the deployed Elastic SAN Volumes."""


class VolumeGroupModule(Module):
    outputs: VolumeGroupOutputs

