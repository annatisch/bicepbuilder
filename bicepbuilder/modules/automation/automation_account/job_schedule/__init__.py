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


class JobSchedule(TypedDict, total=False):
    """"""
    runbookName: Required[str]
    """The runbook property associated with the entity."""
    scheduleName: Required[str]
    """The schedule property associated with the entity."""
    parameters: Dict[str, object]
    """List of job properties."""
    runOn: str
    """The hybrid worker group that the scheduled job should run on."""
    name: str
    """Name of the Automation Account job schedule. Must be a GUID and is autogenerated. No need to provide this value."""


class JobScheduleOutputs(TypedDict, total=False):
    """Outputs for JobSchedule"""
    name: Output[Literal['string']]
    """The name of the deployed job schedule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed job schedule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed job schedule."""


class JobScheduleBicep(Module):
    outputs: JobScheduleOutputs

