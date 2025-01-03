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


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition to use for the managed service."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class CustomerManagedKeyManagedDisk(TypedDict, total=False):
    """The customer managed key definition to use for the managed disk."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    autoRotationEnabled: bool
    """Enable or disable auto-rotating to the latest key version. Default is """
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, using version as per 'autoRotationEnabled' setting."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class DefaultCatalog(TypedDict, total=False):
    """The default catalog configuration for the Databricks workspace."""
    initialType: Required[Literal['HiveMetastore', 'UnityCatalog']]
    """Choose between HiveMetastore or UnityCatalog."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class StorageAccountPrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints for the managed workspace storage account, required when privateStorageAccount is set to Enabled. For security reasons, it is recommended to use private endpoints whenever possible."""
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


class DatabricksWorkspace(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Azure Databricks workspace to create."""
    accessConnectorResourceId: str
    """The resource ID of the associated access connector for private access to the managed workspace storage account. Required if privateStorageAccount is enabled."""
    amlWorkspaceResourceId: str
    """The resource ID of a Azure Machine Learning workspace to link with Databricks workspace."""
    automaticClusterUpdate: Literal['', 'Disabled', 'Enabled']
    """The value for enabling automatic cluster updates in enhanced security compliance."""
    complianceSecurityProfileValue: Literal['', 'Disabled', 'Enabled']
    """The value to Enable or Disable for the compliance security profile."""
    complianceStandards: List[object]
    """The compliance standards array for the security profile. Should be a list of compliance standards like "HIPAA", "NONE" or "PCI_DSS"."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition to use for the managed service."""
    customerManagedKeyManagedDisk: 'CustomerManagedKeyManagedDisk'
    """The customer managed key definition to use for the managed disk."""
    customPrivateSubnetName: str
    """The name of the Private Subnet within the Virtual Network."""
    customPublicSubnetName: str
    """The name of a Public Subnet within the Virtual Network."""
    customVirtualNetworkResourceId: str
    """The resource ID of a Virtual Network where this Databricks Cluster should be created."""
    defaultCatalog: 'DefaultCatalog'
    """The default catalog configuration for the Databricks workspace."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disablePublicIp: bool
    """Disable Public IP."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    enhancedSecurityMonitoring: Literal['', 'Disabled', 'Enabled']
    """The value for enabling or configuring enhanced security monitoring."""
    loadBalancerBackendPoolName: str
    """Name of the outbound Load Balancer Backend Pool for Secure Cluster Connectivity (No Public IP)."""
    loadBalancerResourceId: str
    """Resource URI of Outbound Load balancer for Secure Cluster Connectivity (No Public IP) workspace."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedResourceGroupResourceId: str
    """The managed resource group ID. It is created by the module as per the to-be resource ID you provide."""
    natGatewayName: str
    """Name of the NAT gateway for Secure Cluster Connectivity (No Public IP) workspace subnets."""
    prepareEncryption: bool
    """Prepare the workspace for encryption. Enables the Managed Identity for managed storage account."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    privateStorageAccount: Literal['', 'Disabled', 'Enabled']
    """Determines whether the managed storage account should be private or public. For best security practices, it is recommended to set it to Enabled."""
    publicIpName: str
    """Name of the Public IP for No Public IP workspace with managed vNet."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """The network access type for accessing workspace. Set value to disabled to access workspace only via private link."""
    requiredNsgRules: Literal['AllRules', 'NoAzureDatabricksRules']
    """Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint."""
    requireInfrastructureEncryption: bool
    """A boolean indicating whether or not the DBFS root file system will be enabled with secondary layer of encryption with platform managed keys for data at rest."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    skuName: Literal['premium', 'standard', 'trial']
    """The pricing tier of workspace."""
    storageAccountName: str
    """Default DBFS storage account name."""
    storageAccountPrivateEndpoints: List['StorageAccountPrivateEndpoint']
    """Configuration details for private endpoints for the managed workspace storage account, required when privateStorageAccount is set to Enabled. For security reasons, it is recommended to use private endpoints whenever possible."""
    storageAccountSkuName: str
    """Storage account SKU name."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vnetAddressPrefix: str
    """Address prefix for Managed virtual network."""


class DatabricksWorkspaceOutputs(TypedDict, total=False):
    """Outputs for DatabricksWorkspace"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    managedResourceGroupName: Output[Literal['string']]
    """The name of the managed resource group."""
    managedResourceGroupResourceId: Output[Literal['string']]
    """The resource ID of the managed resource group."""
    name: Output[Literal['string']]
    """The name of the deployed databricks workspace."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the Databricks Workspace."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed databricks workspace."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed databricks workspace."""
    storageAccountName: Output[Literal['string']]
    """The name of the DBFS storage account."""
    storageAccountResourceId: Output[Literal['string']]
    """The resource ID of the DBFS storage account."""
    storagePrivateEndpoints: Output[Literal['array']]
    """The private endpoints of the Databricks Workspace Storage."""
    workspaceResourceId: Output[Literal['string']]
    """The unique identifier of the databricks workspace in databricks control plane."""
    workspaceUrl: Output[Literal['string']]
    """The workspace URL which is of the format 'adb-{workspaceId}.{random}.azuredatabricks.net'."""


class DatabricksWorkspaceModule(Module):
    outputs: DatabricksWorkspaceOutputs


def _databricks_workspace(
        bicep: IO[str],
        params: DatabricksWorkspace,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> DatabricksWorkspaceModule:
    symbol = "databricks_workspace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/databricks/workspace:{tag}' = {{\n")
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
    output = DatabricksWorkspaceModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'managedResourceGroupName': Output(symbol, 'managedResourceGroupName', 'string'),
            'managedResourceGroupResourceId': Output(symbol, 'managedResourceGroupResourceId', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'storageAccountName': Output(symbol, 'storageAccountName', 'string'),
            'storageAccountResourceId': Output(symbol, 'storageAccountResourceId', 'string'),
            'storagePrivateEndpoints': Output(symbol, 'storagePrivateEndpoints', 'array'),
            'workspaceResourceId': Output(symbol, 'workspaceResourceId', 'string'),
            'workspaceUrl': Output(symbol, 'workspaceUrl', 'string'),
        }

    return output
