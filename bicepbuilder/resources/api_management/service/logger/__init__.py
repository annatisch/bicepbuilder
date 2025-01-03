from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Logger(TypedDict, total=False):
    """"""
    name: Required[str]
    """Resource Name."""
    type: Required[Literal['applicationInsights', 'azureEventHub', 'azureMonitor']]
    """Logger type."""
    credentials: Required[Dict[str, object]]
    """Required if loggerType = applicationInsights or azureEventHub. The name and SendRule connection string of the event hub for azureEventHub logger. Instrumentation key for applicationInsights logger."""
    targetResourceId: Required[str]
    """Required if loggerType = applicationInsights or azureEventHub. Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource)."""
    description: str
    """Logger description."""
    isBuffered: bool
    """Whether records are buffered in the logger before publishing."""


class LoggerOutputs(TypedDict, total=False):
    """Outputs for Logger"""
    name: Output[Literal['string']]
    """The name of the logger."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the named value was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the logger."""


class LoggerModule(Module):
    outputs: LoggerOutputs

