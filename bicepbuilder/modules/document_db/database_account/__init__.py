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
    from .gremlin_database import GremlinDatabase
    from .mongodb_database import MongodbDatabase
    from .table import Table


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


class Location(TypedDict, total=False):
    """Default to the location where the account is deployed. Locations enabled for the Cosmos DB account."""
    failoverPriority: Required[int]
    """The failover priority of the region. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists."""
    locationName: Required[str]
    """The name of the region."""
    isZoneRedundant: bool
    """Default to true. Flag to indicate whether or not this region is an AvailabilityZone region."""


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


class VirtualNetworkRule(TypedDict, total=False):
    """List of Virtual Network ACL rules configured for the Cosmos DB account.."""
    subnetResourceId: Required[str]
    """Resource ID of a subnet."""


class NetworkRestriction(TypedDict, total=False):
    """The network configuration of this module. Defaults to """
    ipRules: List[object]
    """A single IPv4 address or a single IPv4 address range in CIDR format. Provided IPs must be well-formatted and cannot be contained in one of the following ranges: 10.0.0.0/8, 100.64.0.0/10, 172.16.0.0/12, 192.168.0.0/16, since these are not enforceable by the IP address filter. Example of valid inputs: "23.40.210.245" or "23.40.210.0/8"."""
    networkAclBypass: Literal['AzureServices', 'None']
    """Default to None. Specifies the network ACL bypass for Azure services."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Default to Disabled. Whether requests from Public Network are allowed."""
    virtualNetworkRules: List['VirtualNetworkRule']
    """List of Virtual Network ACL rules configured for the Cosmos DB account.."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private ip addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private ip address obtained from the private endpoint's subnet."""


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


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    service: Required[str]
    """The subresource to deploy the private endpoint for. For example "blob", "table", "queue" or "file"."""
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
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator (Preview)']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignment objects that contain the 'roleDefinitionIdOrName' and 'principalIds' to define RBAC role assignments on this resource. In the roleDefinitionIdOrName attribute, you can provide either the display name of the role definition, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
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


class SecretsExportConfiguration(TypedDict, total=False):
    """Key vault reference and secret settings for the module's secrets export."""
    keyVaultResourceId: Required[str]
    """The resource ID of the key vault where to store the secrets of this module."""
    primaryReadonlyConnectionStringSecretName: str
    """The primary readonly connection string secret name to create."""
    primaryReadOnlyKeySecretName: str
    """The primary readonly key secret name to create."""
    primaryWriteConnectionStringSecretName: str
    """The primary write connection string secret name to create."""
    primaryWriteKeySecretName: str
    """The primary write key secret name to create."""
    secondaryReadonlyConnectionStringSecretName: str
    """The primary readonly connection string secret name to create."""
    secondaryReadonlyKeySecretName: str
    """The primary readonly key secret name to create."""
    secondaryWriteConnectionStringSecretName: str
    """The primary write connection string secret name to create."""
    secondaryWriteKeySecretName: str
    """The primary write key secret name to create."""


class ConflictResolutionPolicy(TypedDict, total=False):
    """The conflict resolution policy for the container. Conflicts and conflict resolution policies are applicable if the Azure Cosmos DB account is configured with multiple write regions."""
    mode: Required[Literal['Custom', 'LastWriterWins']]
    """Indicates the conflict resolution mode."""
    conflictResolutionPath: str
    """The conflict resolution path in the case of LastWriterWins mode. Required if """
    conflictResolutionProcedure: str
    """The procedure to resolve conflicts in the case of custom mode. Required if """


class UniqueKeyPolicyKey(TypedDict, total=False):
    """The unique key policy configuration containing a list of unique keys that enforces uniqueness constraint on documents in the collection in the Azure Cosmos DB service."""
    paths: Required[List[object]]
    """List of paths must be unique for each document in the Azure Cosmos DB service."""


