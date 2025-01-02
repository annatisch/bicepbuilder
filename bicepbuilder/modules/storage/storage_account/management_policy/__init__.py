from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class ManagementPolicyBicep(Module):
    outputs: ManagementPolicyOutputs

