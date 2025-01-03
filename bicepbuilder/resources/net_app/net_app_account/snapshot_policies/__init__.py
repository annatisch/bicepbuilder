from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class SnapshotPolicy(TypedDict, total=False):
    """"""
    dailyHour: Required[int]
    """The daily snapshot hour."""
    dailyMinute: Required[int]
    """The daily snapshot minute."""
    dailySnapshotsToKeep: Required[int]
    """Daily snapshot count to keep."""
    dailyUsedBytes: Required[int]
    """Daily snapshot used bytes."""
    daysOfMonth: Required[str]
    """The monthly snapshot day."""
    hourlyMinute: Required[int]
    """The hourly snapshot minute."""
    hourlySnapshotsToKeep: Required[int]
    """Hourly snapshot count to keep."""
    hourlyUsedBytes: Required[int]
    """Hourly snapshot used bytes."""
    monthlyHour: Required[int]
    """The monthly snapshot hour."""
    monthlyMinute: Required[int]
    """The monthly snapshot minute."""
    monthlySnapshotsToKeep: Required[int]
    """Monthly snapshot count to keep."""
    monthlyUsedBytes: Required[int]
    """Monthly snapshot used bytes."""
    snapshotPolicyName: Required[str]
    """The name of the snapshot policy."""
    weeklyDay: Required[str]
    """The weekly snapshot day."""
    weeklyHour: Required[int]
    """The weekly snapshot hour."""
    weeklyMinute: Required[int]
    """The weekly snapshot minute."""
    weeklySnapshotsToKeep: Required[int]
    """Weekly snapshot count to keep."""
    weeklyUsedBytes: Required[int]
    """Weekly snapshot used bytes."""
    snapEnabled: bool
    """Indicates whether the snapshot policy is enabled."""
    snapshotPolicyLocation: str
    """The location of the snapshot policy."""


class SnapshotPolicyOutputs(TypedDict, total=False):
    """Outputs for SnapshotPolicy"""
    name: Output[Literal['string']]
    """The name of the Backup Policy."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Snapshot was created in."""
    resourceId: Output[Literal['string']]
    """The resource IDs of the snapshot Policy created within volume."""


class SnapshotPolicyModule(Module):
    outputs: SnapshotPolicyOutputs

