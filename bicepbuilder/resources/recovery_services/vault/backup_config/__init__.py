from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class BackupConfig(TypedDict, total=False):
    """"""
    enhancedSecurityState: Literal['Disabled', 'Enabled']
    """Enable this setting to protect hybrid backups against accidental deletes and add additional layer of authentication for critical operations."""
    isSoftDeleteFeatureStateEditable: bool
    """Is soft delete feature state editable."""
    name: str
    """Name of the Azure Recovery Service Vault Backup Policy."""
    resourceGuardOperationRequests: List[object]
    """ResourceGuard Operation Requests."""
    softDeleteFeatureState: Literal['Disabled', 'Enabled']
    """Enable this setting to protect backup data for Azure VM, SQL Server in Azure VM and SAP HANA in Azure VM from accidental deletes."""
    storageModelType: Literal['GeoRedundant', 'LocallyRedundant', 'ReadAccessGeoZoneRedundant', 'ZoneRedundant']
    """Storage type."""
    storageType: Literal['GeoRedundant', 'LocallyRedundant', 'ReadAccessGeoZoneRedundant', 'ZoneRedundant']
    """Storage type."""
    storageTypeState: Literal['Locked', 'Unlocked']
    """Once a machine is registered against a resource, the storageTypeState is always Locked."""


class BackupConfigOutputs(TypedDict, total=False):
    """Outputs for BackupConfig"""
    name: Output[Literal['string']]
    """The name of the backup config."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the backup config was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the backup config."""


class BackupConfigModule(Module):
    outputs: BackupConfigOutputs

