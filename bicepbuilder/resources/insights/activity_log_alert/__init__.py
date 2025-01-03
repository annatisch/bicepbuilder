from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
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

