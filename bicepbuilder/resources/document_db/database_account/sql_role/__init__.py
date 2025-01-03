from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class SqlRole(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the SQL Role."""
    dataActions: List[object]
    """An array of data actions that are allowed."""
    principalIds: List[object]
    """Ids needs to be granted."""
    roleName: str
    """A user-friendly name for the Role Definition. Must be unique for the database account."""
    roleType: Literal['BuiltInRole', 'CustomRole']
    """Indicates whether the Role Definition was built-in or user created."""


class SqlRoleOutputs(TypedDict, total=False):
    """Outputs for SqlRole"""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the SQL Role Definition and Assignment were created in."""


class SqlRoleModule(Module):
    outputs: SqlRoleOutputs

