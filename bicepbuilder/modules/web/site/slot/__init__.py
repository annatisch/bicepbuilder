from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)

if TYPE_CHECKING:
    from .basic_publishing_credentials_policy import BasicPublishingCredentialsPolicy


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class MetricCategory(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
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
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
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


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""
    properties: Required['IpConfigurationProperties']
    """Properties of private endpoint IP configurations."""


class Lock(TypedDict, total=False):
    """Specify the type of lock."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS zone group to configure for the private endpoint."""
    privateDnsZoneGroupConfigs: Required[List['PrivateDnsZoneGroupConfig']]
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    name: str
    """The name of the Private DNS Zone Group."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator (Preview)']]]
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


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the private endpoint IP configuration is included."""
    customDnsConfigs: List['CustomDnsConfig']
    """Custom DNS configurations."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the private endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipConfigurations: List['IpConfiguration']
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the private endpoint to."""
    lock: 'Lock'
    """Specify the type of lock."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the private endpoint."""
    privateDnsZoneGroup: 'PrivateDnsZoneGroup'
    """The private DNS zone group to configure for the private endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different resource group than the main resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    service: str
    """The subresource to deploy the private endpoint for. For example "vault", "mysqlServer" or "dataFactory"."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['App Compliance Automation Administrator', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Web Plan Contributor', 'Website Contributor']]]
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


class Slot(TypedDict, total=False):
    """"""
    kind: Required[Literal['api', 'app', 'app,container,windows', 'app,linux', 'app,linux,container', 'functionapp', 'functionapp,linux', 'functionapp,linux,container', 'functionapp,linux,container,azurecontainerapps', 'functionapp,workflowapp', 'functionapp,workflowapp,linux', 'linux,api']]
    """Type of site to deploy."""
    name: Required[str]
    """Name of the slot."""
    appInsightResourceId: str
    """Resource ID of the app insight to leverage for this resource."""
    appServiceEnvironmentResourceId: str
    """The resource ID of the app service environment to use for this resource."""
    appSettingsKeyValuePairs: Dict[str, object]
    """The app settings-value pairs except for AzureWebJobsStorage, AzureWebJobsDashboard, APPINSIGHTS_INSTRUMENTATIONKEY and APPLICATIONINSIGHTS_CONNECTION_STRING."""
    authSettingV2Configuration: Dict[str, object]
    """The auth settings V2 configuration."""
    basicPublishingCredentialsPolicies: List['BasicPublishingCredentialsPolicy']
    """The site publishing credential policy names which are associated with the site slot."""
    clientAffinityEnabled: bool
    """If client affinity is enabled."""
    clientCertEnabled: bool
    """To enable client certificate authentication (TLS mutual authentication)."""
    clientCertExclusionPaths: str
    """Client certificate authentication comma-separated exclusion paths."""
    clientCertMode: Literal['Optional', 'OptionalInteractiveUser', 'Required']
    """This composes with ClientCertEnabled setting."""
    cloningInfo: Dict[str, object]
    """If specified during app creation, the app is cloned from a source app."""
    containerSize: int
    """Size of the function container."""
    customDomainVerificationId: str
    """Unique identifier that verifies the custom domains assigned to the app. Customer will add this ID to a txt record for verification."""
    dailyMemoryTimeQuota: int
    """Maximum allowed daily memory-time quota (applicable on dynamic apps only)."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enabled: bool
    """Setting this value to false disables the app (takes the app offline)."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    functionAppConfig: Dict[str, object]
    """The Function App config object."""
    hostNameSslStates: List[object]
    """Hostname SSL states are used to manage the SSL bindings for app's hostnames."""
    httpsOnly: bool
    """Configures a slot to accept only HTTPS requests. Issues redirect for HTTP requests."""
    hybridConnectionRelays: List[object]
    """Names of hybrid connection relays to connect app with."""
    hyperV: bool
    """Hyper-V sandbox."""
    keyVaultAccessIdentityResourceId: str
    """The resource ID of the assigned identity to be used to access a key vault with."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    msDeployConfiguration: Dict[str, object]
    """The extension MSDeployment configuration."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Allow or block all public traffic."""
    redundancyMode: Literal['ActiveActive', 'Failover', 'GeoRedundant', 'Manual', 'None']
    """Site redundancy mode."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    serverFarmResourceId: str
    """The resource ID of the app service plan to use for the slot."""
    siteConfig: Dict[str, object]
    """The site config object."""
    storageAccountRequired: bool
    """Checks if Customer provided storage account is required."""
    storageAccountResourceId: str
    """Required if app of kind functionapp. Resource ID of the storage account to manage triggers and logging function executions."""
    storageAccountUseIdentityAuthentication: bool
    """If the provided storage account requires Identity based authentication ('allowSharedKeyAccess' is set to false). When set to true, the minimum role assignment required for the App Service Managed Identity to the storage account is 'Storage Blob Data Owner'."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualNetworkSubnetId: str
    """Azure Resource Manager ID of the Virtual network and subnet to be joined by Regional VNET Integration. This must be of the form /subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}."""
    vnetContentShareEnabled: bool
    """To enable accessing content over virtual network."""
    vnetImagePullEnabled: bool
    """To enable pulling image over Virtual Network."""
    vnetRouteAllEnabled: bool
    """Virtual Network Route All enabled. This causes all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied."""


class SlotOutputs(TypedDict, total=False):
    """Outputs for Slot"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the slot."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the slot."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the slot was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the slot."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class SlotBicep(Module):
    outputs: SlotOutputs

