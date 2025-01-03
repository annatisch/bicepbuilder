from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
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


class ReplicaModule(Module):
    outputs: ReplicaOutputs

