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


class LinkedStorageAccount(TypedDict, total=False):
    """List of Storage Accounts to be linked. Required if 'forceCmkForQuery' is set to 'true' and 'savedSearches' is not empty."""
    name: Required[str]
    """Name of the link."""
    storageAccountIds: Required[List[object]]
    """Linked storage accounts resources Ids."""


class DataExport(TypedDict, total=False):
    """LAW data export instances to be deployed."""
    name: Required[str]
    """Name of the data export."""
    tableNames: Required[List[object]]
    """The list of table names to export."""
    enable: bool
    """Enable or disable the data export."""


class Destination(TypedDict, total=False):
    """The destination of the data export."""
    resourceId: Required[str]
    """The destination resource ID."""


class MetaData(TypedDict, total=False):
    """The destination metadata."""
    eventHubName: str
    """Allows to define an Event Hub name. Not applicable when destination is Storage Account."""


class DataSource(TypedDict, total=False):
    """LAW data sources to configure."""
    kind: Required[str]
    """The kind of data source."""
    name: Required[str]
    """Name of the data source."""
    counterName: str
    """Counter name to configure when kind is WindowsPerformanceCounter."""
    eventLogName: str
    """The name of the event log to configure when kind is WindowsEvent."""
    eventTypes: List[object]
    """The event types to configure when kind is WindowsEvent."""
    instanceName: str
    """Name of the instance to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    intervalSeconds: int
    """Interval in seconds to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    linkedResourceId: str
    """The resource id of the resource that will be linked to the workspace."""
    objectName: str
    """Name of the object to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    performanceCounters: List[object]
    """List of counters to configure when the kind is LinuxPerformanceObject."""
    state: str
    """State to configure when kind is IISLogs or LinuxSyslogCollection or LinuxPerformanceCollection."""
    syslogName: str
    """System log to configure when kind is LinuxSyslog."""
    syslogSeverities: List[object]
    """Severities to configure when kind is LinuxSyslog."""
    tags: Dict[str, object]
    """Tags to configure in the resource."""


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
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    useThisWorkspace: bool
    """Instead of using an external reference, use the deployed instance as the target for its diagnostic settings. If set to """
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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


class GallerySolution(TypedDict, total=False):
    """List of gallerySolutions to be created in the log analytics workspace."""
    name: Required[str]
    """Name of the solution."""


class Plan(TypedDict, total=False):
    """Plan for solution object supported by the OperationsManagement resource provider."""
    product: Required[str]
    """The product name of the deployed solution."""
    name: str
    """Name of the solution to be created."""
    publisher: str
    """The publisher name of the deployed solution. For Microsoft published gallery solution, it is """


class LinkedService(TypedDict, total=False):
    """List of services to be linked."""
    name: Required[str]
    """Name of the linked service."""
    resourceId: str
    """The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require read access."""
    writeAccessResourceId: str
    """The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require write access."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Only one type of identity is supported: system-assigned or user-assigned, but not both."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


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


class SavedSearche(TypedDict, total=False):
    """Kusto Query Language searches to save."""
    category: Required[str]
    """The category of the saved search. This helps the user to find a saved search faster."""
    displayName: Required[str]
    """Display name for the search."""
    name: Required[str]
    """Name of the saved search."""
    query: Required[str]
    """The query expression for the saved search."""
    etag: str
    """The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag."""
    functionAlias: str
    """The function alias if query serves as a function."""
    functionParameters: str
    """The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to /azure/kusto/query/functions/user-defined-functions."""
    tags: List[object]
    """The tags attached to the saved search."""
    version: int
    """The version number of the query language. The current version is 2 and is the default."""


class StorageInsightsConfig(TypedDict, total=False):
    """List of storage accounts to be read by the workspace."""
    storageAccountResourceId: Required[str]
    """Resource ID of the storage account to be linked."""
    containers: List[object]
    """The names of the blob containers that the workspace should read."""
    tables: List[object]
    """List of tables to be read by the workspace."""


