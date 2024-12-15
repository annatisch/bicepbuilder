from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class ConfigBicep(Module):
    outputs: ConfigOutputs

