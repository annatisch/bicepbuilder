from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class EncryptionProtector(TypedDict, total=False):
    """"""
    serverKeyName: Required[str]
    """The name of the SQL managed instance key."""
    autoRotationEnabled: bool
    """Key auto rotation opt-in flag."""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The encryption protector type like "ServiceManaged", "AzureKeyVault"."""


class EncryptionProtectorOutputs(TypedDict, total=False):
    """Outputs for EncryptionProtector"""
    name: Output[Literal['string']]
    """The name of the deployed managed instance encryption protector."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed managed instance encryption protector."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed managed instance encryption protector."""


class EncryptionProtectorModule(Module):
    outputs: EncryptionProtectorOutputs

