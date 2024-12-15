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


class FirewallRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Server Firewall Rule."""
    endIpAddress: str
    """The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress. Use value '0.0.0.0' for all Azure-internal IP addresses."""
    startIpAddress: str
    """The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' for all Azure-internal IP addresses."""


class FirewallRuleOutputs(TypedDict, total=False):
    """Outputs for FirewallRule"""
    name: Output[Literal['string']]
    """The name of the deployed firewall rule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed firewall rule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed firewall rule."""


class FirewallRuleBicep(Module):
    outputs: FirewallRuleOutputs

