from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Web Plan Contributor', 'Website Contributor']]]
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


class WebServerfarm(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the app service plan."""
    reserved: bool
    """Defaults to false when creating Windows/app App Service Plan. Required if creating a Linux App Service Plan and must be set to true."""
    appServiceEnvironmentId: str
    """The Resource ID of the App Service Environment to use for the App Service Plan."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    elasticScaleEnabled: bool
    """Enable/Disable ElasticScaleEnabled App Service Plan."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    kind: Literal['App', 'Elastic', 'FunctionApp', 'Linux', 'Windows']
    """Kind of server OS."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maximumElasticWorkerCount: int
    """Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan."""
    perSiteScaling: bool
    """If true, apps assigned to this App Service plan can be scaled independently. If false, apps assigned to this App Service plan will scale to all instances of the plan."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    skuCapacity: int
    """Number of workers associated with the App Service Plan. This defaults to 3, to leverage availability zones."""
    skuName: str
    """The name of the SKU will Determine the tier, size, family of the App Service Plan. This defaults to P1v3 to leverage availability zones."""
    tags: Dict[str, object]
    """Tags of the resource."""
    targetWorkerCount: int
    """Scaling worker count."""
    targetWorkerSize: Literal[0, 1, 2]
    """The instance size of the hosting plan (small, medium, or large)."""
    workerTierName: str
    """Target worker tier assigned to the App Service plan."""
    zoneRedundant: bool
    """Zone Redundant server farms can only be used on Premium or ElasticPremium SKU tiers within ZRS Supported regions (https://learn.microsoft.com/en-us/azure/storage/common/redundancy-regions-zrs)."""


class WebServerfarmOutputs(TypedDict, total=False):
    """Outputs for WebServerfarm"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the app service plan."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the app service plan was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the app service plan."""


class WebServerfarmModule(Module):
    outputs: WebServerfarmOutputs

