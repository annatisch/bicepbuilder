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


class ReplicationPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the replication policy."""
    appConsistentFrequencyInMinutes: int
    """The app consistent snapshot frequency (in minutes)."""
    crashConsistentFrequencyInMinutes: int
    """The crash consistent snapshot frequency (in minutes)."""
    multiVmSyncStatus: Literal['Disable', 'Enable']
    """A value indicating whether multi-VM sync has to be enabled."""
    recoveryPointHistory: int
    """The duration in minutes until which the recovery points need to be stored."""


class ReplicationPolicyOutputs(TypedDict, total=False):
    """Outputs for ReplicationPolicy"""
    name: Output[Literal['string']]
    """The name of the replication policy."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication policy was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication policy."""


class ReplicationPolicyBicep(Module):
    outputs: ReplicationPolicyOutputs

