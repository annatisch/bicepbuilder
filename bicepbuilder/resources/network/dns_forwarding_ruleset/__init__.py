from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class TargetDnsServer(TypedDict, total=False):
    """The target DNS servers to forward to."""
    ipAddress: Required[str]
    """The IP address of the target DNS server."""
    port: Required[int]
    """The port of the target DNS server."""


class ForwardingRule(TypedDict, total=False):
    """Array of forwarding rules."""
    domainName: Required[str]
    """The domain name to forward."""
    name: Required[str]
    """The name of the forwarding rule."""
    targetDnsServers: Required[List['TargetDnsServer']]
    """The target DNS servers to forward to."""
    forwardingRuleState: Literal['Disabled', 'Enabled']
    """The state of the forwarding rule."""
    metadata: str
    """Metadata attached to the forwarding rule."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator']]]
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


class VirtualNetworkLink(TypedDict, total=False):
    """Array of virtual network links."""
    virtualNetworkResourceId: Required[str]
    """The resource ID of the virtual network to link."""
    name: str
    """The name of the virtual network link."""


class NetworkDnsForwardingRuleset(TypedDict, total=False):
    """"""
    dnsForwardingRulesetOutboundEndpointResourceIds: Required[List[object]]
    """The reference to the DNS resolver outbound endpoints that are used to route DNS queries matching the forwarding rules in the ruleset to the target DNS servers."""
    name: Required[str]
    """Name of the DNS Forwarding Ruleset."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    forwardingRules: List['ForwardingRule']
    """Array of forwarding rules."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualNetworkLinks: List['VirtualNetworkLink']
    """Array of virtual network links."""


class NetworkDnsForwardingRulesetOutputs(TypedDict, total=False):
    """Outputs for NetworkDnsForwardingRuleset"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the DNS Forwarding Ruleset."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the DNS Forwarding Ruleset was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the DNS Forwarding Ruleset."""


class NetworkDnsForwardingRulesetModule(Module):
    outputs: NetworkDnsForwardingRulesetOutputs

