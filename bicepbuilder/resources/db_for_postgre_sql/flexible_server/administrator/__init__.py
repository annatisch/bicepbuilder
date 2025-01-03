from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Administrator(TypedDict, total=False):
    """"""
    objectId: Required[str]
    """The objectId of the Active Directory administrator."""
    principalName: Required[str]
    """Active Directory administrator principal name."""
    principalType: Required[Literal['Group', 'ServicePrincipal', 'Unknown', 'User']]
    """The principal type used to represent the type of Active Directory Administrator."""
    tenantId: str
    """The tenantId of the Active Directory administrator."""


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

