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


class NatRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the NAT rule."""
    externalMappings: List[object]
    """An address prefix range of destination IPs on the outside network that source IPs will be mapped to. In other words, your post-NAT address prefix range."""
    internalMappings: List[object]
    """An address prefix range of source IPs on the inside network that will be mapped to a set of external IPs. In other words, your pre-NAT address prefix range."""
    ipConfigurationId: str
    """A NAT rule must be configured to a specific VPN Gateway instance. This is applicable to Dynamic NAT only. Static NAT rules are automatically applied to both VPN Gateway instances."""
    mode: Literal['EgressSnat', 'IngressSnat']
    """The type of NAT rule for VPN NAT. IngressSnat mode (also known as Ingress Source NAT) is applicable to traffic entering the Azure hub's site-to-site VPN gateway. EgressSnat mode (also known as Egress Source NAT) is applicable to traffic leaving the Azure hub's Site-to-site VPN gateway."""
    type: Literal['Dynamic', 'Static']
    """The type of NAT rule for VPN NAT. Static one-to-one NAT establishes a one-to-one relationship between an internal address and an external address while Dynamic NAT assigns an IP and port based on availability."""


class NatRuleOutputs(TypedDict, total=False):
    """Outputs for NatRule"""
    name: Output[Literal['string']]
    """The name of the NAT rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the NAT rule was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the NAT rule."""


class NatRuleBicep(Module):
    outputs: NatRuleOutputs

