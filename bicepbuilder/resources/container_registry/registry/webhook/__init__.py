from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Webhook(TypedDict, total=False):
    """"""
    serviceUri: Required[str]
    """The service URI for the webhook to post notifications."""
    action: List[object]
    """The list of actions that trigger the webhook to post notifications."""
    customHeaders: Dict[str, object]
    """Custom headers that will be added to the webhook notifications."""
    location: str
    """Location for all resources."""
    name: str
    """The name of the registry webhook."""
    scope: str
    """The scope of repositories where the event can be triggered. For example, 'foo:*' means events for all tags under repository 'foo'. 'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to 'foo:latest'. Empty means all events."""
    status: Literal['disabled', 'enabled']
    """The status of the webhook at the time the operation was called."""
    tags: Dict[str, object]
    """Tags of the resource."""


class WebhookOutputs(TypedDict, total=False):
    """Outputs for Webhook"""
    actions: Output[Literal['array']]
    """The actions of the webhook."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the webhook."""
    provistioningState: Output[Literal['string']]
    """The provisioning state of the webhook."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Azure container registry."""
    resourceId: Output[Literal['string']]
    """The resource ID of the webhook."""
    status: Output[Literal['string']]
    """The status of the webhook."""


class WebhookModule(Module):
    outputs: WebhookOutputs

