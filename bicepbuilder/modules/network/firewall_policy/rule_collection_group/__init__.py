from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class RuleCollectionGroupBicep(Module):
    outputs: RuleCollectionGroupOutputs

