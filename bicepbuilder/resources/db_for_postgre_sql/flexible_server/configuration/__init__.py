from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Configuration(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the configuration."""
    source: str
    """Source of the configuration."""
    value: str
    """Value of the configuration."""


class ConfigurationOutputs(TypedDict, total=False):
    """Outputs for Configuration"""
    name: Output[Literal['string']]
    """The name of the deployed configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed configuration."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed configuration."""


class ConfigurationModule(Module):
    outputs: ConfigurationOutputs

