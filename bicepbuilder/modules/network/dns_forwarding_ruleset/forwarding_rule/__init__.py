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


class ForwardingRule(TypedDict, total=False):
    """"""
    domainName: Required[str]
    """The domain name for the forwarding rule."""
    name: Required[str]
    """Name of the Forwarding Rule."""
    targetDnsServers: Required[List[object]]
    """DNS servers to forward the DNS query to."""
    forwardingRuleState: str
    """The state of forwarding rule."""
    metadata: Dict[str, object]
    """Metadata attached to the forwarding rule."""


class ForwardingRuleOutputs(TypedDict, total=False):
    """Outputs for ForwardingRule"""
    name: Output[Literal['string']]
    """The name of the Forwarding Rule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the Forwarding Rule was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Forwarding Rule."""


class ForwardingRuleBicep(Module):
    outputs: ForwardingRuleOutputs

