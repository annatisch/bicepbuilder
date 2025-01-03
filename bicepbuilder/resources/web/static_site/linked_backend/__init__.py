from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LinkedBackend(TypedDict, total=False):
    """"""
    backendResourceId: Required[str]
    """The resource ID of the backend linked to the static site."""
    name: str
    """Name of the backend to link to the static site."""
    region: str
    """The region of the backend linked to the static site."""


class LinkedBackendOutputs(TypedDict, total=False):
    """Outputs for LinkedBackend"""
    name: Output[Literal['string']]
    """The name of the static site linked backend."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the static site linked backend was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the static site linked backend."""


class LinkedBackendModule(Module):
    outputs: LinkedBackendOutputs

