from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Key(TypedDict, total=False):
    """"""
    name: str
    """The name of the key. Must follow the ["""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The server key type."""
    uri: str
    """The URI of the server key. If the ServerKeyType is AzureKeyVault, then the URI is required. The AKV URI is required to be in this format: 'https://YourVaultName.azure.net/keys/YourKeyName/YourKeyVersion'."""


class KeyOutputs(TypedDict, total=False):
    """Outputs for Key"""
    name: Output[Literal['string']]
    """The name of the deployed server key."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed server key."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed server key."""


class KeyModule(Module):
    outputs: KeyOutputs

