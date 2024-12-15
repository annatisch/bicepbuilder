from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Notificationchannel(TypedDict, total=False):
    """"""
    events: Required[List[object]]
    """The list of event for which this notification is enabled."""
    name: Required[Literal['autoShutdown', 'costThreshold']]
    """The name of the notification channel."""
    emailRecipient: str
    """The email recipient to send notifications to (can be a list of semi-colon separated email addresses). Required if "webHookUrl" is empty."""
    webHookUrl: str
    """The webhook URL to which the notification will be sent. Required if "emailRecipient" is empty."""
    description: str
    """Description of notification."""
    notificationLocale: str
    """The locale to use when sending a notification (fallback for unsupported languages is EN)."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NotificationchannelOutputs(TypedDict, total=False):
    """Outputs for Notificationchannel"""
    name: Output[Literal['string']]
    """The name of the notification channel."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the notification channel was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the notification channel."""


class NotificationchannelBicep(Module):
    outputs: NotificationchannelOutputs

