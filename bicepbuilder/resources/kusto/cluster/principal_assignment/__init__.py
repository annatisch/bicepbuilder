from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class PrincipalAssignment(TypedDict, total=False):
    """"""
    principalId: Required[str]
    """The principal id assigned to the Kusto Cluster principal. It can be a user email, application id, or security group name."""
    principalType: Required[Literal['App', 'Group', 'User']]
    """The principal type of the principal id."""
    role: Required[Literal['AllDatabasesAdmin', 'AllDatabasesViewer']]
    """The Kusto Cluster role to be assigned to the principal id."""
    tenantId: str
    """The tenant id of the principal id."""


class PrincipalAssignmentOutputs(TypedDict, total=False):
    """Outputs for PrincipalAssignment"""
    name: Output[Literal['string']]
    """The name of the deployed Kusto Cluster Principal Assignment."""
    resourceGroupName: Output[Literal['string']]
    """The resource group name of the deployed Kusto Cluster Principal Assignment."""
    resourceId: Output[Literal['string']]
    """The resource id of the deployed Kusto Cluster Principal Assignment."""


class PrincipalAssignmentModule(Module):
    outputs: PrincipalAssignmentOutputs

