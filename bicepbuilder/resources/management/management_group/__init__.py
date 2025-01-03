from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ManagementGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The group ID of the Management group."""
    displayName: str
    """The friendly name of the management group. If no value is passed then this field will be set to the group ID."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location deployment metadata."""
    parentId: str
    """The management group parent ID. Defaults to current scope."""


class ManagementGroupOutputs(TypedDict, total=False):
    """Outputs for ManagementGroup"""
    name: Output[Literal['string']]
    """The name of the management group."""
    resourceId: Output[Literal['string']]
    """The resource ID of the management group."""


class ManagementGroupModule(Module):
    outputs: ManagementGroupOutputs

