from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Variable(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the variable."""
    value: Required[str]
    """The value of the variable. For security best practices, this value is always passed as a secure string as it could contain an encrypted value when the "isEncrypted" property is set to true."""
    description: str
    """The description of the variable."""
    isEncrypted: bool
    """If the variable should be encrypted. For security reasons encryption of variables should be enabled."""


class VariableOutputs(TypedDict, total=False):
    """Outputs for Variable"""
    name: Output[Literal['string']]
    """The name of the deployed variable."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed variable."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed variable."""


class VariableModule(Module):
    outputs: VariableOutputs

