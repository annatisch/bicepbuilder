from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class OutboundEndpoint(TypedDict, total=False):
    """"""
    dnsResolverName: Required[str]
    """Name of the DNS Private Resolver."""
    name: Required[str]
    """The name of the inbound endpoint."""
    subnetResourceId: Required[str]
    """The subnet ID of the inbound endpoint."""
    location: str
    """Location for all resources."""
    tags: Dict[str, object]
    """Tags of the resource."""


class OutboundEndpointOutputs(TypedDict, total=False):
    """Outputs for OutboundEndpoint"""
    name: Output[Literal['string']]
    """The name of the resource."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the resource."""
    resourceId: Output[Literal['string']]
    """The resource ID of the resource."""


class OutboundEndpointModule(Module):
    outputs: OutboundEndpointOutputs

