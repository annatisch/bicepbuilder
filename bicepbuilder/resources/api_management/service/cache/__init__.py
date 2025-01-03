from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Cache(TypedDict, total=False):
    """"""
    connectionString: Required[str]
    """Runtime connection string to cache. Can be referenced by a named value like so, {{"""
    name: Required[str]
    """Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier)."""
    useFromLocation: Required[str]
    """Location identifier to use cache from (should be either 'default' or valid Azure region identifier)."""
    description: str
    """Cache description."""
    resourceId: str
    """Original uri of entity in external system cache points to."""


class CacheOutputs(TypedDict, total=False):
    """Outputs for Cache"""
    name: Output[Literal['string']]
    """The name of the API management service cache."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service cache was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service cache."""


class CacheModule(Module):
    outputs: CacheOutputs

