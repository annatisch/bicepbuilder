from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class SenderUsername(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the sender username resource to create."""
    username: Required[str]
    """A sender username to be used when sending emails."""
    displayName: str
    """The display name for the senderUsername."""


class SenderUsernameOutputs(TypedDict, total=False):
    """Outputs for SenderUsername"""
    name: Output[Literal['string']]
    """The name of the sender username."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the sender username was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the sender username."""


class SenderUsernameModule(Module):
    outputs: SenderUsernameOutputs

