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
    from .collection import Collection


class MongodbDatabase(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the mongodb database."""
    collections: List['Collection']
    """Collections in the mongodb database."""
    tags: Dict[str, object]
    """Tags of the resource."""
    throughput: int
    """Request Units per second."""


class MongodbDatabaseOutputs(TypedDict, total=False):
    """Outputs for MongodbDatabase"""
    name: Output[Literal['string']]
    """The name of the mongodb database."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the mongodb database was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the mongodb database."""


class MongodbDatabaseBicep(Module):
    outputs: MongodbDatabaseOutputs

