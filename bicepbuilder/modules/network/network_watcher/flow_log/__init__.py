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


class FlowLog(TypedDict, total=False):
    """"""
    storageId: Required[str]
    """Resource ID of the diagnostic storage account."""
    targetResourceId: Required[str]
    """Resource ID of the NSG that must be enabled for Flow Logs."""
    enabled: bool
    """If the flow log should be enabled."""
    formatVersion: Literal[1, 2]
    """The flow log format version."""
    location: str
    """Location for all resources."""
    name: str
    """Name of the resource."""
    networkWatcherName: str
    """Name of the network watcher resource. Must be in the resource group where the Flow log will be created and same region as the NSG."""
    retentionInDays: int
    """Specifies the number of days that logs will be kept for; a value of 0 will retain data indefinitely."""
    tags: Dict[str, object]
    """Tags of the resource."""
    trafficAnalyticsInterval: Literal[10, 60]
    """The interval in minutes which would decide how frequently TA service should do flow analytics."""
    workspaceResourceId: str
    """Specify the Log Analytics Workspace Resource ID."""


class FlowLogOutputs(TypedDict, total=False):
    """Outputs for FlowLog"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the flow log."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the flow log was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the flow log."""


class FlowLogBicep(Module):
    outputs: FlowLogOutputs

