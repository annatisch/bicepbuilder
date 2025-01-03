from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Api(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the product API."""


class ApiOutputs(TypedDict, total=False):
    """Outputs for Api"""
    name: Output[Literal['string']]
    """The name of the product API."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the product API was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the product API."""


class ApiModule(Module):
    outputs: ApiOutputs