class Container(TypedDict, total=False):
    """Array of containers to deploy in the SQL database."""
    name: Required[str]
    """Name of the container."""
    paths: Required[List[object]]
    """List of paths using which data within the container can be partitioned. For kind=MultiHash it can be up to 3. For anything else it needs to be exactly 1."""
    analyticalStorageTtl: int
    """Default to 0. Indicates how long data should be retained in the analytical store, for a container. Analytical store is enabled when ATTL is set with a value other than 0. If the value is set to -1, the analytical store retains all historical data, irrespective of the retention of the data in the transactional store."""
    autoscaleSettingsMaxThroughput: int
    """Specifies the Autoscale settings and represents maximum throughput, the resource can scale up to. The autoscale throughput should have valid throughput values between 1000 and 1000000 inclusive in increments of 1000. If value is set to null, then autoscale will be disabled."""
    conflictResolutionPolicy: 'ConflictResolutionPolicy'
    """The conflict resolution policy for the container. Conflicts and conflict resolution policies are applicable if the Azure Cosmos DB account is configured with multiple write regions."""
    defaultTtl: int
    """Default to -1. Default time to live (in seconds). With Time to Live or TTL, Azure Cosmos DB provides the ability to delete items automatically from a container after a certain time period. If the value is set to "-1", it is equal to infinity, and items don't expire by default."""
    indexingPolicy: Dict[str, object]
    """Indexing policy of the container."""
    kind: Literal['Hash', 'MultiHash']
    """Default to Hash. Indicates the kind of algorithm used for partitioning."""
    throughput: int
    """Default to 400. Request Units per second. Will be ignored if autoscaleSettingsMaxThroughput is used."""
    uniqueKeyPolicyKeys: List['UniqueKeyPolicyKey']
    """The unique key policy configuration containing a list of unique keys that enforces uniqueness constraint on documents in the collection in the Azure Cosmos DB service."""
    version: Literal[1, 2]
    """Default to 1 for Hash and 2 for MultiHash - 1 is not allowed for MultiHash. Version of the partition key definition."""


class SqlDatabase(TypedDict, total=False):
    """SQL Databases configurations."""
    name: Required[str]
    """Name of the SQL database ."""
    autoscaleSettingsMaxThroughput: int
    """Specifies the Autoscale settings and represents maximum throughput, the resource can scale up to.  The autoscale throughput should have valid throughput values between 1000 and 1000000 inclusive in increments of 1000. If value is set to null, then autoscale will be disabled."""
    containers: List['Container']
    """Array of containers to deploy in the SQL database."""
    throughput: int
    """Default to 400. Request units per second. Will be ignored if autoscaleSettingsMaxThroughput is used."""


class SqlRoleDefinition(TypedDict, total=False):
    """SQL Role Definitions configurations."""
    name: Required[str]
    """Name of the SQL Role Definition."""
    dataAction: List[object]
    """An array of data actions that are allowed."""
    roleName: str
    """A user-friendly name for the Role Definition. Must be unique for the database account."""
    roleType: Literal['BuiltInRole', 'CustomRole']
    """Indicates whether the Role Definition was built-in or user created."""


