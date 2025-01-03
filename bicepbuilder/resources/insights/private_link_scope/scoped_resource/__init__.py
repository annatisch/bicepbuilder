from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ScopedResource(TypedDict, total=False):
    """"""
    linkedResourceId: Required[str]
    """The resource ID of the scoped Azure monitor resource."""
    name: Required[str]
    """Name of the private link scoped resource."""


class ScopedResourceOutputs(TypedDict, total=False):
    """Outputs for ScopedResource"""
    name: Output[Literal['string']]
    """The full name of the deployed Scoped Resource."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group where the resource has been deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed scopedResource."""


class ScopedResourceModule(Module):
    outputs: ScopedResourceOutputs

