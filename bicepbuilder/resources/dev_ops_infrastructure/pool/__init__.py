from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Image(TypedDict, total=False):
    """The VM images of the machines in the pool."""
    resourceId: str
    """The specific resource id of the marketplace or compute gallery image. Required if """
    wellKnownImageName: str
    """The image to use from a well-known set of images made available to customers. Required if """
    aliases: List[object]
    """List of aliases to reference the image by."""
    buffer: str
    """The percentage of the buffer to be allocated to this image."""


class Organization(TypedDict, total=False):
    """The list of Azure DevOps organizations the pool should be present in.."""
    url: Required[str]
    """The Azure DevOps organization URL in which the pool should be created."""
    parallelism: int
    """How many machines can be created at maximum in this organization out of the maximumConcurrency of the pool."""
    projects: List[object]
    """List of projects in which the pool should be created."""


class PermissionProfile(TypedDict, total=False):
    """The type of permission which determines which accounts are admins on the Azure DevOps pool."""
    kind: Required[Literal['CreatorOnly', 'Inherit', 'SpecificAccounts']]
    """Determines who has admin permissions to the Azure DevOps pool."""
    groups: List[object]
    """Group email addresses."""
    users: List[object]
    """User email addresses."""


class OrganizationProfile(TypedDict, total=False):
    """Defines the organization in which the pool will be used."""
    kind: Required[Literal['AzureDevOps']]
    """Azure DevOps organization profile."""
    organizations: Required[List['Organization']]
    """The list of Azure DevOps organizations the pool should be present in.."""
    permissionProfile: 'PermissionProfile'
    """The type of permission which determines which accounts are admins on the Azure DevOps pool."""


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


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed service identities assigned to this resource."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class SecretsManagementSetting(TypedDict, total=False):
    """The secret management settings of the machines in the pool."""
    keyExportable: Required[bool]
    """The secret management settings of the machines in the pool."""
    observedCertificates: Required[List[object]]
    """The list of certificates to install on all machines in the pool."""
    certificateStoreLocation: str
    """Where to store certificates on the machine."""


class OsProfile(TypedDict, total=False):
    """The OS profile of the agents in the pool."""
    logonType: Required[Literal['Interactive', 'Service']]
    """The logon type of the machine."""
    secretsManagementSettings: 'SecretsManagementSetting'
    """The secret management settings of the machines in the pool."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator (Preview)', 'User Access Administrator']]]
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


class DataDisk(TypedDict, total=False):
    """A list of empty data disks to attach."""
    caching: Literal['None', 'ReadOnly', 'ReadWrite']
    """The type of caching to be enabled for the data disks. The default value for caching is readwrite. For information about the caching options see: https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/."""
    diskSizeGiB: int
    """The initial disk size in gigabytes."""
    driveLetter: str
    """The drive letter for the empty data disk. If not specified, it will be the first available letter. Letters A, C, D, and E are not allowed."""
    storageAccountType: Literal['Premium_LRS', 'Premium_ZRS', 'Standard_LRS', 'StandardSSD_LRS', 'StandardSSD_ZRS']
    """The storage Account type to be used for the data disk. If omitted, the default is Standard_LRS."""


class StorageProfile(TypedDict, total=False):
    """The storage profile of the machines in the pool."""
    dataDisks: List['DataDisk']
    """A list of empty data disks to attach."""
    osDiskStorageAccountType: Literal['Premium', 'Standard', 'StandardSSD']
    """The Azure SKU name of the machines in the pool."""


class DevOpsInfrastructurePool(TypedDict, total=False):
    """"""
    agentProfile: Required[Dict[str, object]]
    """Defines how the machine will be handled once it executed a job."""
    concurrency: Required[int]
    """Defines how many resources can there be created at any given time."""
    devCenterProjectResourceId: Required[str]
    """The resource id of the DevCenter Project the pool belongs to."""
    fabricProfileSkuName: Required[str]
    """The Azure SKU name of the machines in the pool."""
    images: Required[List['Image']]
    """The VM images of the machines in the pool."""
    name: Required[str]
    """Name of the pool. It needs to be globally unique."""
    organizationProfile: Required['OrganizationProfile']
    """Defines the organization in which the pool will be used."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """The geo-location where the resource lives."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed service identities assigned to this resource."""
    osProfile: 'OsProfile'
    """The OS profile of the agents in the pool."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    storageProfile: 'StorageProfile'
    """The storage profile of the machines in the pool."""
    subnetResourceId: str
    """The subnet id on which to put all machines created in the pool."""
    tags: Dict[str, object]
    """Tags of the resource."""


class DevOpsInfrastructurePoolOutputs(TypedDict, total=False):
    """Outputs for DevOpsInfrastructurePool"""
    location: Output[Literal['string']]
    """The location the Managed DevOps Pool resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Managed DevOps Pool."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Managed DevOps Pool resource was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Managed DevOps Pool."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class DevOpsInfrastructurePoolModule(Module):
    outputs: DevOpsInfrastructurePoolOutputs

