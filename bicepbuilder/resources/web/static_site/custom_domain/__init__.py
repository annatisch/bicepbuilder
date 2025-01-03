from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class CustomDomain(TypedDict, total=False):
    """"""
    name: Required[str]
    """The custom domain name."""
    validationMethod: str
    """Validation method for adding a custom domain."""


class CustomDomainOutputs(TypedDict, total=False):
    """Outputs for CustomDomain"""
    name: Output[Literal['string']]
    """The name of the static site custom domain."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the static site custom domain was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the static site custom domain."""


class CustomDomainModule(Module):
    outputs: CustomDomainOutputs

