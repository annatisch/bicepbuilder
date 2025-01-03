from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class SecurityRuleProperties(TypedDict, total=False):
    """The properties of the security rule."""
    access: Required[Literal['Allow', 'Deny']]
    """Whether network traffic is allowed or denied."""
    direction: Required[Literal['Inbound', 'Outbound']]
    """The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic."""
    priority: Required[int]
    """Required. The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule."""
    protocol: Required[Literal['*', 'Ah', 'Esp', 'Icmp', 'Tcp', 'Udp']]
    """Network protocol this rule applies to."""
    description: str
    """The description of the security rule."""
    destinationAddressPrefix: str
    """Optional. The destination address prefix. CIDR or destination IP range. Asterisk "*" can also be used to match all source IPs. Default tags such as "VirtualNetwork", "AzureLoadBalancer" and "Internet" can also be used."""
    destinationAddressPrefixes: List[object]
    """The destination address prefixes. CIDR or destination IP ranges."""
    destinationApplicationSecurityGroupResourceIds: List[object]
    """The resource IDs of the application security groups specified as destination."""
    destinationPortRange: str
    """The destination port or range. Integer or range between 0 and 65535. Asterisk "*" can also be used to match all ports."""
    destinationPortRanges: List[object]
    """The destination port ranges."""
    sourceAddressPrefix: str
    """The CIDR or source IP range. Asterisk "*" can also be used to match all source IPs. Default tags such as "VirtualNetwork", "AzureLoadBalancer" and "Internet" can also be used. If this is an ingress rule, specifies where network traffic originates from."""
    sourceAddressPrefixes: List[object]
    """The CIDR or source IP ranges."""
    sourceApplicationSecurityGroupResourceIds: List[object]
    """The resource IDs of the application security groups specified as source."""
    sourcePortRange: str
    """The source port or range. Integer or range between 0 and 65535. Asterisk "*" can also be used to match all ports."""
    sourcePortRanges: List[object]
    """The source port ranges."""


class SecurityRule(TypedDict, total=False):
    """Array of Security Rules to deploy to the Network Security Group. When not provided, an NSG including only the built-in roles will be deployed."""
    name: Required[str]
    """The name of the security rule."""
    properties: Required['SecurityRuleProperties']
    """The properties of the security rule."""


class NetworkSecurityGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Network Security Group."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    flushConnection: bool
    """When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation. Network Security Group connection flushing is not available in all regions."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    securityRules: List['SecurityRule']
    """Array of Security Rules to deploy to the Network Security Group. When not provided, an NSG including only the built-in roles will be deployed."""
    tags: Dict[str, object]
    """Tags of the NSG resource."""


class NetworkSecurityGroupOutputs(TypedDict, total=False):
    """Outputs for NetworkSecurityGroup"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the network security group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the network security group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the network security group."""


class NetworkSecurityGroupModule(Module):
    outputs: NetworkSecurityGroupOutputs

