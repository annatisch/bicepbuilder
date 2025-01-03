from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Snapshot(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Elastic SAN Volume Snapshot. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""
    location: str
    """Location for all resources."""


class SnapshotOutputs(TypedDict, total=False):
    """Outputs for Snapshot"""
    location: Output[Literal['string']]
    """The location of the deployed Elastic SAN Volume Snapshot."""
    name: Output[Literal['string']]
    """The name of the deployed Elastic SAN Volume Snapshot."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed Elastic SAN Volume Snapshot."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Elastic SAN Volume Snapshot."""


class SnapshotModule(Module):
    outputs: SnapshotOutputs

