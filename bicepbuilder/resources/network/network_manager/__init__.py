from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
    Output,
)


class NetworkManagerScope(TypedDict, total=False):
    """Scope of Network Manager. Contains a list of management groups or a list of subscriptions. This defines the boundary of network resources that this Network Manager instance can manage. If using Management Groups, ensure that the "Microsoft.Network" resource provider is registered for those Management Groups prior to deployment. Must contain at least one management group or subscription."""
    managementGroups: List[object]
    """List of fully qualified IDs of management groups to assign to the network manager to manage. Required if """
    subscriptions: List[object]
    """List of fully qualified IDs of Subscriptions to assign to the network manager to manage. Required if """


class StaticMember(TypedDict, total=False):
    """Static Members to create for the network group. Contains virtual networks to add to the network group."""
    name: Required[str]
    """The name of the static member."""
    resourceId: Required[str]
    """Resource ID of the virtual network."""


class NetworkGroup(TypedDict, total=False):
    """Network Groups and static members to create for the network manager. Required if using "connectivityConfigurations" or "securityAdminConfigurations" parameters. A network group is global container that includes a set of virtual network resources from any region. Then, configurations are applied to target the network group, which applies the configuration to all members of the group. The two types are group memberships are static and dynamic memberships. Static membership allows you to explicitly add virtual networks to a group by manually selecting individual virtual networks, and is available as a child module, while dynamic membership is defined through Azure policy. See """
    name: Required[str]
    """The name of the network group."""
    description: str
    """A description of the network group."""
    staticMembers: List['StaticMember']
    """Static Members to create for the network group. Contains virtual networks to add to the network group."""


class AppliesToGroup(TypedDict, total=False):
    """Network Groups for the configuration. A connectivity configuration must be associated to at least one network group."""
    groupConnectivity: Required[Literal['DirectlyConnected', 'None']]
    """Group connectivity type."""
    networkGroupResourceId: Required[str]
    """Resource Id of the network group."""
    isGlobal: bool
    """Flag if global is supported."""
    useHubGateway: bool
    """Flag if use hub gateway."""


class Hub(TypedDict, total=False):
    """The hubs to apply the configuration to."""
    resourceId: Required[str]
    """Resource Id of the hub."""
    resourceType: Required[Literal['Microsoft.Network/virtualNetworks']]
    """Resource type of the hub."""


class ConnectivityConfiguration(TypedDict, total=False):
    """Connectivity Configurations to create for the network manager. Network manager must contain at least one network group in order to define connectivity configurations."""
    appliesToGroups: Required[List['AppliesToGroup']]
    """Network Groups for the configuration. A connectivity configuration must be associated to at least one network group."""
    connectivityTopology: Required[Literal['HubAndSpoke', 'Mesh']]
    """The connectivity topology to apply the configuration to."""
    name: Required[str]
    """The name of the connectivity configuration."""
    deleteExistingPeering: bool
    """Delete existing peering connections."""
    description: str
    """A description of the connectivity configuration."""
    hubs: List['Hub']
    """The hubs to apply the configuration to."""
    isGlobal: bool
    """Is global configuration."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'IPAM Pool Contributor', 'LocalNGFirewallAdministrator role', 'Network Contributor', 'Owner', 'Reader', 'Resource Policy Contributor', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class ScopeConnection(TypedDict, total=False):
    """Scope Connections to create for the network manager. Allows network manager to manage resources from another tenant. Supports management groups or subscriptions from another tenant."""
    name: Required[str]
    """The name of the scope connection."""
    resourceId: Required[str]
    """Enter the subscription or management group resource ID that you want to add to this network manager's scope."""
    tenantId: Required[str]
    """Tenant ID of the subscription or management group that you want to manage."""
    description: str
    """A description of the scope connection."""


class AppliesToGroup(TypedDict, total=False):
    """List of network groups for configuration. An admin rule collection must be associated to at least one network group."""
    networkGroupResourceId: Required[str]
    """The resource ID of the network group."""


class Destination(TypedDict, total=False):
    """The destnations filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""
    addressPrefix: Required[str]
    """Address prefix."""
    addressPrefixType: Required[Literal['IPPrefix', 'ServiceTag']]
    """Address prefix type."""


class Source(TypedDict, total=False):
    """The source filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""
    addressPrefix: Required[str]
    """Address prefix."""
    addressPrefixType: Required[Literal['IPPrefix', 'ServiceTag']]
    """Address prefix type."""


