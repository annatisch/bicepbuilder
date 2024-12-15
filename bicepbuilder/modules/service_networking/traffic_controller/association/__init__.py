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


class Association(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the association to create."""
    subnetResourceId: Required[str]
    """The resource ID of the subnet to associate with the traffic controller."""
    location: str
    """Location for all Resources."""


class AssociationOutputs(TypedDict, total=False):
    """Outputs for Association"""
    name: Output[Literal['string']]
    """The name of the association."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the resource was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the association."""
    subnetResourceId: Output[Literal['string']]
    """The resource ID of the associated subnet."""


class AssociationBicep(Module):
    outputs: AssociationOutputs

