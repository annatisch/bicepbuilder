from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class ManagedPrivateEndpoint(TypedDict, total=False):
    """"""
    fqdns: Required[List[object]]
    """Fully qualified domain names."""
    groupId: Required[str]
    """The groupId to which the managed private endpoint is created."""
    managedVirtualNetworkName: Required[str]
    """The name of the parent managed virtual network."""
    name: Required[str]
    """The managed private endpoint resource name."""
    privateLinkResourceId: Required[str]
    """The ARM resource ID of the resource to which the managed private endpoint is created."""


class ManagedPrivateEndpointOutputs(TypedDict, total=False):
    """Outputs for ManagedPrivateEndpoint"""
    name: Output[Literal['string']]
    """The name of the deployed managed private endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed managed private endpoint."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed managed private endpoint."""


class ManagedPrivateEndpointBicep(Module):
    outputs: ManagedPrivateEndpointOutputs

