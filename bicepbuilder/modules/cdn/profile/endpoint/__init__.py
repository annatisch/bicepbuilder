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


class Endpoint(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the endpoint under the profile which is unique globally."""
    properties: Required[Dict[str, object]]
    """Endpoint properties (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/endpoints?pivots=deployment-language-bicep#endpointproperties for details)."""
    location: str
    """Resource location."""
    tags: Dict[str, object]
    """Endpoint tags."""


class EndpointOutputs(TypedDict, total=False):
    """Outputs for Endpoint"""
    endpointProperties: Output[Literal['object']]
    """The properties of the endpoint."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the endpoint was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the endpoint."""
    uri: Output[Literal['string']]
    """The uri of the endpoint."""


class EndpointBicep(Module):
    outputs: EndpointOutputs

