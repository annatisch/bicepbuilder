from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConfigWeb(TypedDict, total=False):
    """"""
    appName: Required[str]
    """The name of the parent site resource."""
    apiManagementConfiguration: Dict[str, object]
    """The web settings api management configuration."""


class ConfigWebOutputs(TypedDict, total=False):
    """Outputs for ConfigWeb"""
    name: Output[Literal['string']]
    """The name of the site config."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the site config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the site config."""


class ConfigWebModule(Module):
    outputs: ConfigWebOutputs

