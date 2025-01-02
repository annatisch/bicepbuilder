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


class BackupLongTermRetentionPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Long Term Retention backup policy. For example "default"."""
    monthlyRetention: str
    """The monthly retention policy for an LTR backup in an ISO 8601 format."""
    weeklyRetention: str
    """The weekly retention policy for an LTR backup in an ISO 8601 format."""
    weekOfYear: int
    """The week of year to take the yearly backup in an ISO 8601 format."""
    yearlyRetention: str
    """The yearly retention policy for an LTR backup in an ISO 8601 format."""


class BackupLongTermRetentionPolicyOutputs(TypedDict, total=False):
    """Outputs for BackupLongTermRetentionPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed database backup long-term retention policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed database backup long-term retention policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed database backup long-term retention policy."""


class BackupLongTermRetentionPolicyBicep(Module):
    outputs: BackupLongTermRetentionPolicyOutputs

