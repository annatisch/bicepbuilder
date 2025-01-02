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
    from .authorization_rule import AuthorizationRule
    from .consumergroup import Consumergroup


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Event Hubs Data Owner', 'Azure Event Hubs Data Receiver', 'Azure Event Hubs Data Sender', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Eventhub(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the event hub."""
    authorizationRules: List['AuthorizationRule']
    """Authorization Rules for the event hub."""
    captureDescriptionDestinationArchiveNameFormat: str
    """Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order."""
    captureDescriptionDestinationBlobContainer: str
    """Blob container Name."""
    captureDescriptionDestinationName: str
    """Name for capture destination."""
    captureDescriptionDestinationStorageAccountResourceId: str
    """Resource ID of the storage account to be used to create the blobs."""
    captureDescriptionEnabled: bool
    """A value that indicates whether capture description is enabled."""
    captureDescriptionEncoding: Literal['Avro', 'AvroDeflate']
    """Enumerates the possible values for the encoding format of capture description. Note: "AvroDeflate" will be deprecated in New API Version."""
    captureDescriptionIntervalInSeconds: int
    """The time window allows you to set the frequency with which the capture to Azure Blobs will happen."""
    captureDescriptionSizeLimitInBytes: int
    """The size window defines the amount of data built up in your Event Hub before an capture operation."""
    captureDescriptionSkipEmptyArchives: bool
    """A value that indicates whether to Skip Empty Archives."""
    consumergroups: List['Consumergroup']
    """The consumer groups to create in this event hub instance."""
    lock: 'Lock'
    """The lock settings of the service."""
    messageRetentionInDays: int
    """Number of days to retain the events for this Event Hub, value should be 1 to 7 days. Will be automatically set to infinite retention if cleanup policy is set to "Compact"."""
    partitionCount: int
    """Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions."""
    retentionDescriptionCleanupPolicy: Literal['Compact', 'Delete']
    """Retention cleanup policy. Enumerates the possible values for cleanup policy."""
    retentionDescriptionRetentionTimeInHours: int
    """Retention time in hours. Number of hours to retain the events for this Event Hub. This value is only used when cleanupPolicy is Delete. If cleanupPolicy is Compact the returned value of this property is Long.MaxValue."""
    retentionDescriptionTombstoneRetentionTimeInHours: int
    """Retention cleanup policy. Number of hours to retain the tombstone markers of a compacted Event Hub. This value is only used when cleanupPolicy is Compact. Consumer must complete reading the tombstone marker within this specified amount of time if consumer begins from starting offset to ensure they get a valid snapshot for the specific key described by the tombstone marker within the compacted Event Hub."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of the Event Hub."""


class EventhubOutputs(TypedDict, total=False):
    """Outputs for Eventhub"""
    name: Output[Literal['string']]
    """The name of the event hub."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the event hub was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the event hub."""


class EventhubBicep(Module):
    outputs: EventhubOutputs

