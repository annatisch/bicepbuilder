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


class Administrator(TypedDict, total=False):
    """The Azure Active Directory (AAD) administrator authentication. Required if no """
    azureADOnlyAuthentication: Required[bool]
    """Azure Active Directory only Authentication enabled."""
    login: Required[str]
    """Login name of the server administrator."""
    principalType: Required[Literal['Application', 'Group', 'User']]
    """Principal Type of the sever administrator."""
    sid: Required[str]
    """SID (object ID) of the server administrator."""
    administratorType: Literal['ActiveDirectory']
    """Type of the sever administrator."""
    tenantId: str
    """Tenant ID of the administrator."""


class AuditSetting(TypedDict, total=False):
    """The audit settings configuration."""
    auditActionsAndGroups: List[object]
    """Specifies the Actions-Groups and Actions to audit."""
    isAzureMonitorTargetEnabled: bool
    """Specifies whether audit events are sent to Azure Monitor."""
    isDevopsAuditEnabled: bool
    """Specifies the state of devops audit. If state is Enabled, devops logs will be sent to Azure Monitor."""
    isManagedIdentityInUse: bool
    """Specifies whether Managed Identity is used to access blob storage."""
    isStorageSecondaryKeyInUse: bool
    """Specifies whether storageAccountAccessKey value is the storage's secondary key."""
    name: str
    """Specifies the name of the audit settings."""
    queueDelayMs: int
    """Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed."""
    retentionDays: int
    """Specifies the number of days to keep in the audit logs in the storage account."""
    state: Literal['Disabled', 'Enabled']
    """Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required."""
    storageAccountResourceId: str
    """Specifies the identifier key of the auditing storage account."""


class BackupLongTermRetentionPolicy(TypedDict, total=False):
    """The long term backup retention policy for the database."""
    backupStorageAccessTier: Literal['Archive', 'Hot']
    """The BackupStorageAccessTier for the LTR backups."""
    makeBackupsImmutable: bool
    """The setting whether to make LTR backups immutable."""
    monthlyRetention: str
    """Monthly retention in ISO 8601 duration format."""
    weeklyRetention: str
    """Weekly retention in ISO 8601 duration format."""
    weekOfYear: int
    """Week of year backup to keep for yearly retention."""
    yearlyRetention: str
    """Yearly retention in ISO 8601 duration format."""


class BackupShortTermRetentionPolicy(TypedDict, total=False):
    """The short term backup retention policy for the database."""
    diffBackupIntervalInHours: int
    """Differential backup interval in hours. For Hyperscale tiers this value will be ignored."""
    retentionDays: int
    """Point-in-time retention in days."""


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


class Sku(TypedDict, total=False):
    """The database SKU."""
    name: Required[str]
    """The name of the SKU, typically, a letter + Number code, e.g. P3."""
    capacity: int
    """The capacity of the particular SKU."""
    family: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    size: str
    """Size of the particular SKU."""
    tier: str
    """The tier or edition of the particular SKU, e.g. Basic, Premium."""


