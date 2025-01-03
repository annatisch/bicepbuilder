from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .......expressions import (
    BicepExpression,
    Module,
    Output,
)


class ReplicationProtectionContainerMapping(TypedDict, total=False):
    """"""
    name: str
    """The name of the replication container mapping. If not provided, it will be automatically generated as """
    policyId: str
    """Resource ID of the replication policy. If defined, policyName will be ignored."""
    policyName: str
    """Name of the replication policy. Will be ignored if policyId is also specified."""
    targetContainerFabricName: str
    """Name of the fabric containing the target container. If targetProtectionContainerId is specified, this parameter will be ignored."""
    targetContainerName: str
    """Name of the target container. Must be specified if targetProtectionContainerId is not. If targetProtectionContainerId is specified, this parameter will be ignored."""
    targetProtectionContainerId: str
    """Resource ID of the target Replication container. Must be specified if targetContainerName is not. If specified, targetContainerFabricName and targetContainerName will be ignored."""


class ReplicationProtectionContainerMappingOutputs(TypedDict, total=False):
    """Outputs for ReplicationProtectionContainerMapping"""
    name: Output[Literal['string']]
    """The name of the replication container."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the replication container was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the replication container."""


class ReplicationProtectionContainerMappingModule(Module):
    outputs: ReplicationProtectionContainerMappingOutputs

