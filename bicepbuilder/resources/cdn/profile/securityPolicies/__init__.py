from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Domain(TypedDict, total=False):
    """List of domain resource id to associate with this resource."""
    id: Required[str]
    """ResourceID to domain that will be associated."""


class Association(TypedDict, total=False):
    """Waf associations (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/securitypolicies?pivots=deployment-language-bicep#securitypolicywebapplicationfirewallassociation for details)."""
    domains: Required[List['Domain']]
    """List of domain resource id to associate with this resource."""
    patternsToMatch: Required[List[object]]
    """List of patterns to match with this association."""


class Securitypolicy(TypedDict, total=False):
    """"""
    associations: Required[List['Association']]
    """Waf associations (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/securitypolicies?pivots=deployment-language-bicep#securitypolicywebapplicationfirewallassociation for details)."""
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


class SecuritypolicyModule(Module):
    outputs: SecuritypolicyOutputs

