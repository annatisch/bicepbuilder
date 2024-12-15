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


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    service: Required[str]
    """The subresource to deploy the private endpoint for. For example "blob", "table", "queue" or "file"."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the private endpoint IP configuration is included."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the private endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the private endpoint to."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the private endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different resource group than the main resource."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class Lock(TypedDict, total=False):
    """Specify the type of lock."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS zone group to configure for the private endpoint."""
    name: str
    """The name of the Private DNS Zone Group."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


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


class ApplicationGateway(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Application Gateway."""
    authenticationCertificates: List[object]
    """Authentication certificates of the application gateway resource."""
    autoscaleMaxCapacity: int
    """Upper bound on number of Application Gateway capacity."""
    autoscaleMinCapacity: int
    """Lower bound on number of Application Gateway capacity."""
    backendAddressPools: List[object]
    """Backend address pool of the application gateway resource."""
    backendHttpSettingsCollection: List[object]
    """Backend http settings of the application gateway resource."""
    backendSettingsCollection: List[object]
    """Backend settings of the application gateway resource. For default limits, see """
    capacity: int
    """The number of Application instances to be configured."""
    customErrorConfigurations: List[object]
    """Custom error configurations of the application gateway resource."""
    enableFips: bool
    """Whether FIPS is enabled on the application gateway resource."""
    enableHttp2: bool
    """Whether HTTP2 is enabled on the application gateway resource."""
    enableRequestBuffering: bool
    """Enable request buffering."""
    enableResponseBuffering: bool
    """Enable response buffering."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallPolicyResourceId: str
    """The resource ID of an associated firewall policy. Should be configured for security reasons."""
    frontendIPConfigurations: List[object]
    """Frontend IP addresses of the application gateway resource."""
    frontendPorts: List[object]
    """Frontend ports of the application gateway resource."""
    gatewayIPConfigurations: List[object]
    """Subnets of the application gateway resource."""
    httpListeners: List[object]
    """Http listeners of the application gateway resource."""
    listeners: List[object]
    """Listeners of the application gateway resource. For default limits, see """
    loadDistributionPolicies: List[object]
    """Load distribution policies of the application gateway resource."""
    location: str
    """Location for all resources."""
    privateLinkConfigurations: List[object]
    """PrivateLink configurations on application gateway."""
    probes: List[object]
    """Probes of the application gateway resource."""
    redirectConfigurations: List[object]
    """Redirect configurations of the application gateway resource."""
    requestRoutingRules: List[object]
    """Request routing rules of the application gateway resource."""
    rewriteRuleSets: List[object]
    """Rewrite rules for the application gateway resource."""
    routingRules: List[object]
    """Routing rules of the application gateway resource."""
    sku: Literal['Standard_Large', 'Standard_Medium', 'Standard_Small', 'Standard_v2', 'WAF_Large', 'WAF_Medium', 'WAF_v2']
    """The name of the SKU for the Application Gateway."""
    sslCertificates: List[object]
    """SSL certificates of the application gateway resource."""
    sslPolicyCipherSuites: Literal['TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA', 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA', 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA256', 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA', 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA', 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_RSA_WITH_3DES_EDE_CBC_SHA', 'TLS_RSA_WITH_AES_128_CBC_SHA', 'TLS_RSA_WITH_AES_128_CBC_SHA256', 'TLS_RSA_WITH_AES_128_GCM_SHA256', 'TLS_RSA_WITH_AES_256_CBC_SHA', 'TLS_RSA_WITH_AES_256_CBC_SHA256', 'TLS_RSA_WITH_AES_256_GCM_SHA384']
    """Ssl cipher suites to be enabled in the specified order to application gateway."""
    sslPolicyMinProtocolVersion: Literal['TLSv1_0', 'TLSv1_1', 'TLSv1_2', 'TLSv1_3']
    """Ssl protocol enums."""
    sslPolicyName: Literal['', 'AppGwSslPolicy20150501', 'AppGwSslPolicy20170401', 'AppGwSslPolicy20170401S', 'AppGwSslPolicy20220101', 'AppGwSslPolicy20220101S']
    """Ssl predefined policy name enums."""
    sslPolicyType: Literal['Custom', 'CustomV2', 'Predefined']
    """Type of Ssl Policy."""
    sslProfiles: List[object]
    """SSL profiles of the application gateway resource."""
    tags: Dict[str, object]
    """Resource tags."""
    trustedClientCertificates: List[object]
    """Trusted client certificates of the application gateway resource."""
    trustedRootCertificates: List[object]
    """Trusted Root certificates of the application gateway resource."""
    urlPathMaps: List[object]
    """URL path map of the application gateway resource."""
    webApplicationFirewallConfiguration: Dict[str, object]
    """Application gateway web application firewall configuration. Should be configured for security reasons."""
    zones: List[object]
    """A list of availability zones denoting where the resource needs to come from."""


class ApplicationGatewayOutputs(TypedDict, total=False):
    """Outputs for ApplicationGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the application gateway."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the application gateway."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the application gateway was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the application gateway."""


class ApplicationGatewayBicep(Module):
    outputs: ApplicationGatewayOutputs


def application_gateway(
        bicep: IO[str],
        /,
        *,
        params: ApplicationGateway,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/application-gateway',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ApplicationGatewayBicep:
    symbol = "application_gateway_" + generate_suffix()
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
    output = ApplicationGatewayBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
