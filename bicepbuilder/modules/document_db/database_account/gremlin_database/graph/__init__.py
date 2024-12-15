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


class Graph(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the graph."""
    indexingPolicy: Dict[str, object]
    """Indexing policy of the graph."""
    partitionKeyPaths: List[object]
    """List of paths using which data within the container can be partitioned."""
    tags: Dict[str, object]
    """Tags of the Gremlin graph resource."""


class GraphOutputs(TypedDict, total=False):
    """Outputs for Graph"""
    name: Output[Literal['string']]
    """The name of the graph."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the graph was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the graph."""


class GraphBicep(Module):
    outputs: GraphOutputs

