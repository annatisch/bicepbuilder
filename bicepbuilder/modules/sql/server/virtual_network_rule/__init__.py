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


class VirtualNetworkRuleBicep(Module):
    outputs: VirtualNetworkRuleOutputs

