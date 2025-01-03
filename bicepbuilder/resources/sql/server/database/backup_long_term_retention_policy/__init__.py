from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class BackupLongTermRetentionPolicy(TypedDict, total=False):
    """"""
    databaseName: Required[str]
    """The name of the parent database."""
    serverName: Required[str]
    """The name of the parent SQL Server."""
    backupStorageAccessTier: Literal['Archive', 'Hot']
    """The BackupStorageAccessTier for the LTR backups."""
    makeBackupsImmutable: bool
    """The setting whether to make LTR backups immutable."""
    monthlyRetention: str
    """Monthly retention in ISO 8601 duration format."""
    weeklyRetention: str
    """Weekly retention in ISO 8601 duration format."""
    weekOfYear: int
    """Week of year backup to keep for yearly retention."""
    yearlyRetention: str
    """Yearly retention in ISO 8601 duration format."""


class BackupLongTermRetentionPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupLongTermRetentionPolicy"""
    name: Output[Literal['string']]
    """The name of the long-term policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the long-term policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the long-term policy."""


class BackupLongTermRetentionPolicyModule(Module):
    outputs: BackupLongTermRetentionPolicyOutputs

