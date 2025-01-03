from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ReplicationAlertSetting(TypedDict, total=False):
    """"""
    customEmailAddresses: List[object]
    """Comma separated list of custom email address for sending alert emails."""
    locale: str
    """The locale for the email notification."""
    name: str
    """The name of the replication Alert Setting."""
    sendToOwners: Literal['DoNotSend', 'Send']
    """The value indicating whether to send email to subscription administrator."""


class ReplicationAlertSettingOutputs(TypedDict, total=False):
    """Outputs for ReplicationAlertSetting"""
    name: Output[Literal['string']]
    """The name of the replication Alert Setting."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication alert setting was created."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication alert setting."""


class ReplicationAlertSettingModule(Module):
    outputs: ReplicationAlertSettingOutputs

