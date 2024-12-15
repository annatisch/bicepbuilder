from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class ApiBicep(Module):
    outputs: ApiOutputs

