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
    roleDefinitionIdOrName: Required[Union[str, Literal['Owner', 'Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Application Group Contributor', 'Desktop Virtualization Application Group Contributor', 'Desktop Virtualization Application Group Reader', 'Desktop Virtualization Contributor', 'Desktop Virtualization Host Pool Contributor', 'Desktop Virtualization Host Pool Reader', 'Desktop Virtualization Power On Off Contributor', 'Desktop Virtualization Reader', 'Desktop Virtualization Session Host Operator', 'Desktop Virtualization User', 'Desktop Virtualization User Session Operator', 'Desktop Virtualization Virtual Machine Contributor', 'Desktop Virtualization Workspace Contributor', 'Desktop Virtualization Workspace Reader']]]
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


class DesktopVirtualizationScalingPlan(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Scaling Plan."""
    description: str
    """Description of the Scaling Plan."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    exclusionTag: str
    """Exclusion tag to be used for exclusion of VMs from Scaling Plan."""
    friendlyName: str
    """Friendly name of the Scaling Plan."""
    hostPoolReferences: List[object]
    """Host pool references of the Scaling Plan."""
    hostPoolType: Literal['Personal', 'Pooled']
    """Host pool type of the Scaling Plan."""
    location: str
    """Location of the Scaling Plan. Defaults to resource group location."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    schedules: List[object]
    """Schedules of the Scaling Plan."""
    tags: Dict[str, object]
    """Tags of the resource."""
    timeZone: str
    """Time zone of the Scaling Plan. Defaults to UTC."""


class DesktopVirtualizationScalingPlanOutputs(TypedDict, total=False):
    """Outputs for DesktopVirtualizationScalingPlan"""
    location: Output[Literal['string']]
    """The location of the Scaling Plan."""
    name: Output[Literal['string']]
    """The name of the Scaling Plan."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Scaling Plan was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Scaling Plan."""


class DesktopVirtualizationScalingPlanBicep(Module):
    outputs: DesktopVirtualizationScalingPlanOutputs


def desktop_virtualization_scaling_plan(
        bicep: IO[str],
        params: DesktopVirtualizationScalingPlan,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> DesktopVirtualizationScalingPlanBicep:
    symbol = "desktop_virtualization_scaling_plan_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/desktop-virtualization/scaling-plan:{tag}' = {{\n")
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
    output = DesktopVirtualizationScalingPlanBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
