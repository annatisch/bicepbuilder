from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Replication(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the replication."""
    location: str
    """Location for all resources."""
    regionEndpointEnabled: bool
    """Specifies whether the replication regional endpoint is enabled. Requests will not be routed to a replication whose regional endpoint is disabled, however its data will continue to be synced with other replications."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneRedundancy: Literal['Disabled', 'Enabled']
    """Whether or not zone redundancy is enabled for this container registry."""


class ReplicationOutputs(TypedDict, total=False):
    """Outputs for Replication"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the replication."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication."""


class ReplicationModule(Module):
    outputs: ReplicationOutputs

