from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Frontend(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the frontend to create."""
    location: str
    """Location for all Resources."""


class FrontendOutputs(TypedDict, total=False):
    """Outputs for Frontend"""
    fqdn: Output[Literal['string']]
    """The FQDN of the frontend."""
    name: Output[Literal['string']]
    """The name of the frontend."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the resource was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the frontend."""


class FrontendModule(Module):
    outputs: FrontendOutputs

