from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Diagnostic(TypedDict, total=False):
    """"""
    apiManagementServiceName: Required[str]
    """The name of the parent API Management service."""
    apiName: Required[str]
    """The name of the parent API."""
    loggerName: Required[str]
    """The name of the logger."""
    httpCorrelationProtocol: Literal['Legacy', 'None', 'W3C']
    """Sets correlation protocol to use for Application Insights diagnostics. Required if using Application Insights."""
    metrics: bool
    """Emit custom metrics via emit-metric policy. Required if using Application Insights."""
    operationNameFormat: Literal['Name', 'URI']
    """The format of the Operation Name for Application Insights telemetries. Required if using Application Insights."""
    alwaysLog: str
    """Specifies for what type of messages sampling settings should not apply."""
    backend: Dict[str, object]
    """Diagnostic settings for incoming/outgoing HTTP messages to the Backend."""
    frontend: Dict[str, object]
    """Diagnostic settings for incoming/outgoing HTTP messages to the Gateway."""
    logClientIp: bool
    """Log the ClientIP."""
    name: Literal['applicationinsights', 'azuremonitor', 'local']
    """Type of diagnostic resource."""
    samplingPercentage: int
    """Rate of sampling for fixed-rate sampling. Specifies the percentage of requests that are logged. 0% sampling means zero requests logged, while 100% sampling means all requests logged."""
    verbosity: Literal['error', 'information', 'verbose']
    """The verbosity level applied to traces emitted by trace policies."""


class DiagnosticOutputs(TypedDict, total=False):
    """Outputs for Diagnostic"""
    name: Output[Literal['string']]
    """The name of the API diagnostic."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API diagnostic was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API diagnostic."""


class DiagnosticBicep(Module):
    outputs: DiagnosticOutputs

