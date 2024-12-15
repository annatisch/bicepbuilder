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


class Portalsetting(TypedDict, total=False):
    """"""
    name: Required[Literal['delegation', 'signin', 'signup']]
    """Portal setting name."""
    properties: Required[Dict[str, object]]
    """Portal setting properties."""


class PortalsettingOutputs(TypedDict, total=False):
    """Outputs for Portalsetting"""
    name: Output[Literal['string']]
    """The name of the API management service portal setting."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service portal setting was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service portal setting."""


class PortalsettingBicep(Module):
    outputs: PortalsettingOutputs

