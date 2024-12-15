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


class InboundNatRule(TypedDict, total=False):
    """"""
    backendPort: Required[int]
    """The port used for the internal endpoint."""
    frontendIPConfigurationName: Required[str]
    """The name of the frontend IP address to set for the inbound NAT rule."""
    name: Required[str]
    """The name of the inbound NAT rule."""
    frontendPort: int
    """The port for the external endpoint. Port numbers for each rule must be unique within the Load Balancer. Required if FrontendPortRangeStart and FrontendPortRangeEnd are not specified."""
    frontendPortRangeStart: int
    """The port range start for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeEnd. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Required if FrontendPort is not specified."""
    backendAddressPoolName: str
    """Name of the backend address pool."""
    enableFloatingIP: bool
    """Configures a virtual machine's endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. This setting is required when using the SQL AlwaysOn Availability Groups in SQL server. This setting can't be changed after you create the endpoint."""
    enableTcpReset: bool
    """Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP."""
    idleTimeoutInMinutes: int
    """The timeout for the TCP idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to TCP."""
    protocol: Literal['All', 'Tcp', 'Udp']
    """The transport protocol for the endpoint."""
    frontendPortRangeEnd: int
    """The port range end for the external endpoint. This property is used together with BackendAddressPool and FrontendPortRangeStart. Individual inbound NAT rule port mappings will be created for each backend address from BackendAddressPool. Required if FrontendPort is not specified."""


class InboundNatRuleOutputs(TypedDict, total=False):
    """Outputs for InboundNatRule"""
    name: Output[Literal['string']]
    """The name of the inbound NAT rule."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the inbound NAT rule was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the inbound NAT rule."""


class InboundNatRuleBicep(Module):
    outputs: InboundNatRuleOutputs

