from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class NetworkApplicationGatewayWebApplicationFirewallPolicy(TypedDict, total=False):
    """"""
    managedRules: Required[Dict[str, object]]
    """Describes the managedRules structure."""
    name: Required[str]
    """Name of the Application Gateway WAF policy."""
    customRules: List[object]
    """The custom rules inside the policy."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    policySettings: Dict[str, object]
    """The PolicySettings for policy."""
    tags: Dict[str, object]
    """Resource tags."""


class NetworkApplicationGatewayWebApplicationFirewallPolicyOutputs(TypedDict, total=False):
    """Outputs for NetworkApplicationGatewayWebApplicationFirewallPolicy"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the application gateway WAF policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the application gateway WAF policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the application gateway WAF policy."""


class NetworkApplicationGatewayWebApplicationFirewallPolicyModule(Module):
    outputs: NetworkApplicationGatewayWebApplicationFirewallPolicyOutputs

