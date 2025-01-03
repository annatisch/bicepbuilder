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


class NetworkExpressRouteCircuit(TypedDict, total=False):
    """"""
    bandwidthInMbps: Required[int]
    """This is the bandwidth in Mbps of the circuit being created. It must exactly match one of the available bandwidth offers List ExpressRoute Service Providers API call."""
    name: Required[str]
    """This is the name of the ExpressRoute circuit."""
    peeringLocation: Required[str]
    """This is the name of the peering location and not the ARM resource location. It must exactly match one of the available peering locations from List ExpressRoute Service Providers API call."""
    serviceProviderName: Required[str]
    """This is the name of the ExpressRoute Service Provider. It must exactly match one of the Service Providers from List ExpressRoute Service Providers API call."""
    allowClassicOperations: bool
    """Allow classic operations. You can connect to virtual networks in the classic deployment model by setting allowClassicOperations to true."""
    bandwidthInGbps: int
    """The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource. Available when configuring Express Route Direct. Default value of 0 will set the property to null."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    expressRoutePortResourceId: str
    """The reference to the ExpressRoutePort resource when the circuit is provisioned on an ExpressRoutePort resource. Available when configuring Express Route Direct."""
    globalReachEnabled: bool
    """Flag denoting global reach status. To enable ExpressRoute Global Reach between different geopolitical regions, your circuits must be Premium SKU."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    peerASN: int
    """The autonomous system number of the customer/connectivity provider."""
    peering: bool
    """Enabled BGP peering type for the Circuit."""
    peeringType: Literal['AzurePrivatePeering', 'MicrosoftPeering']
    """BGP peering type for the Circuit. Choose from AzurePrivatePeering, AzurePublicPeering or MicrosoftPeering."""
    primaryPeerAddressPrefix: str
    """A /30 subnet used to configure IP addresses for interfaces on Link1."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    secondaryPeerAddressPrefix: str
    """A /30 subnet used to configure IP addresses for interfaces on Link2."""
    sharedKey: str
    """The shared key for peering configuration. Router does MD5 hash comparison to validate the packets sent by BGP connection. This parameter is optional and can be removed from peering configuration if not required."""
    skuFamily: Literal['MeteredData', 'UnlimitedData']
    """Chosen SKU family of ExpressRoute circuit. Choose from MeteredData or UnlimitedData SKU families."""
    skuTier: Literal['Local', 'Premium', 'Standard']
    """Chosen SKU Tier of ExpressRoute circuit. Choose from Local, Premium or Standard SKU tiers."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vlanId: int
    """Specifies the identifier that is used to identify the customer."""


class NetworkExpressRouteCircuitOutputs(TypedDict, total=False):
    """Outputs for NetworkExpressRouteCircuit"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of express route curcuit."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the express route curcuit was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of express route curcuit."""
    serviceKey: Output[Literal['string']]
    """The service key of the express route circuit."""


class NetworkExpressRouteCircuitModule(Module):
    outputs: NetworkExpressRouteCircuitOutputs


def _network_express_route_circuit(
        bicep: IO[str],
        params: NetworkExpressRouteCircuit,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkExpressRouteCircuitModule:
    symbol = "network_express_route_circuit_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/express-route-circuit:{tag}' = {{\n")
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
    output = NetworkExpressRouteCircuitModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'serviceKey': Output(symbol, 'serviceKey', 'string'),
        }

    return output
