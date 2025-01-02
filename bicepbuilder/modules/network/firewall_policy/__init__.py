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

if TYPE_CHECKING:
    from .rule_collection_group import RuleCollectionGroup


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    userAssignedResourceIds: Required[List[object]]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[str]
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


class NetworkFirewallPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Firewall Policy."""
    allowSqlRedirect: bool
    """A flag to indicate if SQL Redirect traffic filtering is enabled. Turning on the flag requires no rule using port 11000-11999."""
    autoLearnPrivateRanges: Literal['Disabled', 'Enabled']
    """The operation mode for automatically learning private ranges to not be SNAT."""
    basePolicyResourceId: str
    """Resource ID of the base policy."""
    bypassTrafficSettings: List[object]
    """List of rules for traffic to bypass."""
    certificateName: str
    """Name of the CA certificate."""
    defaultWorkspaceId: str
    """Default Log Analytics Resource ID for Firewall Policy Insights."""
    enableProxy: bool
    """Enable DNS Proxy on Firewalls attached to the Firewall Policy."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    fqdns: List[object]
    """List of FQDNs for the ThreatIntel Allowlist."""
    insightsIsEnabled: bool
    """A flag to indicate if the insights are enabled on the policy."""
    ipAddresses: List[object]
    """List of IP addresses for the ThreatIntel Allowlist."""
    keyVaultSecretId: str
    """Secret ID of (base-64 encoded unencrypted PFX) Secret or Certificate object stored in KeyVault."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    mode: Literal['Alert', 'Deny', 'Off']
    """The configuring of intrusion detection."""
    privateRanges: List[object]
    """List of private IP addresses/IP address ranges to not be SNAT."""
    retentionDays: int
    """Number of days the insights should be enabled on the policy."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    ruleCollectionGroups: List['RuleCollectionGroup']
    """Rule collection groups."""
    servers: List[object]
    """List of Custom DNS Servers."""
    signatureOverrides: List[object]
    """List of specific signatures states."""
    tags: Dict[str, object]
    """Tags of the Firewall policy resource."""
    threatIntelMode: Literal['Alert', 'Deny', 'Off']
    """The operation mode for Threat Intel."""
    tier: Literal['Basic', 'Premium', 'Standard']
    """Tier of Firewall Policy."""
    workspaces: List[object]
    """List of workspaces for Firewall Policy Insights."""


class NetworkFirewallPolicyOutputs(TypedDict, total=False):
    """Outputs for NetworkFirewallPolicy"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed firewall policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed firewall policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed firewall policy."""


class NetworkFirewallPolicyBicep(Module):
    outputs: NetworkFirewallPolicyOutputs


def network_firewall_policy(
        bicep: IO[str],
        params: NetworkFirewallPolicy,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkFirewallPolicyBicep:
    symbol = "network_firewall_policy_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/firewall-policy:{tag}' = {{\n")
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
    output = NetworkFirewallPolicyBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
