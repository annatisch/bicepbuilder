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


class ClientAffineProperty(TypedDict, total=False):
    """The properties that are associated with a subscription that is client-affine."""
    clientId: Required[str]
    """Indicates the Client ID of the application that created the client-affine subscription."""
    isDurable: bool
    """For client-affine subscriptions, this value indicates whether the subscription is durable or not."""
    isShared: bool
    """For client-affine subscriptions, this value indicates whether the subscription is shared or not."""


class Subscription(TypedDict, total=False):
    """The subscriptions of the topic."""
    name: Required[str]
    """The name of the service bus namespace topic subscription."""
    autoDeleteOnIdle: str
    """ISO 8601 timespan idle interval after which the syubscription is automatically deleted. The minimum duration is 5 minutes."""
    clientAffineProperties: 'ClientAffineProperty'
    """The properties that are associated with a subscription that is client-affine."""
    deadLetteringOnFilterEvaluationExceptions: bool
    """A value that indicates whether a subscription has dead letter support when a message expires."""
    deadLetteringOnMessageExpiration: bool
    """A value that indicates whether a subscription has dead letter support when a message expires."""
    defaultMessageTimeToLive: str
    """ISO 8601 timespan idle interval after which the message expires. The minimum duration is 5 minutes."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timespan that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """A value that indicates whether server-side batched operations are enabled."""
    forwardDeadLetteredMessagesTo: str
    """The name of the recipient entity to which all the messages sent to the subscription are forwarded to."""
    forwardTo: str
    """The name of the recipient entity to which all the messages sent to the subscription are forwarded to."""
    isClientAffine: bool
    """A value that indicates whether the subscription supports the concept of session."""
    lockDuration: str
    """ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute."""
    maxDeliveryCount: int
    """Number of maximum deliveries. A message is automatically deadlettered after this number of deliveries. Default value is 10."""
    requiresSession: bool
    """A value that indicates whether the subscription supports the concept of session."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""


class Topic(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Service Bus Topic."""
    authorizationRules: List['AuthorizationRule']
    """Authorization Rules for the Service Bus Topic."""
    autoDeleteOnIdle: str
    """ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes."""
    defaultMessageTimeToLive: str
    """ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """Value that indicates whether server-side batched operations are enabled."""
    enableExpress: bool
    """A value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage. This property is only used if the """
    enablePartitioning: bool
    """A value that indicates whether the topic is to be partitioned across multiple message brokers."""
    lock: 'Lock'
    """The lock settings of the service."""
    maxMessageSizeInKilobytes: int
    """Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024. This property is only used if the """
    maxSizeInMegabytes: int
    """The maximum size of the topic in megabytes, which is the size of memory allocated for the topic. Default is 1024."""
    requiresDuplicateDetection: bool
    """A value indicating if this topic requires duplicate detection."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""
    subscriptions: List['Subscription']
    """The subscriptions of the topic."""
    supportOrdering: bool
    """Value that indicates whether the topic supports ordering."""


class TopicOutputs(TypedDict, total=False):
    """Outputs for Topic"""
    name: Output[Literal['string']]
    """The name of the deployed topic."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed topic."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed topic."""


class TopicBicep(Module):
    outputs: TopicOutputs

