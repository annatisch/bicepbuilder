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


class Topic(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Event Grid Domain Topic."""


class TopicOutputs(TypedDict, total=False):
    """Outputs for Topic"""
    name: Output[Literal['string']]
    """The name of the event grid topic."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the event grid topic was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the event grid topic."""


class TopicBicep(Module):
    outputs: TopicOutputs

