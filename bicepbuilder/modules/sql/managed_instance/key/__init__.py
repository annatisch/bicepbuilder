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


class Key(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the key. Must follow the ["""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The encryption protector type like "ServiceManaged", "AzureKeyVault"."""
    uri: str
    """The URI of the key. If the ServerKeyType is AzureKeyVault, then either the URI or the keyVaultName/keyName combination is required."""


class KeyOutputs(TypedDict, total=False):
    """Outputs for Key"""
    name: Output[Literal['string']]
    """The name of the deployed managed instance key."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed managed instance key."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed managed instance key."""


class KeyBicep(Module):
    outputs: KeyOutputs

