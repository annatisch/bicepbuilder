from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Administrator(TypedDict, total=False):
    """"""
    administratorType: Required[str]
    """Workspace active directory administrator type."""
    login: Required[str]
    """Login of the workspace active directory administrator."""
    sid: Required[str]
    """Object ID of the workspace active directory administrator."""
    tenantId: str
    """Tenant ID of the workspace active directory administrator."""


class AdministratorOutputs(TypedDict, total=False):
    """Outputs for Administrator"""
    name: Output[Literal['string']]
    """The name of the deployed administrator."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed administrator."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed administrator."""


class AdministratorModule(Module):
    outputs: AdministratorOutputs

