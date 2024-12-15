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


class AuthCredential(TypedDict, total=False):
    """List of authentication credentials stored for an upstream. Usually consists of a primary and an optional secondary credential."""
    name: Required[str]
    """The name of the credential."""
    passwordSecretIdentifier: Required[str]
    """KeyVault Secret URI for accessing the password."""
    usernameSecretIdentifier: Required[str]
    """KeyVault Secret URI for accessing the username."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""


class CredentialSet(TypedDict, total=False):
    """"""
    loginServer: Required[str]
    """The credentials are stored for this upstream or login server."""
    name: Required[str]
    """The name of the credential set."""


class CredentialSetOutputs(TypedDict, total=False):
    """Outputs for CredentialSet"""
    name: Output[Literal['string']]
    """The Name of the Credential Set."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Credential Set."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Credential Set."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class CredentialSetBicep(Module):
    outputs: CredentialSetOutputs

