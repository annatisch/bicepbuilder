from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
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


class DatabaseModule(Module):
    outputs: DatabaseOutputs

