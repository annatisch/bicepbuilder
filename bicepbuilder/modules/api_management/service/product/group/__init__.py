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


class Group(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the product group."""


class GroupOutputs(TypedDict, total=False):
    """Outputs for Group"""
    name: Output[Literal['string']]
    """The name of the product group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the product group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the product group."""


class GroupBicep(Module):
    outputs: GroupOutputs

