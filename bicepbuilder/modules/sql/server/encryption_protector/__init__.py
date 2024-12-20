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


class EncryptionProtector(TypedDict, total=False):
    """"""
    serverKeyName: Required[str]
    """The name of the server key."""
    autoRotationEnabled: bool
    """Key auto rotation opt-in flag."""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The encryption protector type."""


class EncryptionProtectorOutputs(TypedDict, total=False):
    """Outputs for EncryptionProtector"""
    name: Output[Literal['string']]
    """The name of the deployed encryption protector."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed encryption protector."""
    resourceId: Output[Literal['string']]
    """The resource ID of the encryption protector."""


class EncryptionProtectorBicep(Module):
    outputs: EncryptionProtectorOutputs

