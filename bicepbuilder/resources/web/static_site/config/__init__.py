from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Config(TypedDict, total=False):
    """"""
    kind: Required[Literal['appsettings', 'functionappsettings']]
    """Type of settings to apply."""
    properties: Required[Dict[str, object]]
    """App settings."""


class ConfigOutputs(TypedDict, total=False):
    """Outputs for Config"""
    name: Output[Literal['string']]
    """The name of the config."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the config was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the config."""


class ConfigModule(Module):
    outputs: ConfigOutputs

