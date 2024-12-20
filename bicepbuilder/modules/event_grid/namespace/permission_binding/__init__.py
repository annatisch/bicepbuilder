from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class PermissionBinding(TypedDict, total=False):
    """"""
    clientGroupName: Required[str]
    """The name of the client group resource that the permission is bound to. The client group needs to be a resource under the same namespace the permission binding is a part of."""
    name: Required[str]
    """Name of the Permission Binding."""
    permission: Required[Literal['Publisher', 'Subscriber']]
    """The allowed permission."""
    topicSpaceName: Required[str]
    """The name of the Topic Space resource that the permission is bound to. The Topic space needs to be a resource under the same namespace the permission binding is a part of."""
    description: str
    """Description of the Permission Binding."""


class PermissionBindingOutputs(TypedDict, total=False):
    """Outputs for PermissionBinding"""
    name: Output[Literal['string']]
    """The name of the Permission Binding."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Permission Binding was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Permission Binding."""


class PermissionBindingBicep(Module):
    outputs: PermissionBindingOutputs

