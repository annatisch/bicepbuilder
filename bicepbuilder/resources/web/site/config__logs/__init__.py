from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConfigLog(TypedDict, total=False):
    """"""
    appName: Required[str]
    """The name of the parent site resource."""
    logsConfiguration: Dict[str, object]
    """The logs settings configuration."""


class ConfigLogOutputs(TypedDict, total=False):
    """Outputs for ConfigLog"""
    name: Output[Literal['string']]
    """The name of the site config."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the site config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the site config."""


class ConfigLogModule(Module):
    outputs: ConfigLogOutputs

