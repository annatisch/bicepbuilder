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


class SqlRoleAssignment(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the SQL Role Assignment."""
    roleDefinitionId: Required[str]
    """Id of the SQL Role Definition."""
    principalId: str
    """Id needs to be granted."""


class SqlRoleAssignmentOutputs(TypedDict, total=False):
    """Outputs for SqlRoleAssignment"""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the SQL Role Assignment was created in."""


class SqlRoleAssignmentBicep(Module):
    outputs: SqlRoleAssignmentOutputs