class Table(TypedDict, total=False):
    """LAW custom tables to be deployed."""
    name: Required[str]
    """The name of the table."""
    plan: str
    """The plan for the table."""
    retentionInDays: int
    """The retention in days for the table."""
    totalRetentionInDays: int
    """The total retention in days for the table."""


class RestoredLog(TypedDict, total=False):
    """The restored logs for the table."""
    endRestoreTime: str
    """The timestamp to end the restore by (UTC)."""
    sourceTable: str
    """The table to restore data from."""
    startRestoreTime: str
    """The timestamp to start the restore from (UTC)."""


class RoleAssignment(TypedDict, total=False):
    """The role assignments for the table."""
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


class Schema(TypedDict, total=False):
    """The schema for the table."""
    name: Required[str]
    """The table name."""
    description: str
    """The table description."""
    displayName: str
    """The table display name."""


class Column(TypedDict, total=False):
    """A list of table custom columns."""
    name: Required[str]
    """The column name."""
    type: Required[Literal['boolean', 'dateTime', 'dynamic', 'guid', 'int', 'long', 'real', 'string']]
    """The column type."""
    dataTypeHint: Literal['armPath', 'guid', 'ip', 'uri']
    """The column data type logical hint."""
    description: str
    """The column description."""
    displayName: str
    """Column display name."""


class SearchResult(TypedDict, total=False):
    """The search results for the table."""
    query: Required[str]
    """The search job query."""
    description: str
    """The search description."""
    endSearchTime: str
    """The timestamp to end the search by (UTC)."""
    limit: int
    """Limit the search job to return up to specified number of rows."""
    startSearchTime: str
    """The timestamp to start the search from (UTC)."""


class Workspace(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Log Analytics workspace."""
    dailyQuotaGb: int
    """The workspace daily quota for ingestion."""
    dataRetention: int
    """Number of days data will be retained for."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    forceCmkForQuery: bool
    """Indicates whether customer managed storage is mandatory for query management."""
    location: str
    """Location for all resources."""
    onboardWorkspaceToSentinel: bool
    """Onboard the Log Analytics Workspace to Sentinel. Requires 'SecurityInsights' solution to be in gallerySolutions."""
    publicNetworkAccessForIngestion: Literal['Disabled', 'Enabled']
    """The network access type for accessing Log Analytics ingestion."""
    publicNetworkAccessForQuery: Literal['Disabled', 'Enabled']
    """The network access type for accessing Log Analytics query."""
    skuCapacityReservationLevel: int
    """The capacity reservation level in GB for this workspace, when CapacityReservation sku is selected. Must be in increments of 100 between 100 and 5000."""
    skuName: Literal['CapacityReservation', 'Free', 'LACluster', 'PerGB2018', 'PerNode', 'Premium', 'Standalone', 'Standard']
    """The name of the SKU."""
    tags: Dict[str, object]
    """Tags of the resource."""
    useResourcePermissions: bool
    """Set to 'true' to use resource or workspace permissions and 'false' (or leave empty) to require workspace permissions."""


class WorkspaceOutputs(TypedDict, total=False):
    """Outputs for Workspace"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    logAnalyticsWorkspaceId: Output[Literal['string']]
    """The ID associated with the workspace."""
    name: Output[Literal['string']]
    """The name of the deployed log analytics workspace."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed log analytics workspace."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed log analytics workspace."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class WorkspaceBicep(Module):
    outputs: WorkspaceOutputs


def workspace(
        bicep: IO[str],
        /,
        *,
        params: Workspace,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'operational-insights/workspace',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> WorkspaceBicep:
    symbol = "workspace_" + generate_suffix()
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
    output = WorkspaceBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'logAnalyticsWorkspaceId': Output(symbol, 'logAnalyticsWorkspaceId', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
