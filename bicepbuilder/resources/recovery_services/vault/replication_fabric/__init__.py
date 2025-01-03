from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ReplicationFabric(TypedDict, total=False):
    """"""
    location: str
    """The recovery location the fabric represents."""
    name: str
    """The name of the fabric."""
    replicationContainers: List[object]
    """Replication containers to create."""


class ReplicationFabricOutputs(TypedDict, total=False):
    """Outputs for ReplicationFabric"""
    name: Output[Literal['string']]
    """The name of the replication fabric."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication fabric was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication fabric."""


class ReplicationFabricModule(Module):
    outputs: ReplicationFabricOutputs

