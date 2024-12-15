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


class StaticMember(TypedDict, total=False):
    """Static Members to create for the network group. Contains virtual networks to add to the network group."""
    name: Required[str]
    """The name of the static member."""
    resourceId: Required[str]
    """Resource ID of the virtual network."""


class NetworkGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the network group."""
    description: str
    """A description of the network group."""


class NetworkGroupOutputs(TypedDict, total=False):
    """Outputs for NetworkGroup"""
    name: Output[Literal['string']]
    """The name of the deployed network group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the network group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed network group."""


class NetworkGroupBicep(Module):
    outputs: NetworkGroupOutputs

