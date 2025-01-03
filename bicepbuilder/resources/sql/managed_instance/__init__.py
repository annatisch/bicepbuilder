from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .database import Database
    from .key import Key


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


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Reservation Purchaser', 'Role Based Access Control Administrator (Preview)', 'SQL DB Contributor', 'SQL Managed Instance Contributor', 'SQL Security Manager', 'SQL Server Contributor', 'SqlDb Migration Role', 'SqlMI Migration Role', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class SqlManagedInstance(TypedDict, total=False):
    """"""
    administratorLogin: Required[str]
    """The username used to establish jumpbox VMs."""
    administratorLoginPassword: Required[str]
    """The password given to the admin user."""
    name: Required[str]
    """The name of the SQL managed instance."""
    subnetResourceId: Required[str]
    """The fully qualified resource ID of the subnet on which the SQL managed instance will be placed."""
    primaryUserAssignedIdentityId: str
    """The resource ID of a user assigned identity to be used by default. Required if "userAssignedIdentities" is not empty."""
    administratorsObj: Dict[str, object]
    """The administrator configuration."""
    collation: str
    """Collation of the managed instance."""
    databases: List['Database']
    """Databases to create in this server."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    dnsZonePartner: str
    """The resource ID of another managed instance whose DNS zone this managed instance will share after creation."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionProtectorObj: Dict[str, object]
    """The encryption protection configuration."""
    hardwareFamily: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    instancePoolResourceId: str
    """The resource ID of the instance pool this managed server belongs to."""
    keys: List['Key']
    """The keys to configure."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses)."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    managedInstanceCreateMode: Literal['Default', 'PointInTimeRestore']
    """Specifies the mode of database creation. Default: Regular instance creation. Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified."""
    minimalTlsVersion: Literal['1.0', '1.1', '1.2', 'None']
    """Minimal TLS version allowed."""
    proxyOverride: Literal['Default', 'Proxy', 'Redirect']
    """Connection type used for connecting to the instance."""
    publicDataEndpointEnabled: bool
    """Whether or not the public data endpoint is enabled."""
    requestedBackupStorageRedundancy: Literal['Geo', 'GeoZone', 'Local', 'Zone']
    """The storage account type used to store backups for this database."""
    restorePointInTime: str
    """Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    securityAlertPoliciesObj: Dict[str, object]
    """The security alert policy configuration."""
    servicePrincipal: Literal['None', 'SystemAssigned']
    """Service principal type. If using AD Authentication and applying Admin, must be set to """
    skuName: str
    """The name of the SKU, typically, a letter + Number code, e.g. P3."""
    skuTier: str
    """The tier or edition of the particular SKU, e.g. Basic, Premium."""
    sourceManagedInstanceId: str
    """The resource identifier of the source managed instance associated with create operation of this instance."""
    storageSizeInGB: int
    """Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments of 32 GB allowed only."""
    tags: Dict[str, object]
    """Tags of the resource."""
    timezoneId: str
    """ID of the timezone. Allowed values are timezones supported by Windows."""
    vCores: int
    """The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80."""
    vulnerabilityAssessmentsObj: Dict[str, object]
    """The vulnerability assessment configuration."""
    zoneRedundant: bool
    """Whether or not multi-az is enabled."""


class SqlManagedInstanceOutputs(TypedDict, total=False):
    """Outputs for SqlManagedInstance"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed managed instance."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed managed instance."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed managed instance."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class SqlManagedInstanceModule(Module):
    outputs: SqlManagedInstanceOutputs

