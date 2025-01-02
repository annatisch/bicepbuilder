from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class BackupShortTermRetentionPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Short Term Retention backup policy. For example "default"."""
    retentionDays: int
    """The backup retention period in days. This is how many days Point-in-Time Restore will be supported."""


class BackupShortTermRetentionPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupShortTermRetentionPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed database backup short-term retention policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed database backup short-term retention policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed database backup short-term retention policy."""


class BackupShortTermRetentionPolicyBicep(Module):
    outputs: BackupShortTermRetentionPolicyOutputs

