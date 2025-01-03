from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ScopeMap(TypedDict, total=False):
    """"""
    actions: Required[List[object]]
    """The list of scoped permissions for registry artifacts."""
    description: str
    """The user friendly description of the scope map."""
    name: str
    """The name of the scope map."""


class ScopeMapOutputs(TypedDict, total=False):
    """Outputs for ScopeMap"""
    name: Output[Literal['string']]
    """The name of the scope map."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the scope map was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the scope map."""


class ScopeMapModule(Module):
    outputs: ScopeMapOutputs

