from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)

if TYPE_CHECKING:
    from .authorization_rule import AuthorizationRule


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Service Bus Data Owner', 'Azure Service Bus Data Receiver', 'Azure Service Bus Data Sender', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Queue(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Service Bus Queue."""
    authorizationRules: List['AuthorizationRule']
    """Authorization Rules for the Service Bus Queue."""
    autoDeleteOnIdle: str
    """ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes (PT5M)."""
    deadLetteringOnMessageExpiration: bool
    """A value that indicates whether this queue has dead letter support when a message expires."""
    defaultMessageTimeToLive: str
    """ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """Value that indicates whether server-side batched operations are enabled."""
    enableExpress: bool
    """A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage. This property is only used if the """
    enablePartitioning: bool
    """A value that indicates whether the queue is to be partitioned across multiple message brokers."""
    forwardDeadLetteredMessagesTo: str
    """Queue/Topic name to forward the Dead Letter message."""
    forwardTo: str
    """Queue/Topic name to forward the messages."""
    lock: 'Lock'
    """The lock settings of the service."""
    lockDuration: str
    """ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute."""
    maxDeliveryCount: int
    """The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10."""
    maxMessageSizeInKilobytes: int
    """Maximum size (in KB) of the message payload that can be accepted by the queue. This property is only used in Premium today and default is 1024."""
    maxSizeInMegabytes: int
    """The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024."""
    requiresDuplicateDetection: bool
    """A value indicating if this queue requires duplicate detection."""
    requiresSession: bool
    """A value that indicates whether the queue supports the concept of sessions."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""


class QueueOutputs(TypedDict, total=False):
    """Outputs for Queue"""
    name: Output[Literal['string']]
    """The name of the deployed queue."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed queue."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed queue."""


class QueueBicep(Module):
    outputs: QueueOutputs

