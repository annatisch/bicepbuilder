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


class AuditSetting(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the audit settings."""
    auditActionsAndGroups: List[object]
    """Specifies the Actions-Groups and Actions to audit."""
    isAzureMonitorTargetEnabled: bool
    """Specifies whether audit events are sent to Azure Monitor."""
    isDevopsAuditEnabled: bool
    """Specifies the state of devops audit. If state is Enabled, devops logs will be sent to Azure Monitor."""
    isManagedIdentityInUse: bool
    """Specifies whether Managed Identity is used to access blob storage."""
    isStorageSecondaryKeyInUse: bool
    """Specifies whether storageAccountAccessKey value is the storage's secondary key."""
    queueDelayMs: int
    """Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed."""
    retentionDays: int
    """Specifies the number of days to keep in the audit logs in the storage account."""
    state: Literal['Disabled', 'Enabled']
    """Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required."""
    storageAccountResourceId: str
    """A blob storage to hold the auditing storage account."""


class AuditSettingOutputs(TypedDict, total=False):
    """Outputs for AuditSetting"""
    name: Output[Literal['string']]
    """The name of the deployed audit settings."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed audit settings."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed audit settings."""


class AuditSettingBicep(Module):
    outputs: AuditSettingOutputs