class Database(TypedDict, total=False):
    """The databases to create in the server."""
    name: Required[str]
    """The name of the Elastic Pool."""
    autoPauseDelay: int
    """Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled."""
    availabilityZone: Literal['1', '2', '3', 'NoPreference']
    """Specifies the availability zone the database is pinned to."""
    backupLongTermRetentionPolicy: 'BackupLongTermRetentionPolicy'
    """The long term backup retention policy for the database."""
    backupShortTermRetentionPolicy: 'BackupShortTermRetentionPolicy'
    """The short term backup retention policy for the database."""
    catalogCollation: str
    """Collation of the metadata catalog."""
    collation: str
    """The collation of the database."""
    createMode: Literal['Copy', 'Default', 'OnlineSecondary', 'PointInTimeRestore', 'Recovery', 'Restore', 'RestoreExternalBackup', 'RestoreExternalBackupSecondary', 'RestoreLongTermRetentionBackup', 'Secondary']
    """Specifies the mode of database creation."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    elasticPoolResourceId: str
    """The resource identifier of the elastic pool containing this database."""
    encryptionProtector: str
    """The azure key vault URI of the database if it's configured with per Database Customer Managed Keys."""
    encryptionProtectorAutoRotation: bool
    """The flag to enable or disable auto rotation of database encryption protector AKV key."""
    federatedClientId: str
    """The Client id used for cross tenant per database CMK scenario."""
    freeLimitExhaustionBehavior: Literal['AutoPause', 'BillOverUsage']
    """Specifies the behavior when monthly free limits are exhausted for the free database."""
    highAvailabilityReplicaCount: int
    """The number of secondary replicas associated with the database that are used to provide high availability. Not applicable to a Hyperscale database within an elastic pool."""
    isLedgerOn: bool
    """Whether or not this database is a ledger database, which means all tables in the database are ledger tables."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this database."""
    longTermRetentionBackupResourceId: str
    """The resource identifier of the long term retention backup associated with create operation of this database."""
    maintenanceConfigurationId: str
    """Maintenance configuration id assigned to the database. This configuration defines the period when the maintenance updates will occur."""
    manualCutover: bool
    """Whether or not customer controlled manual cutover needs to be done during Update Database operation to Hyperscale tier."""
    maxSizeBytes: int
    """The max size of the database expressed in bytes."""
    minCapacity: str
    """Minimal capacity that database will always have allocated, if not paused."""
    performCutover: bool
    """To trigger customer controlled manual cutover during the wait state while Scaling operation is in progress."""
    preferredEnclaveType: Literal['Default', 'VBS']
    """Type of enclave requested on the database."""
    readScale: Literal['Disabled', 'Enabled']
    """The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool."""
    recoverableDatabaseResourceId: str
    """The resource identifier of the recoverable database associated with create operation of this database."""
    recoveryServicesRecoveryPointResourceId: str
    """The resource identifier of the recovery point associated with create operation of this database."""
    requestedBackupStorageRedundancy: Literal['Geo', 'GeoZone', 'Local', 'Zone']
    """The storage account type to be used to store backups for this database."""
    restorableDroppedDatabaseResourceId: str
    """The resource identifier of the restorable dropped database associated with create operation of this database."""
    restorePointInTime: str
    """Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database."""
    sampleName: str
    """The name of the sample schema to apply when creating this database."""
    secondaryType: Literal['Geo', 'Named', 'Standby']
    """The secondary type of the database if it is a secondary."""
    sku: 'Sku'
    """The database SKU."""
    sourceDatabaseDeletionDate: str
    """Specifies the time that the database was deleted."""
    sourceDatabaseResourceId: str
    """The resource identifier of the source database associated with create operation of this database."""
    sourceResourceId: str
    """The resource identifier of the source associated with the create operation of this database."""
    tags: Dict[str, object]
    """Tags of the resource."""
    useFreeLimit: bool
    """Whether or not the database uses free monthly limits. Allowed on one database in a subscription."""
    zoneRedundant: bool
    """Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones."""


class PerDatabaseSetting(TypedDict, total=False):
    """The per database settings for the elastic pool."""
    maxCapacity: Required[str]
    """The maximum capacity any one database can consume. Examples: '0.5', '2'."""
    minCapacity: Required[str]
    """The minimum capacity all databases are guaranteed. Examples: '0.5', '1'."""
    autoPauseDelay: int
    """Auto Pause Delay for per database within pool."""


class Sku(TypedDict, total=False):
    """The elastic pool SKU."""
    name: Required[Literal['BasicPool', 'BC_DC', 'BC_Gen5', 'GP_DC', 'GP_FSv2', 'GP_Gen5', 'HS_Gen5', 'HS_MOPRMS', 'HS_PRMS', 'PremiumPool', 'ServerlessPool', 'StandardPool']]
    """The name of the SKU, typically, a letter + Number code, e.g. P3."""
    capacity: int
    """The capacity of the particular SKU."""
    family: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    size: str
    """Size of the particular SKU."""
    tier: str
    """The tier or edition of the particular SKU, e.g. Basic, Premium."""


