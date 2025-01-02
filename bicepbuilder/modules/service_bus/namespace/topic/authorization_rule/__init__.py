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


class AuthorizationRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the service bus namespace topic."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


class AuthorizationRuleOutputs(TypedDict, total=False):
    """Outputs for AuthorizationRule"""
    name: Output[Literal['string']]
    """The name of the authorization rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the authorization rule was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the authorization rule."""


class AuthorizationRuleBicep(Module):
    outputs: AuthorizationRuleOutputs
