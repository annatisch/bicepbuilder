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


class ScopeConnection(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the scope connection."""
    resourceId: Required[str]
    """Enter the subscription or management group resource ID that you want to add to this network manager's scope."""
    tenantId: Required[str]
    """Tenant ID of the subscription or management group that you want to manage."""
    description: str
    """A description of the scope connection."""


class ScopeConnectionOutputs(TypedDict, total=False):
    """Outputs for ScopeConnection"""
    name: Output[Literal['string']]
    """The name of the deployed scope connection."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the scope connection was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed scope connection."""


class ScopeConnectionBicep(Module):
    outputs: ScopeConnectionOutputs

