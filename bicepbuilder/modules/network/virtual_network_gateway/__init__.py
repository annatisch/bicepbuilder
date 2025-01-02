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
    from .nat_rule import NatRule


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


class PublicIpDiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the Public IP."""
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
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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


class NetworkVirtualNetworkGateway(TypedDict, total=False):
    """"""
    clusterSettings: Required[Dict[str, object]]
    """Specifies one of the following four configurations: Active-Active with (clusterMode = activeActiveBgp) or without (clusterMode = activeActiveNoBgp) BGP, Active-Passive with (clusterMode = activePassiveBgp) or without (clusterMode = activePassiveNoBgp) BGP."""
    gatewayType: Required[Literal['ExpressRoute', 'Vpn']]
    """Specifies the gateway type. E.g. VPN, ExpressRoute."""
    name: Required[str]
    """Specifies the Virtual Network Gateway name."""
    skuName: Literal['Basic', 'ErGw1AZ', 'ErGw2AZ', 'ErGw3AZ', 'HighPerformance', 'Standard', 'UltraPerformance', 'VpnGw1', 'VpnGw1AZ', 'VpnGw2', 'VpnGw2AZ', 'VpnGw3', 'VpnGw3AZ', 'VpnGw4', 'VpnGw4AZ', 'VpnGw5', 'VpnGw5AZ']
    """The SKU of the Gateway."""
    vNetResourceId: Required[str]
    """Virtual Network resource ID."""
    allowRemoteVnetTraffic: bool
    """Configure this gateway to accept traffic from other Azure Virtual Networks. This configuration does not support connectivity to Azure Virtual WAN."""
    allowVirtualWanTraffic: bool
    """Configures this gateway to accept traffic from remote Virtual WAN networks."""
    clientRevokedCertThumbprint: str
    """Thumbprint of the revoked certificate. This would revoke VPN client certificates matching this thumbprint from connecting to the VNet."""
    clientRootCertData: str
    """Client root certificate data used to authenticate VPN clients. Cannot be configured if vpnClientAadConfiguration is provided."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableIPSecReplayProtection: bool
    """disableIPSecReplayProtection flag. Used for VPN Gateways."""
    domainNameLabel: List[object]
    """DNS name(s) of the Public IP resource(s). If you enabled Active-Active mode, you need to provide 2 DNS names, if you want to use this feature. A region specific suffix will be appended to it, e.g.: your-DNS-name.westeurope.cloudapp.azure.com."""
    enableBgpRouteTranslationForNat: bool
    """EnableBgpRouteTranslationForNat flag. Can only be used when "natRules" are enabled on the Virtual Network Gateway."""
    enableDnsForwarding: bool
    """Whether DNS forwarding is enabled or not and is only supported for Express Route Gateways. The DNS forwarding feature flag must be enabled on the current subscription."""
    enablePrivateIpAddress: bool
    """Whether private IP needs to be enabled on this gateway for connections or not. Used for configuring a Site-to-Site VPN connection over ExpressRoute private peering."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    existingFirstPipResourceId: str
    """The Public IP resource ID to associate to the Virtual Network Gateway. If empty, then a new Public IP will be created and applied to the Virtual Network Gateway."""
    firstPipName: str
    """Specifies the name of the Public IP to be created for the Virtual Network Gateway. This will only take effect if no existing Public IP is provided. If neither an existing Public IP nor this parameter is specified, a new Public IP will be created with a default name, using the gateway's name with the '-pip1' suffix."""
    gatewayDefaultSiteLocalNetworkGatewayId: str
    """The reference to the LocalNetworkGateway resource which represents local network site having default routes. Assign Null value in case of removing existing default site setting."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    natRules: List['NatRule']
    """NatRules for virtual network gateway. NAT is supported on the the following SKUs: VpnGw2~5, VpnGw2AZ~5AZ and is supported for IPsec/IKE cross-premises connections only."""
    publicIpDiagnosticSettings: List['PublicIpDiagnosticSetting']
    """The diagnostic settings of the Public IP."""
    publicIPPrefixResourceId: str
    """Resource ID of the Public IP Prefix object. This is only needed if you want your Public IPs created in a PIP Prefix."""
    publicIpZones: List[object]
    """Specifies the zones of the Public IP address. Basic IP SKU does not support Availability Zones."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vpnClientAadConfiguration: Dict[str, object]
    """Configuration for AAD Authentication for P2S Tunnel Type, Cannot be configured if clientRootCertData is provided."""
    vpnClientAddressPoolPrefix: str
    """The IP address range from which VPN clients will receive an IP address when connected. Range specified must not overlap with on-premise network."""
    vpnGatewayGeneration: Literal['Generation1', 'Generation2', 'None']
    """The generation for this VirtualNetworkGateway. Must be None if virtualNetworkGatewayType is not VPN."""
    vpnType: Literal['PolicyBased', 'RouteBased']
    """Specifies the VPN type."""


class NetworkVirtualNetworkGatewayOutputs(TypedDict, total=False):
    """Outputs for NetworkVirtualNetworkGateway"""
    activeActive: Output[Literal['bool']]
    """Shows if the virtual network gateway is configured in Active-Active mode."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the virtual network gateway."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual network gateway was deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual network gateway."""


class NetworkVirtualNetworkGatewayBicep(Module):
    outputs: NetworkVirtualNetworkGatewayOutputs


def network_virtual_network_gateway(
        bicep: IO[str],
        params: NetworkVirtualNetworkGateway,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkVirtualNetworkGatewayBicep:
    symbol = "network_virtual_network_gateway_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/virtual-network-gateway:{tag}' = {{\n")
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
    output = NetworkVirtualNetworkGatewayBicep(symbol)
    output.outputs = {
            'activeActive': Output(symbol, 'activeActive', 'bool'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
