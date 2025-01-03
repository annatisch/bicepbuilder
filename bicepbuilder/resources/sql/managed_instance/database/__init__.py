from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to '' to disable log collection."""
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to 'AllLogs' to collect all logs."""


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to '' to disable log collection."""
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


class Database(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the SQL managed instance database."""
    longTermRetentionBackupResourceId: str
    """The resource ID of the Long Term Retention backup to be used for restore of this managed database. Required if createMode is RestoreLongTermRetentionBackup."""
    recoverableDatabaseId: str
    """The resource identifier of the recoverable database associated with create operation of this database. Required if createMode is Recovery."""
    restorePointInTime: str
    """Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. Required if createMode is PointInTimeRestore."""
    sourceDatabaseId: str
    """The resource identifier of the source database associated with create operation of this database. Required if createMode is PointInTimeRestore."""
    storageContainerSasToken: str
    """Specifies the storage container sas token. Required if createMode is RestoreExternalBackup."""
    storageContainerUri: str
    """Specifies the uri of the storage container where backups for this restore are stored. Required if createMode is RestoreExternalBackup."""
    backupLongTermRetentionPoliciesObj: Dict[str, object]
    """The configuration for the backup long term retention policy definition."""
    backupShortTermRetentionPoliciesObj: Dict[str, object]
    """The configuration for the backup short term retention policy definition."""
    catalogCollation: str
    """Collation of the managed instance."""
    collation: str
    """Collation of the managed instance database."""
    createMode: Literal['Default', 'PointInTimeRestore', 'Recovery', 'RestoreExternalBackup', 'RestoreLongTermRetentionBackup']
    """Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required)."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    restorableDroppedDatabaseId: str
    """The restorable dropped database resource ID to restore when creating this database."""
    tags: Dict[str, object]
    """Tags of the resource."""


class DatabaseOutputs(TypedDict, total=False):
    """Outputs for Database"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed database."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the database was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed database."""


class DatabaseModule(Module):
    outputs: DatabaseOutputs

