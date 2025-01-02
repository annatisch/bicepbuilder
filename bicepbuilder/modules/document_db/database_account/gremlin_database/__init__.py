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

if TYPE_CHECKING:
    from .graph import Graph


class GremlinDatabase(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Gremlin database."""
    graphs: List['Graph']
    """Array of graphs to deploy in the Gremlin database."""
    maxThroughput: int
    """Represents maximum throughput, the resource can scale up to. Cannot be set together with """
    tags: Dict[str, object]
    """Tags of the Gremlin database resource."""
    throughput: int
    """Request Units per second (for example 10000). Cannot be set together with """


class GremlinDatabaseOutputs(TypedDict, total=False):
    """Outputs for GremlinDatabase"""
    name: Output[Literal['string']]
    """The name of the Gremlin database."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Gremlin database was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Gremlin database."""


class GremlinDatabaseBicep(Module):
    outputs: GremlinDatabaseOutputs

