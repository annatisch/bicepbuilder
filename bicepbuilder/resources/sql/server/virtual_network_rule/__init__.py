from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class VirtualNetworkRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Server Virtual Network Rule."""
    virtualNetworkSubnetId: Required[str]
    """The resource ID of the virtual network subnet."""
    ignoreMissingVnetServiceEndpoint: bool
    """Allow creating a firewall rule before the virtual network has vnet service endpoint enabled."""


class VirtualNetworkRuleOutputs(TypedDict, total=False):
    """Outputs for VirtualNetworkRule"""
    name: Output[Literal['string']]
    """The name of the deployed virtual network rule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed virtual network rule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed virtual network rule."""


class VirtualNetworkRuleModule(Module):
    outputs: VirtualNetworkRuleOutputs

