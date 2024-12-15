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


class Schedule(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Automation Account schedule."""
    advancedSchedule: Dict[str, object]
    """The properties of the create Advanced Schedule."""
    description: str
    """The description of the schedule."""
    expiryTime: str
    """The end time of the schedule."""
    frequency: Literal['Day', 'Hour', 'Minute', 'Month', 'OneTime', 'Week']
    """The frequency of the schedule."""
    interval: int
    """Anything."""
    startTime: str
    """The start time of the schedule."""
    timeZone: str
    """The time zone of the schedule."""
    baseTime: str
    """Time used as a basis for e.g. the schedule start date."""


class ScheduleOutputs(TypedDict, total=False):
    """Outputs for Schedule"""
    name: Output[Literal['string']]
    """The name of the deployed schedule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed schedule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed schedule."""


class ScheduleBicep(Module):
    outputs: ScheduleOutputs

