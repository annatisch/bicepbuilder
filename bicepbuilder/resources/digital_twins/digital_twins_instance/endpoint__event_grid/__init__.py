from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class EndpointEventGrid(TypedDict, total=False):
    """"""
    eventGridDomainResourceId: Required[str]
    """The resource ID of the Event Grid to get access keys from."""
    topicEndpoint: Required[str]
    """EventGrid Topic Endpoint."""
    deadLetterSecret: str
    """Dead letter storage secret for key-based authentication. Will be obfuscated during read."""
    deadLetterUri: str
    """Dead letter storage URL for identity-based authentication."""
    name: str
    """The name of the Digital Twin Endpoint."""


class EndpointEventGridOutputs(TypedDict, total=False):
    """Outputs for EndpointEventGrid"""
    name: Output[Literal['string']]
    """The name of the Endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the resource was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Endpoint."""


class EndpointEventGridModule(Module):
    outputs: EndpointEventGridOutputs

