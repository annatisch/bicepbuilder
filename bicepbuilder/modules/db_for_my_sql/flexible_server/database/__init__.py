from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Database(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the database."""
    charset: str
    """The charset of the database."""
    collation: str
    """The collation of the database."""


class DatabaseOutputs(TypedDict, total=False):
    """Outputs for Database"""
    name: Output[Literal['string']]
    """The name of the deployed database."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed database."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed database."""


class DatabaseBicep(Module):
    outputs: DatabaseOutputs

