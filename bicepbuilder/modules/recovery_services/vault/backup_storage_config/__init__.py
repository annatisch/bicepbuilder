from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class BackupStorageConfigBicep(Module):
    outputs: BackupStorageConfigOutputs

