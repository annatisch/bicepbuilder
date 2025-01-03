from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class AuthorizationRule(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the authorization rule."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


class AuthorizationRuleOutputs(TypedDict, total=False):
    """Outputs for AuthorizationRule"""
    name: Output[Literal['string']]
    """The name of the authorization rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the authorization rule was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the authorization rule."""


class AuthorizationRuleModule(Module):
    outputs: AuthorizationRuleOutputs


def _authorization_rule(
        bicep: IO[str],
        params: AuthorizationRule,
        /,
        *,
        namespace_name: Union[str, BicepExpression],
        wcf_relay_name: Union[str, BicepExpression],
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AuthorizationRuleModule:
    symbol = "authorization_rule_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/relay/namespace/wcf-relay/authorization-rule:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    file_handle.write(f"    {resolve_key('namespaceName')}: {resolve_value(namespace_name)}\n")file_handle.write(f"    {resolve_key('wcfRelayName')}: {resolve_value(wcf_relay_name)}\n")
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = AuthorizationRuleModule(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
