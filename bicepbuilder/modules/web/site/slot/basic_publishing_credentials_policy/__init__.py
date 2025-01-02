from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class BasicPublishingCredentialsPolicy(TypedDict, total=False):
    """"""
    name: Required[Literal['ftp', 'scm']]
    """The name of the resource."""
    allow: bool
    """Set to true to enable or false to disable a publishing method."""
    location: str
    """Location for all Resources."""


class BasicPublishingCredentialsPolicyOutputs(TypedDict, total=False):
    """Outputs for BasicPublishingCredentialsPolicy"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the basic publishing credential policy."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the basic publishing credential policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the basic publishing credential policy."""


class BasicPublishingCredentialsPolicyBicep(Module):
    outputs: BasicPublishingCredentialsPolicyOutputs

