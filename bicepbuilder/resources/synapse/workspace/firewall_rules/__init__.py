from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class FirewallRule(TypedDict, total=False):
    """"""
    endIpAddress: Required[str]
    """The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress."""
    name: Required[str]
    """The name of the firewall rule."""
    startIpAddress: Required[str]
    """The start IP address of the firewall rule. Must be IPv4 format."""


class FirewallRuleOutputs(TypedDict, total=False):
    """Outputs for FirewallRule"""
    name: Output[Literal['string']]
    """The name of the deployed firewall rule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed firewall rule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed firewall rule."""


class FirewallRuleModule(Module):
    outputs: FirewallRuleOutputs

