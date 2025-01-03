from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ApplicationType(TypedDict, total=False):
    """"""
    name: str
    """Application type name."""
    tags: Dict[str, object]
    """Tags of the resource."""


class ApplicationTypeOutputs(TypedDict, total=False):
    """Outputs for ApplicationType"""
    name: Output[Literal['string']]
    """The resource name of the Application type."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the Application type."""
    resourceID: Output[Literal['string']]
    """The resource ID of the Application type."""


class ApplicationTypeModule(Module):
    outputs: ApplicationTypeOutputs

