from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class AuthorizationRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the authorization rule."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


class AuthorizationRuleOutputs(TypedDict, total=False):
    """Outputs for AuthorizationRule"""
    name: Output[Literal['string']]
    """The name of the authorization rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the authorization rule was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the authorization rule."""


class AuthorizationRuleModule(Module):
    outputs: AuthorizationRuleOutputs

