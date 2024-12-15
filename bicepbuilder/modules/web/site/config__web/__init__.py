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


class ConfigWebBicep(Module):
    outputs: ConfigWebOutputs

