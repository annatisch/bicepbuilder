from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class NetworkRuleSet(TypedDict, total=False):
    """"""
    defaultAction: Literal['Allow', 'Deny']
    """Default Action for Network Rule Set. Default is "Allow". It will not be set if publicNetworkAccess is "Disabled". Otherwise, it will be set to "Deny" if ipRules or virtualNetworkRules are being used."""
    ipRules: List[object]
    """An array of objects for the public IP ranges you want to allow via the Event Hub Namespace firewall. Supports IPv4 address or CIDR. It will not be set if publicNetworkAccess is "Disabled". Otherwise, when used, defaultAction will be set to "Deny"."""
    networkRuleSetName: str
    """The name of the network ruleset."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """This determines if traffic is allowed over public network. Default is "Enabled". If set to "Disabled", traffic to this namespace will be restricted over Private Endpoints only and network rules will not be applied."""
    trustedServiceAccessEnabled: bool
    """Value that indicates whether Trusted Service Access is enabled or not."""
    virtualNetworkRules: List[object]
    """An array of subnet resource ID objects that this Event Hub Namespace is exposed to via Service Endpoints. You can enable the """


class NetworkRuleSetOutputs(TypedDict, total=False):
    """Outputs for NetworkRuleSet"""
    name: Output[Literal['string']]
    """The name of the network rule set."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the network rule set was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the network rule set."""


class NetworkRuleSetModule(Module):
    outputs: NetworkRuleSetOutputs
