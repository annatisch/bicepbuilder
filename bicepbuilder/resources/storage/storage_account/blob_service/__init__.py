from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .container import Container


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


class BlobService(TypedDict, total=False):
    """"""
    automaticSnapshotPolicyEnabled: bool
    """Automatic Snapshot is enabled if set to true."""
    changeFeedEnabled: bool
    """The blob service properties for change feed events. Indicates whether change feed event logging is enabled for the Blob service."""
    changeFeedRetentionInDays: int
    """Indicates whether change feed event logging is enabled for the Blob service. Indicates the duration of changeFeed retention in days. If left blank, it indicates an infinite retention of the change feed."""
    containerDeleteRetentionPolicyAllowPermanentDelete: bool
    """This property when set to true allows deletion of the soft deleted blob versions and snapshots. This property cannot be used with blob restore policy. This property only applies to blob service and does not apply to containers or file share."""
    containerDeleteRetentionPolicyDays: int
    """Indicates the number of days that the deleted item should be retained."""
    containerDeleteRetentionPolicyEnabled: bool
    """The blob service properties for container soft delete. Indicates whether DeleteRetentionPolicy is enabled."""
    containers: List['Container']
    """Blob containers to create."""
    corsRules: List[object]
    """Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service."""
    defaultServiceVersion: str
    """Indicates the default version to use for requests to the Blob service if an incoming request's version is not specified. Possible values include version 2008-10-27 and all more recent versions."""
    deleteRetentionPolicyAllowPermanentDelete: bool
    """This property when set to true allows deletion of the soft deleted blob versions and snapshots. This property cannot be used with blob restore policy. This property only applies to blob service and does not apply to containers or file share."""
    deleteRetentionPolicyDays: int
    """Indicates the number of days that the deleted blob should be retained."""
    deleteRetentionPolicyEnabled: bool
    """The blob service properties for blob soft delete."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    isVersioningEnabled: bool
    """Use versioning to automatically maintain previous versions of your blobs."""
    lastAccessTimeTrackingPolicyEnabled: bool
    """The blob service property to configure last access time based tracking policy. When set to true last access time based tracking is enabled."""
    restorePolicyDays: int
    """How long this blob can be restored. It should be less than DeleteRetentionPolicy days."""
    restorePolicyEnabled: bool
    """The blob service properties for blob restore policy. If point-in-time restore is enabled, then versioning, change feed, and blob soft delete must also be enabled."""


class BlobServiceOutputs(TypedDict, total=False):
    """Outputs for BlobService"""
    name: Output[Literal['string']]
    """The name of the deployed blob service."""
    resourceGroupName: Output[Literal['string']]
    """The name of the deployed blob service."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed blob service."""


class BlobServiceModule(Module):
    outputs: BlobServiceOutputs

