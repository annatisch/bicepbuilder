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


class ApiVersionSet(TypedDict, total=False):
    """"""
    name: str
    """API Version set name."""
    properties: Dict[str, object]
    """API Version set properties."""


class ApiVersionSetOutputs(TypedDict, total=False):
    """Outputs for ApiVersionSet"""
    name: Output[Literal['string']]
    """The name of the API Version set."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API Version set was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API Version set."""


class ApiVersionSetBicep(Module):
    outputs: ApiVersionSetOutputs

