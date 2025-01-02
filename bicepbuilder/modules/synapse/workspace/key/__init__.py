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
    isActiveCMK: Required[bool]
    """Used to activate the workspace after a customer managed key is provided."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    name: Required[str]
    """The name of the Synapse Workspaces Key."""


class KeyOutputs(TypedDict, total=False):
    """Outputs for Key"""
    name: Output[Literal['string']]
    """The name of the deployed key."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed key."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed key."""


class KeyBicep(Module):
    outputs: KeyOutputs

