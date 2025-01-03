from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .administrator import Administrator
    from .database import Database
    from .firewall_rule import FirewallRule


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Required if 'customerManagedKey' is not empty."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition to use for the managed service."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class CustomerManagedKeyGeo(TypedDict, total=False):
    """The customer managed key definition to use when geoRedundantBackup is "Enabled"."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'MySQL Backup And Export Operator', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class DbForMySqlFlexibleServer(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the MySQL flexible server."""
    skuName: Required[str]
    """The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3."""
    tier: Required[Literal['Burstable', 'GeneralPurpose', 'MemoryOptimized']]
    """The tier of the particular SKU. Tier must align with the "skuName" property. Example, tier cannot be "Burstable" if skuName is "Standard_D4s_v3"."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. Required if 'customerManagedKey' is not empty."""
    privateDnsZoneResourceId: str
    """Private dns zone arm resource ID. Used when the desired connectivity mode is "Private Access". Required if "delegatedSubnetResourceId" is used and the Private DNS Zone name must end with mysql.database.azure.com in order to be linked to the MySQL Flexible Server."""
    restorePointInTime: str
    """Restore point creation time (ISO8601 format), specifying the time to restore from. Required if "createMode" is set to "PointInTimeRestore"."""
    sourceServerResourceId: str
    """The source MySQL server ID. Required if "createMode" is set to "PointInTimeRestore"."""
    storageAutoGrow: Literal['Disabled', 'Enabled']
    """Enable Storage Auto Grow or not. Storage auto-growth prevents a server from running out of storage and becoming read-only. Required if "highAvailability" is not "Disabled"."""
    administratorLogin: str
    """The administrator login name of a server. Can only be specified when the MySQL server is being created."""
    administratorLoginPassword: str
    """The administrator login password."""
    administrators: List['Administrator']
    """The Azure AD administrators when AAD authentication enabled."""
    availabilityZone: Literal['', '1', '2', '3']
    """Availability zone information of the server. Default will have no preference set."""
    backupRetentionDays: int
    """Backup retention days for the server."""
    createMode: Literal['Default', 'GeoRestore', 'PointInTimeRestore', 'Replica']
    """The mode to create a new MySQL server."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition to use for the managed service."""
    customerManagedKeyGeo: 'CustomerManagedKeyGeo'
    """The customer managed key definition to use when geoRedundantBackup is "Enabled"."""
    databases: List['Database']
    """The databases to create in the server."""
    delegatedSubnetResourceId: str
    """Delegated subnet arm resource ID. Used when the desired connectivity mode is "Private Access" - virtual network integration. Delegation must be enabled on the subnet for MySQL Flexible Servers and subnet CIDR size is /29."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallRules: List['FirewallRule']
    """The firewall rules to create in the MySQL flexible server."""
    geoRedundantBackup: Literal['Disabled', 'Enabled']
    """A value indicating whether Geo-Redundant backup is enabled on the server. If "Enabled" and "cMKKeyName" is not empty, then "geoBackupCMKKeyVaultResourceId" and "cMKUserAssignedIdentityResourceId" are also required."""
    highAvailability: Literal['Disabled', 'SameZone', 'ZoneRedundant']
    """The mode for High Availability (HA). It is not supported for the Burstable pricing tier and Zone redundant HA can only be set during server provisioning."""
    highAvailabilityZone: str
    """Standby availability zone information of the server. Default will have no preference set."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maintenanceWindow: Dict[str, object]
    """Properties for the maintenence window. If provided, "customWindow" property must exist and set to "Enabled"."""
    replicationRole: Literal['None', 'Replica', 'Source']
    """The replication role."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    storageAutoIoScaling: Literal['Disabled', 'Enabled']
    """Enable IO Auto Scaling or not. The server scales IOPs up or down automatically depending on your workload needs."""
    storageIOPS: int
    """Storage IOPS for a server. Max IOPS are determined by compute size."""
    storageSizeGB: Literal[20, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    """Max storage allowed for a server. In all compute tiers, the minimum storage supported is 20 GiB and maximum is 16 TiB."""
    tags: Dict[str, object]
    """Tags of the resource."""
    version: Literal['5.7', '8.0.21']
    """MySQL Server version."""


class DbForMySqlFlexibleServerOutputs(TypedDict, total=False):
    """Outputs for DbForMySqlFlexibleServer"""
    fqdn: Output[Literal['string']]
    """The FQDN of the MySQL Flexible server."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed MySQL Flexible server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed MySQL Flexible server."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed MySQL Flexible server."""


class DbForMySqlFlexibleServerModule(Module):
    outputs: DbForMySqlFlexibleServerOutputs

