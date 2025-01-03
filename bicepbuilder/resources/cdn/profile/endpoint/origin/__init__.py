from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Origin(TypedDict, total=False):
    """"""
    endpointName: Required[str]
    """The name of the CDN Endpoint."""
    hostName: Required[str]
    """The hostname of the origin."""
    name: Required[str]
    """The name of the origin."""
    priority: int
    """The priority of origin in given origin group for load balancing. Required if """
    privateLinkAlias: str
    """The private link alias of the origin. Required if privateLinkLocation is provided."""
    privateLinkLocation: str
    """The private link location of the origin. Required if privateLinkAlias is provided."""
    weight: int
    """The weight of the origin used for load balancing. Required if """
    enabled: bool
    """Whether the origin is enabled for load balancing."""
    httpPort: int
    """The HTTP port of the origin."""
    httpsPort: int
    """The HTTPS port of the origin."""
    originHostHeader: str
    """The host header value sent to the origin."""
    privateLinkResourceId: str
    """The private link resource ID of the origin."""
    profileName: str
    """The name of the CDN profile. Default to "default"."""


class OriginOutputs(TypedDict, total=False):
    """Outputs for Origin"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the endpoint was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the endpoint."""


class OriginModule(Module):
    outputs: OriginOutputs

