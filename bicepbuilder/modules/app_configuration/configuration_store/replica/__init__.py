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


class Replica(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the replica."""
    replicaLocation: Required[str]
    """Location of the replica."""


class ReplicaOutputs(TypedDict, total=False):
    """Outputs for Replica"""
    name: Output[Literal['string']]
    """The name of the replica that was deployed."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the app configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replica that was deployed."""


class ReplicaBicep(Module):
    outputs: ReplicaOutputs

