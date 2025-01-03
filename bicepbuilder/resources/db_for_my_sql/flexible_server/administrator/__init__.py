from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Administrator(TypedDict, total=False):
    """"""
    identityResourceId: Required[str]
    """The resource ID of the identity used for AAD Authentication."""
    login: Required[str]
    """Login name of the server administrator."""
    sid: Required[str]
    """SID (object ID) of the server administrator."""
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

