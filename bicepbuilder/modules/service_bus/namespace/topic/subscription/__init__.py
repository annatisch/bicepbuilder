from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Subscription(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the service bus namespace topic subscription."""
    autoDeleteOnIdle: str
    """ISO 8601 timespan idle interval after which the subscription is automatically deleted. The minimum duration is 5 minutes."""
    clientAffineProperties: Dict[str, object]
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
    """Enumerates the possible values for the status of a messaging entity."""


class SubscriptionOutputs(TypedDict, total=False):
    """Outputs for Subscription"""
    name: Output[Literal['string']]
    """The name of the topic subscription."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the topic subscription was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the topic subscription."""


class SubscriptionBicep(Module):
    outputs: SubscriptionOutputs

