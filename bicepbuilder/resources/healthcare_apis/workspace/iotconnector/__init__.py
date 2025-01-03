from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .fhirdestination import Fhirdestination


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


class Iotconnector(TypedDict, total=False):
    """"""
    eventHubName: Required[str]
    """Event Hub name to connect to."""
    eventHubNamespaceName: Required[str]
    """Namespace of the Event Hub to connect to."""
    name: Required[str]
    """The name of the MedTech service."""
    consumerGroup: str
    """Consumer group of the event hub to connected to."""
    deviceMapping: Dict[str, object]
    """The mapping JSON that determines how incoming device data is normalized."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    fhirdestination: 'Fhirdestination'
    """FHIR Destination."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    tags: Dict[str, object]
    """Tags of the resource."""


class IotconnectorOutputs(TypedDict, total=False):
    """Outputs for Iotconnector"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the medtech service."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the namespace is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the medtech service."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    workspaceName: Output[Literal['string']]
    """The name of the medtech workspace."""


class IotconnectorModule(Module):
    outputs: IotconnectorOutputs

