from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class EventSubscription(TypedDict, total=False):
    """"""
    destination: Required[Dict[str, object]]
    """The destination for the event subscription. (See https://learn.microsoft.com/en-us/azure/templates/microsoft.eventgrid/eventsubscriptions?pivots=deployment-language-bicep#eventsubscriptiondestination-objects for more information)."""
    name: Required[str]
    """The name of the Event Subscription."""
    topicName: Required[str]
    """Name of the Event Grid Topic."""
    deadLetterDestination: Dict[str, object]
    """Dead Letter Destination. (See https://learn.microsoft.com/en-us/azure/templates/microsoft.eventgrid/eventsubscriptions?pivots=deployment-language-bicep#deadletterdestination-objects for more information)."""
    deadLetterWithResourceIdentity: Dict[str, object]
    """Dead Letter with Resource Identity Configuration. (See https://learn.microsoft.com/en-us/azure/templates/microsoft.eventgrid/eventsubscriptions?pivots=deployment-language-bicep#deadletterwithresourceidentity-objects for more information)."""
    deliveryWithResourceIdentity: Dict[str, object]
    """Delivery with Resource Identity Configuration. (See https://learn.microsoft.com/en-us/azure/templates/microsoft.eventgrid/eventsubscriptions?pivots=deployment-language-bicep#deliverywithresourceidentity-objects for more information)."""
    eventDeliverySchema: Literal['CloudEventSchemaV1_0', 'CustomInputSchema', 'EventGridEvent', 'EventGridSchema']
    """The event delivery schema for the event subscription."""
    expirationTimeUtc: str
    """The expiration time for the event subscription. Format is ISO-8601 (yyyy-MM-ddTHH:mm:ssZ)."""
    filter: Dict[str, object]
    """The filter for the event subscription. (See https://learn.microsoft.com/en-us/azure/templates/microsoft.eventgrid/eventsubscriptions?pivots=deployment-language-bicep#eventsubscriptionfilter for more information)."""
    labels: List[object]
    """The list of user defined labels."""
    retryPolicy: Dict[str, object]
    """The retry policy for events. This can be used to configure the TTL and maximum number of delivery attempts and time to live for events."""


class EventSubscriptionOutputs(TypedDict, total=False):
    """Outputs for EventSubscription"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the event subscription."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the event subscription was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the event subscription."""


class EventSubscriptionModule(Module):
    outputs: EventSubscriptionOutputs

