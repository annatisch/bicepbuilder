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


class CaCertificate(TypedDict, total=False):
    """"""
    encodedCertificate: Required[str]
    """Base64 encoded PEM (Privacy Enhanced Mail) format certificate data."""
    name: Required[str]
    """Name of the CA certificate."""
    description: str
    """Description for the CA Certificate resource."""


class CaCertificateOutputs(TypedDict, total=False):
    """Outputs for CaCertificate"""
    name: Output[Literal['string']]
    """The name of the CA certificate."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the CA certificate was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the CA certificate."""


class CaCertificateBicep(Module):
    outputs: CaCertificateOutputs

