from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Snapshot(TypedDict, total=False):
    """List of Elastic SAN Volume Snapshots to be created in the Elastic SAN Volume."""
    name: Required[str]
    """The name of the Elastic SAN Volume Snapshot. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""


class Volume(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Elastic SAN Volume. The name can only contain lowercase letters, numbers, hyphens and underscores, and must begin and end with a letter or a number. Each hyphen and underscore must be preceded and followed by an alphanumeric character."""
    sizeGiB: Required[int]
    """Size of the Elastic SAN Volume in Gibibytes (GiB). The supported capacity ranges from 1 Gibibyte (GiB) to 64 Tebibyte (TiB), equating to 65536 Gibibytes (GiB)."""
    location: str
    """Location for all resources."""
    snapshots: List['Snapshot']
    """List of Elastic SAN Volume Snapshots to be created in the Elastic SAN Volume."""


class VolumeOutputs(TypedDict, total=False):
    """Outputs for Volume"""
    location: Output[Literal['string']]
    """The location of the deployed Elastic SAN Volume."""
    name: Output[Literal['string']]
    """The name of the deployed Elastic SAN Volume."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed Elastic SAN Volume."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Elastic SAN Volume."""
    snapshots: Output[Literal['array']]
    """Details on the deployed Elastic SAN Volume Snapshots."""
    targetIqn: Output[Literal['string']]
    """The iSCSI Target IQN (iSCSI Qualified Name) of the deployed Elastic SAN Volume."""
    targetPortalHostname: Output[Literal['string']]
    """The iSCSI Target Portal Host Name of the deployed Elastic SAN Volume."""
    targetPortalPort: Output[Literal['int']]
    """The iSCSI Target Portal Port of the deployed Elastic SAN Volume."""
    volumeId: Output[Literal['string']]
    """The volume Id of the deployed Elastic SAN Volume."""


class VolumeModule(Module):
    outputs: VolumeOutputs

