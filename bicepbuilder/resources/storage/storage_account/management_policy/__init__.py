from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ManagementPolicy(TypedDict, total=False):
    """"""
    rules: Required[List[object]]
    """The Storage Account ManagementPolicies Rules."""


class ManagementPolicyOutputs(TypedDict, total=False):
    """Outputs for ManagementPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed management policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed management policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed management policy."""


class ManagementPolicyModule(Module):
    outputs: ManagementPolicyOutputs

