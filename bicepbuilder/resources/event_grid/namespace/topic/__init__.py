from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .event_subscription import EventSubscription


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Resource Notifications System Topics Subscriber', 'Contributor', 'EventGrid Contributor', 'EventGrid Data Contributor', 'EventGrid Data Receiver', 'EventGrid Data Sender', 'EventGrid EventSubscription Contributor', 'EventGrid EventSubscription Reader', 'EventGrid TopicSpaces Publisher', 'EventGrid TopicSpaces Subscriber', 'Owner', 'Reader', 'User Access Administrator']]]
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


class Topic(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the topic."""
    eventRetentionInDays: int
    """Event retention for the namespace topic expressed in days."""
    eventSubscriptions: List['EventSubscription']
    """All event subscriptions to create."""
    inputSchema: str
    """This determines the format that is expected for incoming events published to the topic."""
    lock: 'Lock'
    """The lock settings of the service."""
    publisherType: str
    """Publisher type of the namespace topic."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""


class TopicOutputs(TypedDict, total=False):
    """Outputs for Topic"""
    name: Output[Literal['string']]
    """The name of the Namespace Topic."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Namespace Topic was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Namespace Topic."""


class TopicModule(Module):
    outputs: TopicOutputs

