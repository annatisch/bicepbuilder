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


class ConnectionMonitor(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the resource."""
    endpoints: List[object]
    """List of connection monitor endpoints."""
    location: str
    """Location for all resources."""
    networkWatcherName: str
    """Name of the network watcher resource. Must be in the resource group where the Flow log will be created and same region as the NSG."""
    tags: Dict[str, object]
    """Tags of the resource."""
    testConfigurations: List[object]
    """List of connection monitor test configurations."""
    testGroups: List[object]
    """List of connection monitor test groups."""
    workspaceResourceId: str
    """Specify the Log Analytics Workspace Resource ID."""


class ConnectionMonitorOutputs(TypedDict, total=False):
    """Outputs for ConnectionMonitor"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed connection monitor."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the connection monitor was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed connection monitor."""


class ConnectionMonitorBicep(Module):
    outputs: ConnectionMonitorOutputs

