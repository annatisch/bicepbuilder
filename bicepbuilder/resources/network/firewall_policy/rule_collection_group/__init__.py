from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class RuleCollectionGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the rule collection group to deploy."""
    priority: Required[int]
    """Priority of the Firewall Policy Rule Collection Group resource."""
    ruleCollections: List[object]
    """Group of Firewall Policy rule collections."""


class RuleCollectionGroupOutputs(TypedDict, total=False):
    """Outputs for RuleCollectionGroup"""
    name: Output[Literal['string']]
    """The name of the deployed rule collection group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed rule collection group."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed rule collection group."""


class RuleCollectionGroupModule(Module):
    outputs: RuleCollectionGroupOutputs

