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


class MetricCategory(TypedDict, total=False):
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    category: Required[str]
    """Name of a Diagnostic Metric category for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    metricCategories: List['MetricCategory']
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Elastic SAN Network Admin', 'Elastic SAN Owner', 'Elastic SAN Reader', 'Elastic SAN Volume Group Owner']]]
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
    """List of Elastic SAN Volume Groups to be created in the Elastic SAN. An Elastic SAN can have a maximum of 200 volume groups."""
    name: Required[str]
    """The name of the Elastic SAN Volume Group. The name can only contain lowercase letters, numbers and hyphens, and must begin and end with a letter or a number. Each hyphen must be preceded and followed by an alphanumeric character."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition. This parameter enables the encryption of Elastic SAN Volume Group using a customer-managed key. Currently, the only supported configuration is to use the same user-assigned identity for both 'managedIdentities.userAssignedResourceIds' and 'customerManagedKey.userAssignedIdentityResourceId'. Other configurations such as system-assigned identity are not supported. Ensure that the specified user-assigned identity has the 'Key Vault Crypto Service Encryption User' role access to both the key vault and the key itself. The key vault must also have purge protection enabled."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. The Elastic SAN Volume Group supports the following identity combinations: no identity is specified, only system-assigned identity is specified, only user-assigned identity is specified, and both system-assigned and user-assigned identities are specified. A maximum of one user-assigned identity is supported."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    virtualNetworkRules: List['VirtualNetworkRule']
    """List of Virtual Network Rules, permitting virtual network subnet to connect to the resource through service endpoint. Each Elastic SAN Volume Group supports up to 200 virtual network rules."""
    volumes: List['Volume']
    """List of Elastic SAN Volumes to be created in the Elastic SAN Volume Group. Elastic SAN Volume Group can contain up to 1,000 volumes."""


class ElasticSan(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Elastic SAN. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""
    availabilityZone: Literal[1, 2, 3]
    """Configuration of the availability zone for the Elastic SAN. Required if """
    baseSizeTiB: int
    """Size of the Elastic SAN base capacity in Tebibytes (TiB). The supported capacity ranges from 1 Tebibyte (TiB) to 400 Tebibytes (TiB)."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    extendedCapacitySizeTiB: int
    """Size of the Elastic SAN additional capacity in Tebibytes (TiB). The supported capacity ranges from 0 Tebibyte (TiB) to 600 Tebibytes (TiB)."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Whether or not public network access is allowed for this resource. For security reasons it should be """
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Elastic SAN Network Admin', 'Elastic SAN Owner', 'Elastic SAN Reader', 'Elastic SAN Volume Group Owner']]]
    """Array of role assignments to create."""
    sku: Literal['Premium_LRS', 'Premium_ZRS']
    """Specifies the SKU for the Elastic SAN."""
    tags: Dict[str, object]
    """Tags of the Elastic SAN resource."""
    volumeGroups: List['VolumeGroup']
    """List of Elastic SAN Volume Groups to be created in the Elastic SAN. An Elastic SAN can have a maximum of 200 volume groups."""


class ElasticSanOutputs(TypedDict, total=False):
    """Outputs for ElasticSan"""
    location: Output[Literal['string']]
    """The location of the deployed Elastic SAN."""
    name: Output[Literal['string']]
    """The name of the deployed Elastic SAN."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed Elastic SAN."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Elastic SAN."""
    volumeGroups: Output[Literal['array']]
    """Details on the deployed Elastic SAN Volume Groups."""


class ElasticSanBicep(Module):
    outputs: ElasticSanOutputs


def elastic_san(
        bicep: IO[str],
        params: ElasticSan,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ElasticSanBicep:
    symbol = "elastic_san_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/elastic-san/elastic-san:{tag}' = {{\n")
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
    output = ElasticSanBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'volumeGroups': Output(symbol, 'volumeGroups', 'array'),
        }

    return output
