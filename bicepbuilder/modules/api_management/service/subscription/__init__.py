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


class Subscription(TypedDict, total=False):
    """"""
    displayName: Required[str]
    """API Management Service Subscriptions name. Must be 1 to 100 characters long."""
    name: Required[str]
    """Subscription name."""
    allowTracing: bool
    """Determines whether tracing can be enabled."""
    ownerId: str
    """User (user ID path) for whom subscription is being created in form /users/{userId}."""
    primaryKey: str
    """Primary subscription key. If not specified during request key will be generated automatically."""
    scope: str
    """Scope type to choose between a product, "allAPIs" or a specific API. Scope like "/products/{productId}" or "/apis" or "/apis/{apiId}"."""
    secondaryKey: str
    """Secondary subscription key. If not specified during request key will be generated automatically."""
    state: str
    """Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are """"


class SubscriptionOutputs(TypedDict, total=False):
    """Outputs for Subscription"""
    name: Output[Literal['string']]
    """The name of the API management service subscription."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service subscription was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service subscription."""


class SubscriptionBicep(Module):
    outputs: SubscriptionOutputs

