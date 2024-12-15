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


class FrontendBicep(Module):
    outputs: FrontendOutputs

