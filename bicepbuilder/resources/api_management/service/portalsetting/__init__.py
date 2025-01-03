from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
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


class PortalsettingModule(Module):
    outputs: PortalsettingOutputs

