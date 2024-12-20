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


class ReplicationAlertSettingBicep(Module):
    outputs: ReplicationAlertSettingOutputs

