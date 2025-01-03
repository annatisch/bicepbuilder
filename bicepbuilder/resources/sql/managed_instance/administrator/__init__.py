from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Administrator(TypedDict, total=False):
    """"""
    login: Required[str]
    """Login name of the managed instance administrator."""
    sid: Required[str]
    """SID (object ID) of the managed instance administrator."""
    tenantId: str
    """Tenant ID of the managed instance administrator."""


class AdministratorOutputs(TypedDict, total=False):
    """Outputs for Administrator"""
    name: Output[Literal['string']]
    """The name of the deployed managed instance administrator."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed managed instance administrator."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed managed instance administrator."""


class AdministratorModule(Module):
    outputs: AdministratorOutputs

