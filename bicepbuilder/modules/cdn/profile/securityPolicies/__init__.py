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


class Association(TypedDict, total=False):
    """Waf associations (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/securitypolicies?pivots=deployment-language-bicep#securitypolicywebapplicationfirewallassociation for details)."""
    patternsToMatch: Required[List[object]]
    """List of patterns to match with this association."""


class Domain(TypedDict, total=False):
    """List of domain resource id to associate with this resource."""
    id: Required[str]
    """ResourceID to domain that will be associated."""


class Securitypolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The resource name."""
    wafPolicyResourceId: Required[str]
    """Resource ID of WAF Policy."""


class SecuritypolicyOutputs(TypedDict, total=False):
    """Outputs for Securitypolicy"""
    name: Output[Literal['string']]
    """The name of the secrect."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the secret was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the secrect."""


class SecuritypolicyBicep(Module):
    outputs: SecuritypolicyOutputs

