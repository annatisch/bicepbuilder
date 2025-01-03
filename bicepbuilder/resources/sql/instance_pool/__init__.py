from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class SqlInstancePool(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the instance pool."""
    subnetResourceId: Required[str]
    """The subnet resource ID for the instance pool."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this database."""
    location: str
    """Location for all resources."""
    skuFamily: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    skuName: str
    """The SKU name for the instance pool."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tier: Literal['GeneralPurpose']
    """The vCore service tier for the instance pool."""
    vCores: Literal[8, 16, 24, 32, 40, 64, 80, 96, 128, 160, 192, 224, 256]
    """The number of vCores for the instance pool."""


class SqlInstancePoolOutputs(TypedDict, total=False):
    """Outputs for SqlInstancePool"""
    instancePoolLocation: Output[Literal['string']]
    """The location of the SQL instance pool."""
    name: Output[Literal['string']]
    """The name of the SQL instance pool."""
    resourceGroupName: Output[Literal['string']]
    """The resource group name of the SQL instance pool."""
    resourceId: Output[Literal['string']]
    """The ID of the SQL instance pool."""


class SqlInstancePoolModule(Module):
    outputs: SqlInstancePoolOutputs

