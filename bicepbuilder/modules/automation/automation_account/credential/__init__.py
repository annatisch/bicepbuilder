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


class Credential(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Automation Account credential."""
    password: Required[str]
    """Password of the credential."""
    userName: Required[str]
    """The user name associated to the credential."""
    description: str
    """Description of the credential."""


class CredentialOutputs(TypedDict, total=False):
    """Outputs for Credential"""
    name: Output[Literal['string']]
    """The name of the credential associated to the automation account."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed credential."""
    resourceId: Output[Literal['string']]
    """The resource Id of the credential associated to the automation account."""


class CredentialBicep(Module):
    outputs: CredentialOutputs

