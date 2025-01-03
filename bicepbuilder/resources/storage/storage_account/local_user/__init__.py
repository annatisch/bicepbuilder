from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LocalUser(TypedDict, total=False):
    """"""
    hasSshKey: Required[bool]
    """Indicates whether SSH key exists. Set it to false to remove existing SSH key."""
    hasSshPassword: Required[bool]
    """Indicates whether SSH password exists. Set it to false to remove existing SSH password."""
    name: Required[str]
    """The name of the local user used for SFTP Authentication."""
    permissionScopes: Required[List[object]]
    """The permission scopes of the local user."""
    hasSharedKey: bool
    """Indicates whether shared key exists. Set it to false to remove existing shared key."""
    homeDirectory: str
    """The local user home directory."""
    sshAuthorizedKeys: Dict[str, object]
    """The local user SSH authorized keys for SFTP."""


class LocalUserOutputs(TypedDict, total=False):
    """Outputs for LocalUser"""
    name: Output[Literal['string']]
    """The name of the deployed local user."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed local user."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed local user."""


class LocalUserModule(Module):
    outputs: LocalUserOutputs

