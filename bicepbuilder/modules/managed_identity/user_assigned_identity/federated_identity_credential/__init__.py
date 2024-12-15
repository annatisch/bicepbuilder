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


class FederatedIdentityCredential(TypedDict, total=False):
    """"""
    audiences: Required[List[object]]
    """The list of audiences that can appear in the issued token. Should be set to api://AzureADTokenExchange for Azure AD. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Azure AD in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your IdP to serve as the audience of this token."""
    issuer: Required[str]
    """The URL of the issuer to be trusted. Must match the issuer claim of the external token being exchanged."""
    name: Required[str]
    """The name of the secret."""
    subject: Required[str]
    """The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format, as each IdP uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Azure AD."""


class FederatedIdentityCredentialOutputs(TypedDict, total=False):
    """Outputs for FederatedIdentityCredential"""
    name: Output[Literal['string']]
    """The name of the federated identity credential."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the federated identity credential was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the federated identity credential."""


class FederatedIdentityCredentialBicep(Module):
    outputs: FederatedIdentityCredentialOutputs

