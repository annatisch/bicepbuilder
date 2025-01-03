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


class InsightsActionGroup(TypedDict, total=False):
    """"""
    groupShortName: Required[str]
    """The short name of the action group."""
    name: Required[str]
    """The name of the action group."""
    armRoleReceivers: List[object]
    """The list of ARM role receivers that are part of this action group. Roles are Azure RBAC roles and only built-in roles are supported."""
    automationRunbookReceivers: List[object]
    """The list of AutomationRunbook receivers that are part of this action group."""
    azureAppPushReceivers: List[object]
    """The list of AzureAppPush receivers that are part of this action group."""
    azureFunctionReceivers: List[object]
    """The list of function receivers that are part of this action group."""
    emailReceivers: List[object]
    """The list of email receivers that are part of this action group."""
    enabled: bool
    """Indicates whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    itsmReceivers: List[object]
    """The list of ITSM receivers that are part of this action group."""
    location: str
    """Location for all resources."""
    logicAppReceivers: List[object]
    """The list of logic app receivers that are part of this action group."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    smsReceivers: List[object]
    """The list of SMS receivers that are part of this action group."""
    tags: Dict[str, object]
    """Tags of the resource."""
    voiceReceivers: List[object]
    """The list of voice receivers that are part of this action group."""
    webhookReceivers: List[object]
    """The list of webhook receivers that are part of this action group."""


class InsightsActionGroupOutputs(TypedDict, total=False):
    """Outputs for InsightsActionGroup"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the action group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the action group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the action group."""


class InsightsActionGroupModule(Module):
    outputs: InsightsActionGroupOutputs

