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


class StaticMember(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the static member."""
    resourceId: Required[str]
    """Resource ID of the virtual network."""


class StaticMemberOutputs(TypedDict, total=False):
    """Outputs for StaticMember"""
    name: Output[Literal['string']]
    """The name of the deployed static member."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the static member was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed static member."""


class StaticMemberBicep(Module):
    outputs: StaticMemberOutputs

