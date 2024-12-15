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
    objectId: Required[str]
    """The objectId of the Active Directory administrator."""
    principalName: Required[str]
    """Active Directory administrator principal name."""
    principalType: Required[Literal['Group', 'ServicePrincipal', 'Unknown', 'User']]
    """The principal type used to represent the type of Active Directory Administrator."""
    tenantId: str
    """The tenantId of the Active Directory administrator."""


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

