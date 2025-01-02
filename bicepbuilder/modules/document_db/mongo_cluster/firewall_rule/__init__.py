from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class FirewallRule(TypedDict, total=False):
    """"""
    endIpAddress: Required[str]
    """The end IP address of the Azure Cosmos DB MongoDB vCore cluster firewall rule. Must be IPv4 format."""
    name: Required[str]
    """The name of the firewall rule."""
    startIpAddress: Required[str]
    """The start IP address of the Azure Cosmos DB MongoDB vCore cluster firewall rule. Must be IPv4 format."""


class FirewallRuleOutputs(TypedDict, total=False):
    """Outputs for FirewallRule"""
    name: Output[Literal['string']]
    """The name of the firewall rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Azure Cosmos DB MongoDB vCore cluster was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the firewall rule."""


class FirewallRuleBicep(Module):
    outputs: FirewallRuleOutputs

