from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class BackupStorageConfig(TypedDict, total=False):
    """"""
    crossRegionRestoreFlag: bool
    """Opt in details of Cross Region Restore feature."""
    name: str
    """The name of the backup storage config."""
    storageModelType: Literal['GeoRedundant', 'LocallyRedundant', 'ReadAccessGeoZoneRedundant', 'ZoneRedundant']
    """Change Vault Storage Type (Works if vault has not registered any backup instance)."""


class BackupStorageConfigOutputs(TypedDict, total=False):
    """Outputs for BackupStorageConfig"""
    name: Output[Literal['string']]
    """The name of the backup storage config."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the backup storage configuration was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the backup storage config."""


class BackupStorageConfigModule(Module):
    outputs: BackupStorageConfigOutputs

