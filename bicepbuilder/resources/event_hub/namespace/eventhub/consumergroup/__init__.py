from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Consumergroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the consumer group."""
    userMetadata: str
    """User Metadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored."""


class ConsumergroupOutputs(TypedDict, total=False):
    """Outputs for Consumergroup"""
    name: Output[Literal['string']]
    """The name of the consumer group."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the consumer group was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the consumer group."""


class ConsumergroupModule(Module):
    outputs: ConsumergroupOutputs

