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


class BackupPolicy(TypedDict, total=False):
    """"""
    backupVaultName: Required[str]
    """The name of the backup vault."""
    name: str
    """The name of the backup policy."""
    properties: Dict[str, object]
    """The properties of the backup policy."""


class BackupPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupPolicy"""
    name: Output[Literal['string']]
    """The name of the backup policy."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the backup policy was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the backup policy."""


class BackupPolicyBicep(Module):
    outputs: BackupPolicyOutputs

