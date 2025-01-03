from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Monitoring Metrics Publisher', 'Application Insights Component Contributor', 'Application Insights Snapshot Debugger', 'Monitoring Contributor']]]
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


class InsightsComponent(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Application Insights."""
    workspaceResourceId: Required[str]
    """Resource ID of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property."""
    applicationType: Literal['other', 'web']
    """Application type."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableIpMasking: bool
    """Disable IP masking. Default value is set to true."""
    disableLocalAuth: bool
    """Disable Non-AAD based Auth. Default value is set to false."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    forceCustomerStorageForProfiler: bool
    """Force users to create their own storage account for profiler and debugger."""
    kind: str
    """The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone."""
    linkedStorageAccountResourceId: str
    """Linked storage account resource ID."""
    location: str
    """Location for all Resources."""
    publicNetworkAccessForIngestion: Literal['Disabled', 'Enabled']
    """The network access type for accessing Application Insights ingestion. - Enabled or Disabled."""
    publicNetworkAccessForQuery: Literal['Disabled', 'Enabled']
    """The network access type for accessing Application Insights query. - Enabled or Disabled."""
    retentionInDays: Literal[30, 60, 90, 120, 180, 270, 365, 550, 730]
    """Retention period in days."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    samplingPercentage: int
    """Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry."""
    tags: Dict[str, object]
    """Tags of the resource."""


class InsightsComponentOutputs(TypedDict, total=False):
    """Outputs for InsightsComponent"""
    applicationId: Output[Literal['string']]
    """The application ID of the application insights component."""
    connectionString: Output[Literal['string']]
    """Application Insights Connection String."""
    instrumentationKey: Output[Literal['string']]
    """Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the application insights component."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the application insights component was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the application insights component."""


class InsightsComponentModule(Module):
    outputs: InsightsComponentOutputs

