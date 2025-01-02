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


class Policy(TypedDict, total=False):
    """"""
    value: Required[str]
    """Contents of the Policy as defined by the format."""
    format: Literal['rawxml', 'rawxml-link', 'xml', 'xml-link']
    """Format of the policyContent."""
    name: str
    """The name of the policy."""


class PolicyOutputs(TypedDict, total=False):
    """Outputs for Policy"""
    name: Output[Literal['string']]
    """The name of the API management service policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service policy."""


class PolicyBicep(Module):
    outputs: PolicyOutputs

