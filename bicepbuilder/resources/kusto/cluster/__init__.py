from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class AcceptedAudience(TypedDict, total=False):
    """The Kusto Cluster's accepted audiences."""
    value: Required[str]
    """GUID or valid URL representing an accepted audience."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


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


class LanguageExtension(TypedDict, total=False):
    """List of the language extensions of the Kusto Cluster."""
    languageExtensionCustomImageName: Required[str]
    """The name of the language extension custom image."""
    languageExtensionImageName: Required[Literal['Python3_10_8', 'Python3_10_8_DL', 'Python3_6_5', 'PythonCustomImage', 'R']]
    """The name of the language extension image."""
    languageExtensionName: Required[Literal['PYTHON', 'R']]
    """The name of the language extension."""


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
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class PrincipalAssignment(TypedDict, total=False):
    """The Principal Assignments for the Kusto Cluster."""
    principalId: Required[str]
    """The principal id assigned to the Kusto Cluster principal. It can be a user email, application id, or security group name."""
    principalType: Required[Literal['App', 'Group', 'User']]
    """The principal type of the principal id."""
    role: Required[Literal['AllDatabasesAdmin', 'AllDatabasesViewer']]
    """The Kusto Cluster role to be assigned to the principal id."""
    tenantId: str
    """The tenant id of the principal."""


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
    """The private DNS Zone Groups to associate the Private Endpoint. A DNS Zone Group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS Zone Group config."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS zone group to configure for the private endpoint."""
    privateDnsZoneGroupConfigs: Required[List['PrivateDnsZoneGroupConfig']]
    """The private DNS Zone Groups to associate the Private Endpoint. A DNS Zone Group can support up to 5 DNS zones."""
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
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    service: Required[str]
    """The subresource to deploy the private endpoint for. For example "blob", "table", "queue" or "file" for a Storage Account's Private Endpoints."""
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
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader']]]
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


class TrustedExternalTenant(TypedDict, total=False):
    """The external tenants trusted by the Kusto Cluster."""
    value: Required[str]
    """GUID representing an external tenant."""


class VirtualNetworkConfiguration(TypedDict, total=False):
    """The virtual network configuration of the Kusto Cluster."""
    dataManagementPublicIpResourceId: Required[str]
    """The public IP address resource id of the data management service.."""
    enginePublicIpResourceId: Required[str]
    """The public IP address resource id of the engine service."""
    subnetResourceId: Required[str]
    """The resource ID of the subnet to which to deploy the Kusto Cluster."""


class KustoCluster(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Kusto cluster which must be unique within Azure."""
    sku: Required[str]
    """The SKU of the Kusto Cluster."""
    acceptedAudiences: List['AcceptedAudience']
    """The Kusto Cluster's accepted audiences."""
    allowedFqdnList: List[object]
    """List of allowed fully-qulified domain names (FQDNs) for egress from the Kusto Cluster."""
    allowedIpRangeList: List[object]
    """List of IP addresses in CIDR format allowed to connect to the Kusto Cluster."""
    autoScaleMax: int
    """When auto-scale is enabled, the maximum number of instances in the Kusto Cluster."""
    autoScaleMin: int
    """When auto-scale is enabled, the minimum number of instances in the Kusto Cluster."""
    capacity: int
    """The number of instances of the Kusto Cluster."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableAutoScale: bool
    """Enable/disable auto-scale."""
    enableAutoStop: bool
    """Enable/disable auto-stop."""
    enableDiskEncryption: bool
    """Enable/disable disk encryption."""
    enableDoubleEncryption: bool
    """Enable/disable double encryption."""
    enablePublicNetworkAccess: bool
    """Enable/disable public network access. If disabled, only private endpoint connection is allowed to the Kusto Cluster."""
    enablePurge: bool
    """Enable/disable purge."""
    enableRestrictOutboundNetworkAccess: bool
    """Enable/disable restricting outbound network access."""
    enableStreamingIngest: bool
    """Enable/disable streaming ingest."""
    enableTelemetry: bool
    """Enable/disable usage telemetry for module."""
    enableZoneRedundant: bool
    """Enable/disable zone redundancy."""
    engineType: Literal['V2', 'V3']
    """The engine type of the Kusto Cluster."""
    languageExtensions: List['LanguageExtension']
    """List of the language extensions of the Kusto Cluster."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    principalAssignments: List['PrincipalAssignment']
    """The Principal Assignments for the Kusto Cluster."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    publicIPType: Literal['DualStack', 'IPv4', 'IPv6']
    """Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6)."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tier: Literal['Basic', 'Standard']
    """The tier of the Kusto Cluster."""
    trustedExternalTenants: List['TrustedExternalTenant']
    """The external tenants trusted by the Kusto Cluster."""
    virtualClusterGraduationProperties: str
    """The virtual cluster graduation properties of the Kusto Cluster."""
    virtualNetworkConfiguration: 'VirtualNetworkConfiguration'
    """The virtual network configuration of the Kusto Cluster."""


class KustoClusterOutputs(TypedDict, total=False):
    """Outputs for KustoCluster"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the kusto cluster."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the kusto cluster."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the kusto cluster was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource id of the kusto cluster."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class KustoClusterModule(Module):
    outputs: KustoClusterOutputs

