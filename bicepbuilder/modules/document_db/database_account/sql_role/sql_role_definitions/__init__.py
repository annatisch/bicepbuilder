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


class SqlRoleDefinition(TypedDict, total=False):
    """"""
    dataActions: List[object]
    """An array of data actions that are allowed."""
    roleName: str
    """A user-friendly name for the Role Definition. Must be unique for the database account."""
    roleType: Literal['BuiltInRole', 'CustomRole']
    """Indicates whether the Role Definition was built-in or user created."""


class SqlRoleDefinitionOutputs(TypedDict, total=False):
    """Outputs for SqlRoleDefinition"""
    name: Output[Literal['string']]
    """The name of the SQL database."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the SQL database was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the SQL database."""


class SqlRoleDefinitionBicep(Module):
    outputs: SqlRoleDefinitionOutputs

