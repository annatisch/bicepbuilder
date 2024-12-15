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


class AuthorizationServer(TypedDict, total=False):
    """"""
    authorizationEndpoint: Required[str]
    """OAuth authorization endpoint. See """
    clientId: Required[str]
    """Client or app ID registered with this authorization server."""
    clientSecret: Required[str]
    """Client or app secret registered with this authorization server. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value."""
    displayName: Required[str]
    """API Management Service Authorization Servers name. Must be 1 to 50 characters long."""
    grantTypes: Required[List[object]]
    """Form of an authorization grant, which the client uses to request the access token. - authorizationCode, implicit, resourceOwnerPassword, clientCredentials."""
    name: Required[str]
    """Identifier of the authorization server."""
    authorizationMethods: List[object]
    """HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional. - HEAD, OPTIONS, TRACE, GET, POST, PUT, PATCH, DELETE."""
    bearerTokenSendingMethods: List[object]
    """Specifies the mechanism by which access token is passed to the API. - authorizationHeader or query."""
    clientAuthenticationMethod: List[object]
    """Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format. - Basic or Body."""
    clientRegistrationEndpoint: str
    """Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced."""
    defaultScope: str
    """Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values."""
    resourceOwnerPassword: str
    """Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password."""
    resourceOwnerUsername: str
    """Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username."""
    serverDescription: str
    """Description of the authorization server. Can contain HTML formatting tags."""
    supportState: bool
    """If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security."""
    tokenBodyParameters: List[object]
    """Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}. - TokenBodyParameterContract object."""
    tokenEndpoint: str
    """OAuth token endpoint. Contains absolute URI to entity being referenced."""


class AuthorizationServerOutputs(TypedDict, total=False):
    """Outputs for AuthorizationServer"""
    name: Output[Literal['string']]
    """The name of the API management service authorization server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service authorization server was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service authorization server."""


class AuthorizationServerBicep(Module):
    outputs: AuthorizationServerOutputs

