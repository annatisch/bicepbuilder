from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
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
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: Required[str]
    """Name of a Diagnostic Metric category for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class InsightsDiagnosticSetting(TypedDict, total=False):
    """"""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category."""
    location: str
    """Location deployment metadata."""
    logAnalyticsDestinationType: Literal['', 'AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    metricCategories: List['MetricCategory']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    name: str
    """Name of the Diagnostic settings."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace."""


class InsightsDiagnosticSettingOutputs(TypedDict, total=False):
    """Outputs for InsightsDiagnosticSetting"""
    name: Output[Literal['string']]
    """The name of the diagnostic settings."""
    resourceId: Output[Literal['string']]
    """The resource ID of the diagnostic settings."""
    subscriptionName: Output[Literal['string']]
    """The name of the subscription to deploy into."""


class InsightsDiagnosticSettingModule(Module):
    outputs: InsightsDiagnosticSettingOutputs


def _insights_diagnostic_setting(
        bicep: IO[str],
        params: InsightsDiagnosticSetting,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> InsightsDiagnosticSettingModule:
    symbol = "insights_diagnostic_setting_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/diagnostic-setting:{tag}' = {{\n")
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
    output = InsightsDiagnosticSettingModule(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'subscriptionName': Output(symbol, 'subscriptionName', 'string'),
        }

    return output
