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


class SharedPrivateLinkResource(TypedDict, total=False):
    """"""
    groupId: Required[str]
    """The group ID from the provider of resource the shared private link resource is for."""
    name: Required[str]
    """The name of the shared private link resource managed by the Azure Cognitive Search service within the specified resource group."""
    privateLinkResourceId: Required[str]
    """The resource ID of the resource the shared private link resource is for."""
    requestMessage: Required[str]
    """The request message for requesting approval of the shared private link resource."""
    resourceRegion: str
    """Can be used to specify the Azure Resource Manager location of the resource to which a shared private link is to be created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service)."""


class SharedPrivateLinkResourceOutputs(TypedDict, total=False):
    """Outputs for SharedPrivateLinkResource"""
    name: Output[Literal['string']]
    """The name of the shared private link resource."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the shared private link resource was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the shared private link resource."""


class SharedPrivateLinkResourceBicep(Module):
    outputs: SharedPrivateLinkResourceOutputs

