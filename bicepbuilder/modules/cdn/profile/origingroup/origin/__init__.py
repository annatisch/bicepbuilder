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


class Origin(TypedDict, total=False):
    """"""
    hostName: Required[str]
    """The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint."""
    name: Required[str]
    """The name of the origion."""
    originGroupName: Required[str]
    """The name of the group."""
    profileName: Required[str]
    """The name of the CDN profile."""
    enabledState: Literal['Disabled', 'Enabled']
    """Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool."""
    enforceCertificateNameCheck: bool
    """Whether to enable certificate name check at origin level."""
    httpPort: int
    """The value of the HTTP port. Must be between 1 and 65535."""
    httpsPort: int
    """The value of the HTTPS port. Must be between 1 and 65535."""
    originHostHeader: str
    """The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure Front Door origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint."""
    priority: int
    """Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5."""
    sharedPrivateLinkResource: Dict[str, object]
    """The properties of the private link resource for private origin."""
    weight: int
    """Weight of the origin in given origin group for load balancing. Must be between 1 and 1000."""


class OriginOutputs(TypedDict, total=False):
    """Outputs for Origin"""
    name: Output[Literal['string']]
    """The name of the origin."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the origin was created in."""
    resourceId: Output[Literal['string']]
    """The resource id of the origin."""


class OriginBicep(Module):
    outputs: OriginOutputs

