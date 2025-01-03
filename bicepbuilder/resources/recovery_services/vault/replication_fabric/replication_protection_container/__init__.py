from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class ReplicationProtectionContainer(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the replication container."""
    replicationContainerMappings: List[object]
    """Replication containers mappings to create."""


class ReplicationProtectionContainerOutputs(TypedDict, total=False):
    """Outputs for ReplicationProtectionContainer"""
    name: Output[Literal['string']]
    """The name of the replication container."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication container was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication container."""


class ReplicationProtectionContainerModule(Module):
    outputs: ReplicationProtectionContainerOutputs

