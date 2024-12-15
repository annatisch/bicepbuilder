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


class Administrator(TypedDict, total=False):
    """"""
    administratorType: Required[str]
    """Workspace active directory administrator type."""
    login: Required[str]
    """Login of the workspace active directory administrator."""
    sid: Required[str]
    """Object ID of the workspace active directory administrator."""
    tenantId: str
    """Tenant ID of the workspace active directory administrator."""


class AdministratorOutputs(TypedDict, total=False):
    """Outputs for Administrator"""
    name: Output[Literal['string']]
    """The name of the deployed administrator."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed administrator."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed administrator."""


class AdministratorBicep(Module):
    outputs: AdministratorOutputs

