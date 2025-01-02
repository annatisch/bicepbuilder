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


class SavedSearch(TypedDict, total=False):
    """"""
    category: Required[str]
    """Query category."""
    displayName: Required[str]
    """Display name for the search."""
    name: Required[str]
    """Name of the saved search."""
    query: Required[str]
    """Kusto Query to be stored."""
    etag: str
    """The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag."""
    functionAlias: str
    """The function alias if query serves as a function."""
    functionParameters: str
    """The optional function parameters if query serves as a function. Value should be in the following format: "param-name1:type1 = default_value1, param-name2:type2 = default_value2". For more examples and proper syntax please refer to /azure/kusto/query/functions/user-defined-functions."""
    tags: List[object]
    """Tags to configure in the resource."""
    version: int
    """The version number of the query language."""


class SavedSearchOutputs(TypedDict, total=False):
    """Outputs for SavedSearch"""
    name: Output[Literal['string']]
    """The name of the deployed saved search."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the saved search is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed saved search."""


class SavedSearchBicep(Module):
    outputs: SavedSearchOutputs

