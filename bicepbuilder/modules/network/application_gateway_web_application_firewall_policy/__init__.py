from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class NetworkApplicationGatewayWebApplicationFirewallPolicyBicep(Module):
    outputs: NetworkApplicationGatewayWebApplicationFirewallPolicyOutputs


def network_application_gateway_web_application_firewall_policy(
        bicep: IO[str],
        params: NetworkApplicationGatewayWebApplicationFirewallPolicy,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkApplicationGatewayWebApplicationFirewallPolicyBicep:
    symbol = "network_application_gateway_web_application_firewall_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/application-gateway-web-application-firewall-policy:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = NetworkApplicationGatewayWebApplicationFirewallPolicyBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
