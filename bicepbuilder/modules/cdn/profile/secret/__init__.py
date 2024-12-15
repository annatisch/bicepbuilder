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


class Secret(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the secrect."""
    secretSourceResourceId: str
    """The resource ID of the secret source. Required if the """
    secretVersion: str
    """The version of the secret."""
    subjectAlternativeNames: List[object]
    """The subject alternative names of the secrect."""
    type: Literal['AzureFirstPartyManagedCertificate', 'CustomerCertificate', 'ManagedCertificate', 'UrlSigningKey']
    """The type of the secrect."""
    useLatestVersion: bool
    """Indicates whether to use the latest version of the secrect."""


class SecretOutputs(TypedDict, total=False):
    """Outputs for Secret"""
    name: Output[Literal['string']]
    """The name of the secrect."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the secret was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the secrect."""


class SecretBicep(Module):
    outputs: SecretOutputs

