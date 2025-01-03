from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Rule(TypedDict, total=False):
    """List of rules."""
    action: Required[Literal['Allow', 'Block', 'Log', 'Redirect']]
    """Describes what action to be applied when rule matches."""
    enabledState: Required[Literal['Disabled', 'Enabled']]
    """Describes if the custom rule is in enabled or disabled state."""
    matchConditions: Required[List[object]]
    """List of match conditions. See https://learn.microsoft.com/en-us/azure/templates/microsoft.network/frontdoorwebapplicationfirewallpolicies#matchcondition for details."""
    name: Required[str]
    """Describes the name of the rule."""
    priority: Required[int]
    """Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value."""
    ruleType: Required[Literal['MatchRule', 'RateLimitRule']]
    """Describes type of rule."""
    rateLimitDurationInMinutes: int
    """Time window for resetting the rate limit count. Default is 1 minute."""
    rateLimitThreshold: int
    """Number of allowed requests per client within the time window."""


class CustomRule(TypedDict, total=False):
    """The custom rules inside the policy."""
    rules: List['Rule']
    """List of rules."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedRuleSet(TypedDict, total=False):
    """List of rule sets."""
    ruleSetType: Required[str]
    """Defines the rule set type to use."""
    ruleSetVersion: Required[str]
    """Defines the version of the rule set to use."""
    exclusions: List[object]
    """Describes the exclusions that are applied to all rules in the set."""
    ruleGroupOverrides: List[object]
    """Defines the rule group overrides to apply to the rule set."""
    ruleSetAction: Literal['Block', 'Log', 'Redirect']
    """Defines the rule set action."""


class ManagedRule(TypedDict, total=False):
    """Describes the managedRules structure."""
    managedRuleSets: List['ManagedRuleSet']
    """List of rule sets."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    name: str
    """The name (as GUID) of the role assignment. If not provided, a GUID will be generated."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class NetworkFrontDoorWebApplicationFirewallPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Front Door WAF policy."""
    customRules: 'CustomRule'
    """The custom rules inside the policy."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedRules: 'ManagedRule'
    """Describes the managedRules structure."""
    policySettings: Dict[str, object]
    """The PolicySettings for policy."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    sku: Literal['Premium_AzureFrontDoor', 'Standard_AzureFrontDoor']
    """The pricing tier of the WAF profile."""
    tags: Dict[str, object]
    """Resource tags."""


class NetworkFrontDoorWebApplicationFirewallPolicyOutputs(TypedDict, total=False):
    """Outputs for NetworkFrontDoorWebApplicationFirewallPolicy"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Front Door WAF policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the Front Door WAF policy was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Front Door WAF policy."""


class NetworkFrontDoorWebApplicationFirewallPolicyModule(Module):
    outputs: NetworkFrontDoorWebApplicationFirewallPolicyOutputs

