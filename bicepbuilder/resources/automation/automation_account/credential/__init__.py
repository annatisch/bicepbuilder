from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Credential(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Automation Account credential."""
    password: Required[str]
    """Password of the credential."""
    userName: Required[str]
    """The user name associated to the credential."""
    description: str
    """Description of the credential."""


class CredentialOutputs(TypedDict, total=False):
    """Outputs for Credential"""
    name: Output[Literal['string']]
    """The name of the credential associated to the automation account."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed credential."""
    resourceId: Output[Literal['string']]
    """The resource Id of the credential associated to the automation account."""


class CredentialModule(Module):
    outputs: CredentialOutputs

