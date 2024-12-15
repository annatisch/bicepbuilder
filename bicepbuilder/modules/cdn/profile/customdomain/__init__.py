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


class Customdomain(TypedDict, total=False):
    """"""
    certificateType: Required[Literal['AzureFirstPartyManagedCertificate', 'CustomerCertificate', 'ManagedCertificate']]
    """The type of the certificate used for secure delivery."""
    hostName: Required[str]
    """The host name of the domain. Must be a domain name."""
    name: Required[str]
    """The name of the custom domain."""
    profileName: Required[str]
    """The name of the CDN profile."""
    extendedProperties: Dict[str, object]
    """Key-Value pair representing migration properties for domains."""
    minimumTlsVersion: Literal['TLS10', 'TLS12']
    """The minimum TLS version required for the custom domain. Default value: TLS12."""
    preValidatedCustomDomainResourceId: str
    """Resource reference to the Azure resource where custom domain ownership was prevalidated."""
    secretName: str
    """The name of the secret. ie. subs/rg/profile/secret."""
    azureDnsZoneResourceId: str
    """Resource reference to the Azure DNS zone."""


class CustomdomainOutputs(TypedDict, total=False):
    """Outputs for Customdomain"""
    name: Output[Literal['string']]
    """The name of the custom domain."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the custom domain was created in."""
    resourceId: Output[Literal['string']]
    """The resource id of the custom domain."""


class CustomdomainBicep(Module):
    outputs: CustomdomainOutputs

