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


class Table(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the table."""
    maxThroughput: int
    """Represents maximum throughput, the resource can scale up to. Cannot be set together with """
    tags: Dict[str, object]
    """Tags for the table."""
    throughput: int
    """Request Units per second (for example 10000). Cannot be set together with """


class TableOutputs(TypedDict, total=False):
    """Outputs for Table"""
    name: Output[Literal['string']]
    """The name of the table."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the table was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the table."""


class TableBicep(Module):
    outputs: TableOutputs

