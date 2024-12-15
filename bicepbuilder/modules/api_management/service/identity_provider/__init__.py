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


class IdentityProvider(TypedDict, total=False):
    """"""
    name: Required[str]
    """Identity provider name."""
    clientId: str
    """Client ID of the Application in the external Identity Provider. Required if identity provider is used."""
    clientSecret: str
    """Client secret of the Application in external Identity Provider, used to authenticate login request. Required if identity provider is used."""
    allowedTenants: List[object]
    """List of Allowed Tenants when configuring Azure Active Directory login. - string."""
    authority: str
    """OpenID Connect discovery endpoint hostname for AAD or AAD B2C."""
    clientLibrary: Literal['ADAL', 'MSAL-2']
    """The client library to be used in the developer portal. Only applies to AAD and AAD B2C Identity Provider."""
    passwordResetPolicyName: str
    """Password Reset Policy Name. Only applies to AAD B2C Identity Provider."""
    profileEditingPolicyName: str
    """Profile Editing Policy Name. Only applies to AAD B2C Identity Provider."""
    signInPolicyName: str
    """Signin Policy Name. Only applies to AAD B2C Identity Provider."""
    signInTenant: str
    """The TenantId to use instead of Common when logging into Active Directory."""
    signUpPolicyName: str
    """Signup Policy Name. Only applies to AAD B2C Identity Provider."""
    type: Literal['aad', 'aadB2C', 'facebook', 'google', 'microsoft', 'twitter']
    """Identity Provider Type identifier."""


class IdentityProviderOutputs(TypedDict, total=False):
    """Outputs for IdentityProvider"""
    name: Output[Literal['string']]
    """The name of the API management service identity provider."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service identity provider was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service identity provider."""


class IdentityProviderBicep(Module):
    outputs: IdentityProviderOutputs