class Rule(TypedDict, total=False):
    """List of rules for the admin rules collection. Security admin rules allows enforcing security policy criteria that matches the conditions set. Warning: A rule collection without rule will cause a deployment configuration for security admin goal state in network manager to fail."""
    access: Required[Literal['Allow', 'AlwaysAllow', 'Deny']]
    """Indicates the access allowed for this particular rule. "Allow" means traffic matching this rule will be allowed. "Deny" means traffic matching this rule will be blocked. "AlwaysAllow" means that traffic matching this rule will be allowed regardless of other rules with lower priority or user-defined NSGs."""
    direction: Required[Literal['Inbound', 'Outbound']]
    """Indicates if the traffic matched against the rule in inbound or outbound."""
    name: Required[str]
    """The name of the rule."""
    priority: Required[int]
    """The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule."""
    protocol: Required[Literal['Ah', 'Any', 'Esp', 'Icmp', 'Tcp', 'Udp']]
    """Network protocol this rule applies to."""
    description: str
    """A description of the rule."""
    destinationPortRanges: List[object]
    """List of destination port ranges. This specifies on which ports traffic will be allowed or denied by this rule. Provide an (*) to allow traffic on any port. Port ranges are between 1-65535."""
    destinations: List['Destination']
    """The destnations filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""
    sourcePortRanges: List[object]
    """List of destination port ranges. This specifies on which ports traffic will be allowed or denied by this rule. Provide an (*) to allow traffic on any port. Port ranges are between 1-65535."""
    sources: List['Source']
    """The source filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""


class RuleCollection(TypedDict, total=False):
    """Rule collections to create for the security admin configuration."""
    appliesToGroups: Required[List['AppliesToGroup']]
    """List of network groups for configuration. An admin rule collection must be associated to at least one network group."""
    name: Required[str]
    """The name of the admin rule collection."""
    description: str
    """A description of the admin rule collection."""
    rules: List['Rule']
    """List of rules for the admin rules collection. Security admin rules allows enforcing security policy criteria that matches the conditions set. Warning: A rule collection without rule will cause a deployment configuration for security admin goal state in network manager to fail."""


class SecurityAdminConfiguration(TypedDict, total=False):
    """Security Admin Configurations, Rule Collections and Rules to create for the network manager. Azure Virtual Network Manager provides two different types of configurations you can deploy across your virtual networks, one of them being a SecurityAdmin configuration. A security admin configuration contains a set of rule collections. Each rule collection contains one or more security admin rules. You then associate the rule collection with the network groups that you want to apply the security admin rules to."""
    applyOnNetworkIntentPolicyBasedServices: Required[Literal['All', 'AllowRulesOnly', 'None']]
    """Apply on network intent policy based services."""
    name: Required[str]
    """The name of the security admin configuration."""
    description: str
    """A description of the security admin configuration."""
    ruleCollections: List['RuleCollection']
    """Rule collections to create for the security admin configuration."""


class NetworkManager(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Network Manager."""
    networkManagerScopeAccesses: Required[Literal['Connectivity', 'SecurityAdmin']]
    """Scope Access. String array containing any of "Connectivity", "SecurityAdmin". The connectivity feature allows you to create network topologies at scale. The security admin feature lets you create high-priority security rules, which take precedence over NSGs."""
    networkManagerScopes: Required['NetworkManagerScope']
    """Scope of Network Manager. Contains a list of management groups or a list of subscriptions. This defines the boundary of network resources that this Network Manager instance can manage. If using Management Groups, ensure that the "Microsoft.Network" resource provider is registered for those Management Groups prior to deployment. Must contain at least one management group or subscription."""
    networkGroups: List['NetworkGroup']
    """Network Groups and static members to create for the network manager. Required if using "connectivityConfigurations" or "securityAdminConfigurations" parameters. A network group is global container that includes a set of virtual network resources from any region. Then, configurations are applied to target the network group, which applies the configuration to all members of the group. The two types are group memberships are static and dynamic memberships. Static membership allows you to explicitly add virtual networks to a group by manually selecting individual virtual networks, and is available as a child module, while dynamic membership is defined through Azure policy. See """
    connectivityConfigurations: List['ConnectivityConfiguration']
    """Connectivity Configurations to create for the network manager. Network manager must contain at least one network group in order to define connectivity configurations."""
    description: str
    """A description of the Network Manager."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    scopeConnections: List['ScopeConnection']
    """Scope Connections to create for the network manager. Allows network manager to manage resources from another tenant. Supports management groups or subscriptions from another tenant."""
    securityAdminConfigurations: List['SecurityAdminConfiguration']
    """Security Admin Configurations, Rule Collections and Rules to create for the network manager. Azure Virtual Network Manager provides two different types of configurations you can deploy across your virtual networks, one of them being a SecurityAdmin configuration. A security admin configuration contains a set of rule collections. Each rule collection contains one or more security admin rules. You then associate the rule collection with the network groups that you want to apply the security admin rules to."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NetworkManagerOutputs(TypedDict, total=False):
    """Outputs for NetworkManager"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the network manager."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the network manager was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the network manager."""


class NetworkManagerModule(Module):
    outputs: NetworkManagerOutputs


def _network_manager(
        bicep: IO[str],
        params: NetworkManager,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkManagerModule:
    symbol = "network_manager_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/network-manager:{tag}' = {{\n")
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
    output = NetworkManagerModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
