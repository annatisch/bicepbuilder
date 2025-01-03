from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class DdosProtectionPlan(TypedDict, total=False):
    """The DDoS protection plan associated with the public IP address."""
    id: Required[str]
    """The resource ID of the DDOS protection plan associated with the public IP address."""


class DdosSetting(TypedDict, total=False):
    """The DDoS protection plan configuration associated with the public IP address."""
    protectionMode: Required[Literal['Enabled']]
    """The DDoS protection policy customizations."""
    ddosProtectionPlan: 'DdosProtectionPlan'
    """The DDoS protection plan associated with the public IP address."""


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class MetricCategory(TypedDict, total=False):
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    category: Required[str]
    """Name of a Diagnostic Metric category for a resource type this setting is applied to. Set to """
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
    metricCategories: List['MetricCategory']
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    name: str
    """The name of the diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


class DnsSetting(TypedDict, total=False):
    """The DNS settings of the public IP address."""
    domainNameLabel: Required[str]
    """The domain name label. The concatenation of the domain name label and the regionalized DNS zone make up the fully qualified domain name associated with the public IP address. If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system."""
    domainNameLabelScope: Required[Literal['', 'NoReuse', 'ResourceGroupReuse', 'SubscriptionReuse', 'TenantReuse']]
    """The domain name label scope. If a domain name label and a domain name label scope are specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system with a hashed value includes in FQDN."""
    fqdn: str
    """The Fully Qualified Domain Name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone."""
    reverseFqdn: str
    """The reverse FQDN. A user-visible, fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN."""


class IpTag(TypedDict, total=False):
    """The list of tags associated with the public IP address."""
    ipTagType: Required[str]
    """The IP tag type."""
    tag: Required[str]
    """The IP tag."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator']]]
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


class NetworkPublicIpAddress(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Public IP Address."""
    ddosSettings: 'DdosSetting'
    """The DDoS protection plan configuration associated with the public IP address."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    dnsSettings: 'DnsSetting'
    """The DNS settings of the public IP address."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    idleTimeoutInMinutes: int
    """The idle timeout of the public IP address."""
    ipTags: List['IpTag']
    """The list of tags associated with the public IP address."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    publicIPAddressVersion: Literal['IPv4', 'IPv6']
    """IP address version."""
    publicIPAllocationMethod: Literal['Dynamic', 'Static']
    """The public IP address allocation method."""
    publicIpPrefixResourceId: str
    """Resource ID of the Public IP Prefix object. This is only needed if you want your Public IPs created in a PIP Prefix."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    skuName: Literal['Basic', 'Standard']
    """Name of a public IP address SKU."""
    skuTier: Literal['Global', 'Regional']
    """Tier of a public IP address SKU."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zones: Literal[1, 2, 3]
    """A list of availability zones denoting the IP allocated for the resource needs to come from."""


class NetworkPublicIpAddressOutputs(TypedDict, total=False):
    """Outputs for NetworkPublicIpAddress"""
    ipAddress: Output[Literal['string']]
    """The public IP address of the public IP address resource."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the public IP address."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the public IP address was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the public IP address."""


class NetworkPublicIpAddressModule(Module):
    outputs: NetworkPublicIpAddressOutputs

