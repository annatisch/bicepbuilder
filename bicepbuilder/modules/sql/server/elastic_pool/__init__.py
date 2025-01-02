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


class PerDatabaseSetting(TypedDict, total=False):
    """The per database settings for the elastic pool."""
    maxCapacity: Required[str]
    """The maximum capacity any one database can consume. Examples: '0.5', '2'."""
    minCapacity: Required[str]
    """The minimum capacity all databases are guaranteed. Examples: '0.5', '1'."""
    autoPauseDelay: int
    """Auto Pause Delay for per database within pool."""


class Sku(TypedDict, total=False):
    """The elastic pool SKU."""
    name: Required[Literal['BasicPool', 'BC_DC', 'BC_Gen5', 'GP_DC', 'GP_FSv2', 'GP_Gen5', 'HS_Gen5', 'HS_MOPRMS', 'HS_PRMS', 'PremiumPool', 'ServerlessPool', 'StandardPool']]
    """The name of the SKU, typically, a letter + Number code, e.g. P3."""
    capacity: int
    """The capacity of the particular SKU."""
    family: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    size: str
    """Size of the particular SKU."""
    tier: str
    """The tier or edition of the particular SKU, e.g. Basic, Premium."""


class ElasticPool(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Elastic Pool."""
    autoPauseDelay: int
    """Time in minutes after which elastic pool is automatically paused. A value of -1 means that automatic pause is disabled."""
    availabilityZone: Literal['1', '2', '3', 'NoPreference']
    """Specifies the availability zone the pool's primary replica is pinned to."""
    highAvailabilityReplicaCount: int
    """The number of secondary replicas associated with the elastic pool that are used to provide high availability. Applicable only to Hyperscale elastic pools."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this elastic pool."""
    location: str
    """Location for all resources."""
    maintenanceConfigurationId: str
    """Maintenance configuration resource ID assigned to the elastic pool. This configuration defines the period when the maintenance updates will will occur."""
    maxSizeBytes: int
    """The storage limit for the database elastic pool in bytes."""
    minCapacity: int
    """Minimal capacity that serverless pool will not shrink below, if not paused."""
    perDatabaseSettings: 'PerDatabaseSetting'
    """The per database settings for the elastic pool."""
    preferredEnclaveType: Literal['Default', 'VBS']
    """Type of enclave requested on the elastic pool."""
    sku: 'Sku'
    """The elastic pool SKU."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneRedundant: bool
    """Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones."""


class ElasticPoolOutputs(TypedDict, total=False):
    """Outputs for ElasticPool"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed Elastic Pool."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed Elastic Pool."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Elastic Pool."""


class ElasticPoolBicep(Module):
    outputs: ElasticPoolOutputs

