from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConfigurationCustomdnssuffix(TypedDict, total=False):
    """"""
    certificateUrl: Required[str]
    """The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix."""
    dnsSuffix: Required[str]
    """Enable the default custom domain suffix to use for all sites deployed on the ASE."""
    keyVaultReferenceIdentity: Required[str]
    """The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available."""


class ConfigurationCustomdnssuffixOutputs(TypedDict, total=False):
    """Outputs for ConfigurationCustomdnssuffix"""
    name: Output[Literal['string']]
    """The name of the configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed configuration."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed configuration."""


class ConfigurationCustomdnssuffixModule(Module):
    outputs: ConfigurationCustomdnssuffixOutputs

