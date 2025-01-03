from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class MetaData(TypedDict, total=False):
    """The destination metadata."""
    eventHubName: str
    """Allows to define an Event Hub name. Not applicable when destination is Storage Account."""


class Destination(TypedDict, total=False):
    """Destination properties."""
    resourceId: Required[str]
    """The destination resource ID."""
    metaData: 'MetaData'
    """The destination metadata."""


class DataExport(TypedDict, total=False):
    """"""
    name: Required[str]
    """The data export rule name."""
    tableNames: Required[List[object]]
    """An array of tables to export, for example: ['Heartbeat', 'SecurityEvent']."""
    destination: 'Destination'
    """Destination properties."""
    enable: bool
    """Active when enabled."""


class DataExportOutputs(TypedDict, total=False):
    """Outputs for DataExport"""
    name: Output[Literal['string']]
    """The name of the data export."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the data export was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the data export."""


class DataExportModule(Module):
    outputs: DataExportOutputs

