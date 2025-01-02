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


class BackupLongTermRetentionPolicy(TypedDict, total=False):
    """The long term backup retention policy to create for the database."""
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
    """The short term backup retention policy to create for the database."""
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
    """"""
    name: Required[str]
    """The name of the database."""
    autoPauseDelay: int
    """Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled."""
    availabilityZone: Literal['1', '2', '3', 'NoPreference']
    """Specifies the availability zone the database is pinned to."""
    backupLongTermRetentionPolicy: 'BackupLongTermRetentionPolicy'
    """The long term backup retention policy to create for the database."""
    backupShortTermRetentionPolicy: 'BackupShortTermRetentionPolicy'
    """The short term backup retention policy to create for the database."""
    catalogCollation: str
    """Collation of the metadata catalog."""
    collation: str
    """The collation of the database."""
    createMode: Literal['Copy', 'Default', 'OnlineSecondary', 'PointInTimeRestore', 'Recovery', 'Restore', 'RestoreExternalBackup', 'RestoreExternalBackupSecondary', 'RestoreLongTermRetentionBackup', 'Secondary']
    """Specifies the mode of database creation."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    elasticPoolResourceId: str
    """The resource ID of the elastic pool containing this database."""
    encryptionProtector: str
    """The azure key vault URI of the database if it's configured with per Database Customer Managed Keys."""
    encryptionProtectorAutoRotation: bool
    """The flag to enable or disable auto rotation of database encryption protector AKV key."""
    federatedClientId: str
    """The Client id used for cross tenant per database CMK scenario."""
    freeLimitExhaustionBehavior: Literal['AutoPause', 'BillOverUsage']
    """Specifies the behavior when monthly free limits are exhausted for the free database."""
    highAvailabilityReplicaCount: int
    """The number of readonly secondary replicas associated with the database."""
    isLedgerOn: bool
    """Whether or not this database is a ledger database, which means all tables in the database are ledger tables. Note: the value of this property cannot be changed after the database has been created."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this database."""
    location: str
    """Location for all resources."""
    longTermRetentionBackupResourceId: str
    """The resource identifier of the long term retention backup associated with create operation of this database."""
    maintenanceConfigurationId: str
    """Maintenance configuration ID assigned to the database. This configuration defines the period when the maintenance updates will occur."""
    manualCutover: bool
    """Whether or not customer controlled manual cutover needs to be done during Update Database operation to Hyperscale tier."""
    maxSizeBytes: int
    """The max size of the database expressed in bytes."""
    minCapacity: str
    """Minimal capacity that database will always have allocated."""
    performCutover: bool
    """To trigger customer controlled manual cutover during the wait state while Scaling operation is in progress."""
    preferredEnclaveType: Literal['Default', 'VBS']
    """Type of enclave requested on the database i.e. Default or VBS enclaves."""
    readScale: Literal['Disabled', 'Enabled']
    """The state of read-only routing."""
    recoverableDatabaseResourceId: str
    """The resource identifier of the recoverable database associated with create operation of this database."""
    recoveryServicesRecoveryPointResourceId: str
    """The resource identifier of the recovery point associated with create operation of this database."""
    requestedBackupStorageRedundancy: Literal['Geo', 'GeoZone', 'Local', 'Zone']
    """The storage account type to be used to store backups for this database."""
    restorableDroppedDatabaseResourceId: str
    """The resource identifier of the restorable dropped database associated with create operation of this database."""
    restorePointInTime: str
    """Point in time (ISO8601 format) of the source database to restore when createMode set to Restore or PointInTimeRestore."""
    sampleName: str
    """The name of the sample schema to apply when creating this database."""
    secondaryType: Literal['Geo', 'Named', 'Standby']
    """The secondary type of the database if it is a secondary."""
    sku: 'Sku'
    """The database SKU."""
    sourceDatabaseDeletionDate: str
    """The time that the database was deleted when restoring a deleted database."""
    sourceDatabaseResourceId: str
    """The resource identifier of the source database associated with create operation of this database."""
    sourceResourceId: str
    """The resource identifier of the source associated with the create operation of this database."""
    tags: Dict[str, object]
    """Tags of the resource."""
    useFreeLimit: bool
    """Whether or not the database uses free monthly limits. Allowed on one database in a subscription."""
    zoneRedundant: bool
    """Whether or not this database is zone redundant."""


class DatabaseOutputs(TypedDict, total=False):
    """Outputs for Database"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed database."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed database."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed database."""


class DatabaseBicep(Module):
    outputs: DatabaseOutputs