class DocumentDbDatabaseAccount(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Database Account."""
    automaticFailover: bool
    """Default to true. Enable automatic failover for regions."""
    backupIntervalInMinutes: int
    """Default to 240. An integer representing the interval in minutes between two backups. Only applies to periodic backup type."""
    backupPolicyContinuousTier: Literal['Continuous30Days', 'Continuous7Days']
    """Default to Continuous30Days. Configuration values for continuous mode backup."""
    backupPolicyType: Literal['Continuous', 'Periodic']
    """Default to Continuous. Describes the mode of backups. Periodic backup must be used if multiple write locations are used."""
    backupRetentionIntervalInHours: int
    """Default to 8. An integer representing the time (in hours) that each backup is retained. Only applies to periodic backup type."""
    backupStorageRedundancy: Literal['Geo', 'Local', 'Zone']
    """Default to Local. Enum to indicate type of backup residency. Only applies to periodic backup type."""
    capabilitiesToAdd: Literal['DisableRateLimitingResponses', 'EnableCassandra', 'EnableGremlin', 'EnableMaterializedViews', 'EnableMongo', 'EnableNoSQLFullTextSearch', 'EnableNoSQLVectorSearch', 'EnableServerless', 'EnableTable']
    """List of Cosmos DB capabilities for the account."""
    databaseAccountOfferType: Literal['Standard']
    """Default to Standard. The offer type for the Azure Cosmos DB database account."""
    defaultConsistencyLevel: Literal['BoundedStaleness', 'ConsistentPrefix', 'Eventual', 'Session', 'Strong']
    """Default to Session. The default consistency level of the Cosmos DB account."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableKeyBasedMetadataWriteAccess: bool
    """Default to true. Disable write operations on metadata resources (databases, containers, throughput) via account keys."""
    disableLocalAuth: bool
    """Default to true. Opt-out of local authentication and ensure only MSI and AAD can be used exclusively for authentication."""
    enableAnalyticalStorage: bool
    """Default to false. Flag to indicate whether to enable storage analytics."""
    enableFreeTier: bool
    """Default to false. Flag to indicate whether Free Tier is enabled."""
    enableMultipleWriteLocations: bool
    """Default to false. Enables the account to write in multiple locations. Periodic backup must be used if enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    gremlinDatabases: List['GremlinDatabase']
    """Gremlin Databases configurations."""
    location: str
    """Default to current resource group scope location. Location for all resources."""
    locations: List['Location']
    """Default to the location where the account is deployed. Locations enabled for the Cosmos DB account."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    maxIntervalInSeconds: int
    """Default to 300. Max lag time (minutes). Required for BoundedStaleness. Valid ranges, Single Region: 5 to 84600. Multi Region: 300 to 86400."""
    maxStalenessPrefix: int
    """Default to 100000. Max stale requests. Required for BoundedStaleness. Valid ranges, Single Region: 10 to 1000000. Multi Region: 100000 to 1000000."""
    minimumTlsVersion: Literal['Tls12']
    """Default to TLS 1.2. Enum to indicate the minimum allowed TLS version. Azure Cosmos DB for MongoDB RU and Apache Cassandra only work with TLS 1.2 or later."""
    mongodbDatabases: List['MongodbDatabase']
    """MongoDB Databases configurations."""
    networkRestrictions: 'NetworkRestriction'
    """The network configuration of this module. Defaults to """
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Cosmos DB Account Reader Role', 'Cosmos DB Operator', 'CosmosBackupOperator', 'CosmosRestoreOperator', 'DocumentDB Account Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator (Preview)', 'User Access Administrator']]]
    """Array of role assignment objects that contain the 'roleDefinitionIdOrName' and 'principalIds' to define RBAC role assignments on this resource. In the roleDefinitionIdOrName attribute, you can provide either the display name of the role definition, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    secretsExportConfiguration: 'SecretsExportConfiguration'
    """Key vault reference and secret settings for the module's secrets export."""
    serverVersion: Literal['3.2', '3.6', '4.0', '4.2', '5.0', '6.0', '7.0']
    """Default to 4.2. Specifies the MongoDB server version to use."""
    sqlDatabases: List['SqlDatabase']
    """SQL Databases configurations."""
    sqlRoleAssignmentsPrincipalIds: List[object]
    """SQL Role Definitions configurations."""
    sqlRoleDefinitions: List['SqlRoleDefinition']
    """SQL Role Definitions configurations."""
    tables: List['Table']
    """Table configurations."""
    tags: Dict[str, object]
    """Tags of the Database Account resource."""
    totalThroughputLimit: int
    """Default to unlimited. The total throughput limit imposed on this Cosmos DB account (RU/s)."""


class DocumentDbDatabaseAccountOutputs(TypedDict, total=False):
    """Outputs for DocumentDbDatabaseAccount"""
    endpoint: Output[Literal['string']]
    """The endpoint of the database account."""
    exportedSecrets: Output[Literal['object']]
    """The references to the secrets exported to the provided Key Vault."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the database account."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the database account."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the database account was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the database account."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class DocumentDbDatabaseAccountBicep(Module):
    outputs: DocumentDbDatabaseAccountOutputs


def document_db_database_account(
        bicep: IO[str],
        params: DocumentDbDatabaseAccount,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.10.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> DocumentDbDatabaseAccountBicep:
    symbol = "document_db_database_account_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/document-db/database-account:{tag}' = {{\n")
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
    output = DocumentDbDatabaseAccountBicep(symbol)
    output.outputs = {
            'endpoint': Output(symbol, 'endpoint', 'string'),
            'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
