from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class FabricCapacity(TypedDict, total=False):
    """"""
    adminMembers: Required[List[object]]
    """List of admin members. Format: ["something@domain.com"]."""
    name: Required[str]
    """Name of the resource to create."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    skuName: Literal['F1024', 'F128', 'F16', 'F2', 'F2048', 'F256', 'F32', 'F4', 'F512', 'F64', 'F8']
    """SKU tier of the Fabric resource."""
    skuTier: Literal['Fabric']
    """SKU name of the Fabric resource."""
    tags: Dict[str, object]
    """Tags of the resource."""


class FabricCapacityOutputs(TypedDict, total=False):
    """Outputs for FabricCapacity"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed Fabric resource."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the module was deployed to."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Fabric resource."""


class FabricCapacityModule(Module):
    outputs: FabricCapacityOutputs

