from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class DataSource(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the data source."""
    counterName: str
    """Counter name to configure when kind is WindowsPerformanceCounter."""
    eventLogName: str
    """Windows event log name to configure when kind is WindowsEvent."""
    eventTypes: List[object]
    """Windows event types to configure when kind is WindowsEvent."""
    instanceName: str
    """Name of the instance to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    intervalSeconds: int
    """Interval in seconds to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    kind: Literal['AzureActivityLog', 'IISLogs', 'LinuxPerformanceCollection', 'LinuxPerformanceObject', 'LinuxSyslog', 'LinuxSyslogCollection', 'WindowsEvent', 'WindowsPerformanceCounter']
    """The kind of the data source."""
    linkedResourceId: str
    """Resource ID of the resource to be linked."""
    objectName: str
    """Name of the object to configure when kind is WindowsPerformanceCounter or LinuxPerformanceObject."""
    performanceCounters: List[object]
    """List of counters to configure when the kind is LinuxPerformanceObject."""
    state: str
    """State to configure when kind is IISLogs or LinuxSyslogCollection or LinuxPerformanceCollection."""
    syslogName: str
    """System log to configure when kind is LinuxSyslog."""
    syslogSeverities: List[object]
    """Severities to configure when kind is LinuxSyslog."""
    tags: Dict[str, object]
    """Tags to configure in the resource."""


class DataSourceOutputs(TypedDict, total=False):
    """Outputs for DataSource"""
    name: Output[Literal['string']]
    """The name of the deployed data source."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the data source is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed data source."""


class DataSourceModule(Module):
    outputs: DataSourceOutputs

