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


class NamedValue(TypedDict, total=False):
    """"""
    displayName: Required[str]
    """Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters."""
    name: Required[str]
    """Named value Name."""
    keyVault: Dict[str, object]
    """KeyVault location details of the namedValue."""
    secret: bool
    """Determines whether the value is a secret and should be encrypted or not. Default value is false."""
    tags: List[object]
    """Tags that when provided can be used to filter the NamedValue list. - string."""
    value: str
    """Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value."""


class NamedValueOutputs(TypedDict, total=False):
    """Outputs for NamedValue"""
    name: Output[Literal['string']]
    """The name of the named value."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the named value was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the named value."""


class NamedValueBicep(Module):
    outputs: NamedValueOutputs

