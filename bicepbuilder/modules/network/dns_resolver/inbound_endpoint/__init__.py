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


class InboundEndpoint(TypedDict, total=False):
    """"""
    dnsResolverName: Required[str]
    """Name of the DNS Private Resolver."""
    name: Required[str]
    """The name of the inbound endpoint."""
    subnetResourceId: Required[str]
    """The subnet ID of the inbound endpoint."""
    location: str
    """Location for all resources."""
    privateIpAddress: str
    """The private IP address of the inbound endpoint."""
    privateIpAllocationMethod: str
    """The private IP allocation method of the inbound endpoint."""
    tags: Dict[str, object]
    """Tags of the resource."""


class InboundEndpointOutputs(TypedDict, total=False):
    """Outputs for InboundEndpoint"""
    name: Output[Literal['string']]
    """The name of the resource."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the resource."""
    resourceId: Output[Literal['string']]
    """The resource ID of the resource."""


class InboundEndpointBicep(Module):
    outputs: InboundEndpointOutputs
