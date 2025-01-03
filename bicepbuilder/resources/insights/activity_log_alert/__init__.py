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


class InsightsActivityLogAlert(TypedDict, total=False):
    """"""
    conditions: Required[List[object]]
    """An Array of objects containing conditions that will cause this alert to activate. Conditions can also be combined with logical operators """
    name: Required[str]
    """The name of the alert."""
    actions: List[object]
    """The list of actions to take when alert triggers."""
    alertDescription: str
    """Description of the alert."""
    enabled: bool
    """Indicates whether this alert is enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    scopes: List[object]
    """The list of resource IDs that this Activity Log Alert is scoped to."""
    tags: Dict[str, object]
    """Tags of the resource."""


class InsightsActivityLogAlertOutputs(TypedDict, total=False):
    """Outputs for InsightsActivityLogAlert"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the activity log alert."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the activity log alert was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the activity log alert."""


class InsightsActivityLogAlertModule(Module):
    outputs: InsightsActivityLogAlertOutputs


def _insights_activity_log_alert(
        bicep: IO[str],
        params: InsightsActivityLogAlert,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> InsightsActivityLogAlertModule:
    symbol = "insights_activity_log_alert_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/activity-log-alert:{tag}' = {{\n")
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
    output = InsightsActivityLogAlertModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
