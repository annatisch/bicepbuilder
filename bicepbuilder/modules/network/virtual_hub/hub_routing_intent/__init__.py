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


class HubRoutingIntent(TypedDict, total=False):
    """"""
    azureFirewallResourceId: Required[str]
    """Hub firewall Resource ID."""
    internetToFirewall: Required[bool]
    """Configures Routing Intent to Forward Internet traffic to the firewall (0.0.0.0/0)."""
    privateToFirewall: Required[bool]
    """Configures Routing Intent to forward Private traffic to the firewall (RFC1918)."""
    virtualHubName: Required[str]
    """Name of the Virtual Hub."""


class HubRoutingIntentOutputs(TypedDict, total=False):
    """Outputs for HubRoutingIntent"""
    name: Output[Literal['string']]
    """The name of the Routing Intent configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the Routing Intent configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Routing Intent configuration."""


class HubRoutingIntentBicep(Module):
    outputs: HubRoutingIntentOutputs