class ElasticPool(TypedDict, total=False):
    """The Elastic Pools to create in the server."""
    name: Required[str]
    """The name of the Elastic Pool."""
    autoPauseDelay: int
    """Time in minutes after which elastic pool is automatically paused. A value of -1 means that automatic pause is disabled."""
    availabilityZone: Literal['1', '2', '3', 'NoPreference']
    """Specifies the availability zone the pool's primary replica is pinned to."""
    highAvailabilityReplicaCount: int
    """The number of secondary replicas associated with the elastic pool that are used to provide high availability. Applicable only to Hyperscale elastic pools."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this elastic pool."""
    maintenanceConfigurationId: str
    """Maintenance configuration id assigned to the elastic pool. This configuration defines the period when the maintenance updates will will occur."""
    maxSizeBytes: int
    """The storage limit for the database elastic pool in bytes."""
    minCapacity: int
    """Minimal capacity that serverless pool will not shrink below, if not paused."""
    perDatabaseSettings: 'PerDatabaseSetting'
    """The per database settings for the elastic pool."""
    preferredEnclaveType: Literal['Default', 'VBS']
    """Type of enclave requested on the elastic pool."""
    sku: 'Sku'
    """The elastic pool SKU."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneRedundant: bool
    """Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones."""


class EncryptionProtectorObj(TypedDict, total=False):
    """The encryption protection configuration."""
    serverKeyName: Required[str]
    """The name of the server key."""
    autoRotationEnabled: bool
    """Key auto rotation opt-in flag."""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The encryption protector type."""


class FirewallRule(TypedDict, total=False):
    """The firewall rules to create in the server."""
    name: Required[str]
    """The name of the firewall rule."""
    endIpAddress: str
    """The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress. Use value '0.0.0.0' for all Azure-internal IP addresses."""
    startIpAddress: str
    """The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' for all Azure-internal IP addresses."""


class Key(TypedDict, total=False):
    """The keys to configure."""
    name: str
    """The name of the key. Must follow the ["""
    serverKeyType: Literal['AzureKeyVault', 'ServiceManaged']
    """The server key type."""
    uri: str
    """The URI of the server key. If the ServerKeyType is AzureKeyVault, then the URI is required. The AKV URI is required to be in this format: 'https://YourVaultName.azure.net/keys/YourKeyName/YourKeyVersion'."""


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
    """A list of IP configurations of the Private Endpoint. This will be used to map to the first-party Service endpoints."""
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
    """The private DNS Zone Group to configure for the Private Endpoint."""
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
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the Private Endpoint IP configuration is included."""
    customDnsConfigs: List['CustomDnsConfig']
    """Custom DNS configurations."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the Private Endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipConfigurations: List['IpConfiguration']
    """A list of IP configurations of the Private Endpoint. This will be used to map to the first-party Service endpoints."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the Private Endpoint to."""
    lock: 'Lock'
    """Specify the type of lock."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the Private Endpoint."""
    privateDnsZoneGroup: 'PrivateDnsZoneGroup'
    """The private DNS Zone Group to configure for the Private Endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different Resource Group than the main resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    service: str
    """The subresource to deploy the Private Endpoint for. For example "vault" for a Key Vault Private Endpoint."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/Resource Groups in this deployment."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Reservation Purchaser', 'Role Based Access Control Administrator', 'SQL DB Contributor', 'SQL Managed Instance Contributor', 'SQL Security Manager', 'SQL Server Contributor', 'SqlDb Migration Role', 'SqlMI Migration Role', 'User Access Administrator']]]
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
    sqlAdminPasswordSecretName: str
    """The sqlAdminPassword secret name to create."""
    sqlAzureConnectionStringSercretName: str
    """The sqlAzureConnectionString secret name to create."""


class SecurityAlertPolicy(TypedDict, total=False):
    """The security alert policies to create in the server."""
    name: Required[str]
    """The name of the Security Alert Policy."""
    disabledAlerts: Literal['Access_Anomaly', 'Brute_Force', 'Data_Exfiltration', 'Sql_Injection', 'Sql_Injection_Vulnerability', 'Unsafe_Action']
    """Alerts to disable."""
    emailAccountAdmins: bool
    """Specifies that the alert is sent to the account administrators."""
    emailAddresses: List[object]
    """Specifies an array of email addresses to which the alert is sent."""
    retentionDays: int
    """Specifies the number of days to keep in the Threat Detection audit logs."""
    state: Literal['Disabled', 'Enabled']
    """Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database."""
    storageAccountAccessKey: str
    """Specifies the identifier key of the Threat Detection audit storage account."""
    storageEndpoint: str
    """Specifies the blob storage endpoint. This blob storage will hold all Threat Detection audit logs."""


