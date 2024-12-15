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


class Module(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Automation Account module."""
    uri: Required[str]
    """Module package URI, e.g. https://www.powershellgallery.com/api/v2/package."""
    location: str
    """Location for all resources."""
    tags: Dict[str, object]
    """Tags of the Automation Account resource."""
    version: str
    """Module version or specify latest to get the latest version."""


class ModuleOutputs(TypedDict, total=False):
    """Outputs for Module"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed module."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed module."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed module."""


class ModuleBicep(Module):
    outputs: ModuleOutputs

