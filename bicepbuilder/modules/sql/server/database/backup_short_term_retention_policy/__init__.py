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
    databaseName: Required[str]
    """The name of the parent database."""
    serverName: Required[str]
    """The name of the parent SQL Server."""
    diffBackupIntervalInHours: int
    """Differential backup interval in hours. For Hyperscal tiers this value will be ignored."""
    retentionDays: int
    """Poin-in-time retention in days."""


class BackupShortTermRetentionPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupShortTermRetentionPolicy"""
    name: Output[Literal['string']]
    """The name of the short-term policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the short-term policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the short-term policy."""


class BackupShortTermRetentionPolicyBicep(Module):
    outputs: BackupShortTermRetentionPolicyOutputs

