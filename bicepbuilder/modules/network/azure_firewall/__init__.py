from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class ApplicationRuleCollection(TypedDict, total=False):
    """Collection of application rule collections used by Azure Firewall."""
    name: Required[str]
    """Name of the application rule collection."""


class ApplicationRuleCollectionProperties(TypedDict, total=False):
    """Properties of the azure firewall application rule collection."""
    priority: Required[int]
    """Priority of the application rule collection."""


class Action(TypedDict, total=False):
    """The action type of a rule collection."""
    type: Required[Literal['Allow', 'Deny']]
    """The type of action."""


class Rule(TypedDict, total=False):
    """Collection of rules used by a application rule collection."""
    name: Required[str]
    """Name of the application rule."""
    description: str
    """Description of the rule."""
    fqdnTags: List[object]
    """List of FQDN Tags for this rule."""
    sourceAddresses: List[object]
    """List of source IP addresses for this rule."""
    sourceIpGroups: List[object]
    """List of source IpGroups for this rule."""
    targetFqdns: List[object]
    """List of FQDNs for this rule."""


class Protocol(TypedDict, total=False):
    """Array of ApplicationRuleProtocols."""
    protocolType: Required[Literal['Http', 'Https', 'Mssql']]
    """Protocol type."""
    port: int
    """Port number for the protocol."""


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class NatRuleCollection(TypedDict, total=False):
    """Collection of NAT rule collections used by Azure Firewall."""
    name: Required[str]
    """Name of the NAT rule collection."""


class NatRuleCollectionProperties(TypedDict, total=False):
    """Properties of the azure firewall NAT rule collection."""
    priority: Required[int]
    """Priority of the NAT rule collection."""


class Action(TypedDict, total=False):
    """The action type of a NAT rule collection."""
    type: Required[Literal['Dnat', 'Snat']]
    """The type of action."""


class Rule(TypedDict, total=False):
    """Collection of rules used by a NAT rule collection."""
    name: Required[str]
    """Name of the NAT rule."""
    protocols: Required[Literal['Any', 'ICMP', 'TCP', 'UDP']]
    """Array of AzureFirewallNetworkRuleProtocols applicable to this NAT rule."""
    description: str
    """Description of the rule."""
    destinationAddresses: List[object]
    """List of destination IP addresses for this rule. Supports IP ranges, prefixes, and service tags."""
    destinationPorts: List[object]
    """List of destination ports."""
    sourceAddresses: List[object]
    """List of source IP addresses for this rule."""
    sourceIpGroups: List[object]
    """List of source IpGroups for this rule."""
    translatedAddress: str
    """The translated address for this NAT rule."""
    translatedFqdn: str
    """The translated FQDN for this NAT rule."""
    translatedPort: str
    """The translated port for this NAT rule."""


class NetworkRuleCollection(TypedDict, total=False):
    """Collection of network rule collections used by Azure Firewall."""
    name: Required[str]
    """Name of the network rule collection."""


class NetworkRuleCollectionProperties(TypedDict, total=False):
    """Properties of the azure firewall network rule collection."""
    priority: Required[int]
    """Priority of the network rule collection."""


class Action(TypedDict, total=False):
    """The action type of a rule collection."""
    type: Required[Literal['Allow', 'Deny']]
    """The type of action."""


class Rule(TypedDict, total=False):
    """Collection of rules used by a network rule collection."""
    name: Required[str]
    """Name of the network rule."""
    protocols: Required[Literal['Any', 'ICMP', 'TCP', 'UDP']]
    """Array of AzureFirewallNetworkRuleProtocols."""
    description: str
    """Description of the rule."""
    destinationAddresses: List[object]
    """List of destination IP addresses."""
    destinationFqdns: List[object]
    """List of destination FQDNs."""
    destinationIpGroups: List[object]
    """List of destination IP groups for this rule."""
    destinationPorts: List[object]
    """List of destination ports."""
    sourceAddresses: List[object]
    """List of source IP addresses for this rule."""
    sourceIpGroups: List[object]
    """List of source IpGroups for this rule."""


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


class AzureFirewall(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Azure Firewall."""
    hubIPAddresses: Dict[str, object]
    """IP addresses associated with AzureFirewall. Required if """
    virtualHubId: str
    """The virtualHub resource ID to which the firewall belongs. Required if """
    virtualNetworkResourceId: str
    """Shared services Virtual Network resource ID. The virtual network ID containing AzureFirewallSubnet. If a Public IP is not provided, then the Public IP that is created as part of this module will be applied with the subnet provided in this variable. Required if """
    additionalPublicIpConfigurations: List[object]
    """This is to add any additional Public IP configurations on top of the Public IP with subnet IP configuration."""
    azureSkuTier: Literal['Basic', 'Premium', 'Standard']
    """Tier of an Azure Firewall."""
    enableForcedTunneling: bool
    """Enable/Disable forced tunneling."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallPolicyId: str
    """Resource ID of the Firewall Policy that should be attached."""
    location: str
    """Location for all resources."""
    managementIPAddressObject: Dict[str, object]
    """Specifies the properties of the Management Public IP to create and be used by Azure Firewall. If it's not provided and managementIPResourceID is empty, a '-mip' suffix will be appended to the Firewall's name."""
    managementIPResourceID: str
    """The Management Public IP resource ID to associate to the AzureFirewallManagementSubnet. If empty, then the Management Public IP that is created as part of this module will be applied to the AzureFirewallManagementSubnet."""
    publicIPAddressObject: Dict[str, object]
    """Specifies the properties of the Public IP to create and be used by the Firewall, if no existing public IP was provided."""
    publicIPResourceID: str
    """The Public IP resource ID to associate to the AzureFirewallSubnet. If empty, then the Public IP that is created as part of this module will be applied to the AzureFirewallSubnet."""
    tags: Dict[str, object]
    """Tags of the Azure Firewall resource."""
    threatIntelMode: Literal['Alert', 'Deny', 'Off']
    """The operation mode for Threat Intel."""
    zones: List[object]
    """Zone numbers e.g. 1,2,3."""


class AzureFirewallOutputs(TypedDict, total=False):
    """Outputs for AzureFirewall"""
    applicationRuleCollections: Output[Literal['array']]
    """List of Application Rule Collections used by Azure Firewall."""
    ipConfAzureFirewallSubnet: Output[Literal['object']]
    """The Public IP configuration object for the Azure Firewall Subnet."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Azure Firewall."""
    natRuleCollections: Output[Literal['array']]
    """List of NAT rule collections used by Azure Firewall."""
    networkRuleCollections: Output[Literal['array']]
    """List of Network Rule Collections used by Azure Firewall."""
    privateIp: Output[Literal['string']]
    """The private IP of the Azure firewall."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the Azure firewall was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Azure Firewall."""


class AzureFirewallBicep(Module):
    outputs: AzureFirewallOutputs


def azure_firewall(
        bicep: IO[str],
        /,
        *,
        params: AzureFirewall,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/azure-firewall',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AzureFirewallBicep:
    symbol = "azure_firewall_" + generate_suffix()
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
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = AzureFirewallBicep(symbol)
    output.outputs = {
            'applicationRuleCollections': Output(symbol, 'applicationRuleCollections', 'array'),
            'ipConfAzureFirewallSubnet': Output(symbol, 'ipConfAzureFirewallSubnet', 'object'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'natRuleCollections': Output(symbol, 'natRuleCollections', 'array'),
            'networkRuleCollections': Output(symbol, 'networkRuleCollections', 'array'),
            'privateIp': Output(symbol, 'privateIp', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
