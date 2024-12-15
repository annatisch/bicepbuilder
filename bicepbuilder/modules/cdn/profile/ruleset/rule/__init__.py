from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Rule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the rule."""
    order: Required[int]
    """The order in which this rule will be applied. Rules with a lower order are applied before rules with a higher order."""
    profileName: Required[str]
    """The name of the profile."""
    ruleSetName: Required[str]
    """The name of the rule set."""
    actions: List[object]
    """A list of actions that are executed when all the conditions of a rule are satisfied."""
    conditions: List[object]
    """A list of conditions that must be matched for the actions to be executed."""
    matchProcessingBehavior: Literal['Continue', 'Stop']
    """If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue."""


class RuleOutputs(TypedDict, total=False):
    """Outputs for Rule"""
    name: Output[Literal['string']]
    """The name of the rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the custom domain was created in."""
    resourceId: Output[Literal['string']]
    """The resource id of the rule."""


class RuleBicep(Module):
    outputs: RuleOutputs

