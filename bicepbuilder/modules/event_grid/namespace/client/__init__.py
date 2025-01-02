from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Client(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Client."""
    clientCertificateAuthenticationAllowedThumbprints: List[object]
    """The list of thumbprints that are allowed during client authentication. Required if the clientCertificateAuthenticationValidationSchema is 'ThumbprintMatch'."""
    attributes: Dict[str, object]
    """Attributes for the client. Supported values are int, bool, string, string[]."""
    authenticationName: str
    """The name presented by the client for authentication. The default value is the name of the resource."""
    clientCertificateAuthenticationValidationSchema: Literal['DnsMatchesAuthenticationName', 'EmailMatchesAuthenticationName', 'IpMatchesAuthenticationName', 'SubjectMatchesAuthenticationName', 'ThumbprintMatch', 'UriMatchesAuthenticationName']
    """The validation scheme used to authenticate the client."""
    description: str
    """Description of the Client resource."""
    state: str
    """Indicates if the client is enabled or not."""


class ClientOutputs(TypedDict, total=False):
    """Outputs for Client"""
    name: Output[Literal['string']]
    """The name of the Client."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Client was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Client."""


class ClientBicep(Module):
    outputs: ClientOutputs

