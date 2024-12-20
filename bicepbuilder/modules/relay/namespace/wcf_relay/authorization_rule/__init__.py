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


class AuthorizationRuleBicep(Module):
    outputs: AuthorizationRuleOutputs


def authorization_rule(
        bicep: IO[str],
        /,
        *,
        params: AuthorizationRule,
        scope: Optional[BicepExpression] = None,
        namespace_name: Union[str, BicepExpression],
        wcf_relay_name: Union[str, BicepExpression],
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'relay/namespace/wcf-relay/authorization-rule',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AuthorizationRuleBicep:
    symbol = "authorization_rule_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} '{registry_prefix}/{path}:{tag}' = {{\n")
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
    output = AuthorizationRuleBicep(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
