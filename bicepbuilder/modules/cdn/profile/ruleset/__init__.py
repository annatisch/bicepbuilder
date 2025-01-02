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


class Ruleset(TypedDict, total=False):
    """"""


class RulesetOutputs(TypedDict, total=False):
    """Outputs for Ruleset"""
    name: Output[Literal['string']]
    """The name of the rule set."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the custom domain was created in."""
    resourceId: Output[Literal['string']]
    """The resource id of the rule set."""


class RulesetBicep(Module):
    outputs: RulesetOutputs

