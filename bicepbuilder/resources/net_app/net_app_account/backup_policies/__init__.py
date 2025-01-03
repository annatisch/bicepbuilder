from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class BackupPolicy(TypedDict, total=False):
    """"""
    dailyBackupsToKeep: Required[int]
    """The daily backups to keep."""
    monthlyBackupsToKeep: Required[int]
    """The monthly backups to keep."""
    weeklyBackupsToKeep: Required[int]
    """The weekly backups to keep."""
    backupEnabled: bool
    """Indicates whether the backup policy is enabled."""
    backupPolicyName: str
    """The name of the backup policy."""


class BackupPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupPolicy"""
    name: Output[Literal['string']]
    """The name of the Backup Policy."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Backup Policy was created in."""
    resourceId: Output[Literal['string']]
    """The resource IDs of the backup Policy created within volume."""


class BackupPolicyModule(Module):
    outputs: BackupPolicyOutputs

