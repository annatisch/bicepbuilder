from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .administrator import Administrator
    from .configuration import Configuration
    from .database import Database
    from .firewall_rule import FirewallRule


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Required if 'cMKKeyName' is not empty."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, using 'latest'."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


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
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    metricCategories: List['MetricCategory']
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    name: str
    """The name of the diagnostic setting."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator']]]
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
    """Configuration details for private endpoints. Used when the desired connectivy mode is 'Public Access' and 'delegatedSubnetResourceId' is NOT used."""
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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class DbForPostgreSqlFlexibleServer(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the PostgreSQL flexible server."""
    skuName: Required[str]
    """The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3."""
    tier: Required[Literal['Burstable', 'GeneralPurpose', 'MemoryOptimized']]
    """The tier of the particular SKU. Tier must align with the 'skuName' property. Example, tier cannot be 'Burstable' if skuName is 'Standard_D4s_v3'."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. Required if 'cMKKeyName' is not empty."""
    pointInTimeUTC: str
    """Required if 'createMode' is set to 'PointInTimeRestore'."""
    sourceServerResourceId: str
    """Required if 'createMode' is set to 'PointInTimeRestore'."""
    administratorLogin: str
    """The administrator login name for the server. Can only be specified when the PostgreSQL server is being created."""
    administratorLoginPassword: str
    """The administrator login password."""
    administrators: List['Administrator']
    """The Azure AD administrators when AAD authentication enabled."""
    availabilityZone: Literal['', '1', '2', '3']
    """Availability zone information of the server. Default will have no preference set."""
    backupRetentionDays: int
    """Backup retention days for the server."""
    configurations: List['Configuration']
    """The configurations to create in the server."""
    createMode: Literal['Create', 'Default', 'GeoRestore', 'PointInTimeRestore', 'Replica', 'Update']
    """The mode to create a new PostgreSQL server."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition."""
    databases: List['Database']
    """The databases to create in the server."""
    delegatedSubnetResourceId: str
    """Delegated subnet arm resource ID. Used when the desired connectivity mode is 'Private Access' - virtual network integration."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallRules: List['FirewallRule']
    """The firewall rules to create in the PostgreSQL flexible server."""
    geoRedundantBackup: Literal['Disabled', 'Enabled']
    """A value indicating whether Geo-Redundant backup is enabled on the server. Should be disabled if 'cMKKeyName' is not empty."""
    highAvailability: Literal['Disabled', 'SameZone', 'ZoneRedundant']
    """The mode for high availability."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maintenanceWindow: Dict[str, object]
    """Properties for the maintenence window. If provided, 'customWindow' property must exist and set to 'Enabled'."""
    privateDnsZoneArmResourceId: str
    """Private dns zone arm resource ID. Used when the desired connectivity mode is 'Private Access' and required when 'delegatedSubnetResourceId' is used. The Private DNS Zone must be linked to the Virtual Network referenced in 'delegatedSubnetResourceId'."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. Used when the desired connectivy mode is 'Public Access' and 'delegatedSubnetResourceId' is NOT used."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    storageSizeGB: Literal[32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    """Max storage allowed for a server."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tenantId: str
    """Tenant id of the server."""
    version: Literal['11', '12', '13', '14', '15', '16']
    """PostgreSQL Server version."""


class DbForPostgreSqlFlexibleServerOutputs(TypedDict, total=False):
    """Outputs for DbForPostgreSqlFlexibleServer"""
    fqdn: Output[Literal['string']]
    """The FQDN of the PostgreSQL Flexible server."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed PostgreSQL Flexible server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed PostgreSQL Flexible server."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed PostgreSQL Flexible server."""


class DbForPostgreSqlFlexibleServerModule(Module):
    outputs: DbForPostgreSqlFlexibleServerOutputs

