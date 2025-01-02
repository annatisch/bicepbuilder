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


class IntegrationServiceEnvironment(TypedDict, total=False):
    """The integration service environment settings."""
    id: str
    """The integration service environment Id."""


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
    """The resource ID(s) to assign to the resource."""


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


class LogicWorkflow(TypedDict, total=False):
    """"""
    name: Required[str]
    """The logic app workflow name."""
    actionsAccessControlConfiguration: Dict[str, object]
    """The access control configuration for workflow actions."""
    connectorEndpointsConfiguration: Dict[str, object]
    """The endpoints configuration:  Access endpoint and outgoing IP addresses for the connector."""
    contentsAccessControlConfiguration: Dict[str, object]
    """The access control configuration for accessing workflow run contents."""
    definitionParameters: Dict[str, object]
    """Parameters for the definition template."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    integrationAccount: Dict[str, object]
    """The integration account."""
    integrationServiceEnvironment: 'IntegrationServiceEnvironment'
    """The integration service environment settings."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. Only one type of identity is supported: system-assigned or user-assigned, but not both."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Logic App Contributor', 'Logic App Operator', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    state: Literal['Completed', 'Deleted', 'Disabled', 'Enabled', 'NotSpecified', 'Suspended']
    """The state. - NotSpecified, Completed, Enabled, Disabled, Deleted, Suspended."""
    tags: Dict[str, object]
    """Tags of the resource."""
    triggersAccessControlConfiguration: Dict[str, object]
    """The access control configuration for invoking workflow triggers."""
    workflowActions: Dict[str, object]
    """The definitions for one or more actions to execute at workflow runtime."""
    workflowEndpointsConfiguration: Dict[str, object]
    """The endpoints configuration:  Access endpoint and outgoing IP addresses for the workflow."""
    workflowManagementAccessControlConfiguration: Dict[str, object]
    """The access control configuration for workflow management."""
    workflowOutputs: Dict[str, object]
    """The definitions for the outputs to return from a workflow run."""
    workflowParameters: Dict[str, object]
    """The definitions for one or more parameters that pass the values to use at your logic app's runtime."""
    workflowStaticResults: Dict[str, object]
    """The definitions for one or more static results returned by actions as mock outputs when static results are enabled on those actions. In each action definition, the runtimeConfiguration.staticResult.name attribute references the corresponding definition inside staticResults."""
    workflowTriggers: Dict[str, object]
    """The definitions for one or more triggers that instantiate your workflow. You can define more than one trigger, but only with the Workflow Definition Language, not visually through the Logic Apps Designer."""


class LogicWorkflowOutputs(TypedDict, total=False):
    """Outputs for LogicWorkflow"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the logic app."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the logic app was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the logic app."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class LogicWorkflowBicep(Module):
    outputs: LogicWorkflowOutputs


def logic_workflow(
        bicep: IO[str],
        params: LogicWorkflow,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> LogicWorkflowBicep:
    symbol = "logic_workflow_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/logic/workflow:{tag}' = {{\n")
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
    output = LogicWorkflowBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
