from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Collection(TypedDict, total=False):
    """"""
    indexes: Required[List[object]]
    """Indexes for the collection."""
    name: Required[str]
    """Name of the collection."""
    shardKey: Required[Dict[str, object]]
    """ShardKey for the collection."""
    throughput: int
    """Request Units per second."""


class CollectionOutputs(TypedDict, total=False):
    """Outputs for Collection"""
    name: Output[Literal['string']]
    """The name of the mongodb database collection."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the mongodb database collection was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the mongodb database collection."""


class CollectionBicep(Module):
    outputs: CollectionOutputs