class VirtualNetworkRule(TypedDict, total=False):
    """The virtual network rules to create in the server."""
    name: Required[str]
    """The name of the Server Virtual Network Rule."""
    virtualNetworkSubnetId: Required[str]
    """The resource ID of the virtual network subnet."""
    ignoreMissingVnetServiceEndpoint: bool
    """Allow creating a firewall rule before the virtual network has vnet service endpoint enabled."""


class RecurringScan(TypedDict, total=False):
    """The recurring scans settings."""
    emails: Required[List[object]]
    """Specifies an array of e-mail addresses to which the scan notification is sent."""
    emailSubscriptionAdmins: bool
    """Specifies that the schedule scan notification will be sent to the subscription administrators."""
    isEnabled: bool
    """Recurring scans state."""


class VulnerabilityAssessmentsObj(TypedDict, total=False):
    """The vulnerability assessment configuration."""
    name: Required[str]
    """The name of the vulnerability assessment."""
    storageAccountResourceId: Required[str]
    """The resource ID of the storage account to store the scan reports."""
    createStorageRoleAssignment: bool
    """Specifies whether to create a role assignment for the storage account."""
    recurringScans: 'RecurringScan'
    """The recurring scans settings."""
    useStorageAccountAccessKey: bool
    """Specifies whether to use the storage account access key to access the storage account."""


class SqlServer(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the server."""
    administratorLogin: str
    """The administrator username for the server. Required if no """
    administratorLoginPassword: str
    """The administrator login password. Required if no """
    administrators: 'Administrator'
    """The Azure Active Directory (AAD) administrator authentication. Required if no """
    primaryUserAssignedIdentityId: str
    """The resource ID of a user assigned identity to be used by default. Required if "userAssignedIdentities" is not empty."""
    auditSettings: 'AuditSetting'
    """The audit settings configuration."""
    databases: List['Database']
    """The databases to create in the server."""
    elasticPools: List['ElasticPool']
    """The Elastic Pools to create in the server."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionProtectorObj: 'EncryptionProtectorObj'
    """The encryption protection configuration."""
    federatedClientId: str
    """The Client id used for cross tenant CMK scenario."""
    firewallRules: List['FirewallRule']
    """The firewall rules to create in the server."""
    isIPv6Enabled: Literal['Disabled', 'Enabled']
    """Whether or not to enable IPv6 support for this server."""
    keyId: str
    """A CMK URI of the key to use for encryption."""
    keys: List['Key']
    """The keys to configure."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    minimalTlsVersion: Literal['1.0', '1.1', '1.2', '1.3']
    """Minimal TLS version allowed."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    publicNetworkAccess: Literal['', 'Disabled', 'Enabled', 'SecuredByPerimeter']
    """Whether or not public network access is allowed for this resource. For security reasons it should be disabled. If not specified, it will be disabled by default if private endpoints are set and neither firewall rules nor virtual network rules are set."""
    restrictOutboundNetworkAccess: Literal['', 'Disabled', 'Enabled']
    """Whether or not to restrict outbound network access for this server."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    secretsExportConfiguration: 'SecretsExportConfiguration'
    """Key vault reference and secret settings for the module's secrets export."""
    securityAlertPolicies: List['SecurityAlertPolicy']
    """The security alert policies to create in the server."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualNetworkRules: List['VirtualNetworkRule']
    """The virtual network rules to create in the server."""
    vulnerabilityAssessmentsObj: 'VulnerabilityAssessmentsObj'
    """The vulnerability assessment configuration."""


class SqlServerOutputs(TypedDict, total=False):
    """Outputs for SqlServer"""
    exportedSecrets: Output[Literal['object']]
    """A hashtable of references to the secrets exported to the provided Key Vault. The key of each reference is each secret's name."""
    fullyQualifiedDomainName: Output[Literal['string']]
    """The fully qualified domain name of the deployed SQL server."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed SQL server."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the SQL server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed SQL server."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed SQL server."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class SqlServerBicep(Module):
    outputs: SqlServerOutputs


def sql_server(
        bicep: IO[str],
        params: SqlServer,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> SqlServerBicep:
    symbol = "sql_server_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/sql/server:{tag}' = {{\n")
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
    output = SqlServerBicep(symbol)
    output.outputs = {
            'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
            'fullyQualifiedDomainName': Output(symbol, 'fullyQualifiedDomainName', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
