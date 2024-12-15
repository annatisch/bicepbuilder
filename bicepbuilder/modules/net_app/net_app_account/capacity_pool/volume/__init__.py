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


class Volume(TypedDict, total=False):
    """"""
    backupLabel: Required[str]
    """The label of the backup."""
    backupName: Required[str]
    """The name of the backup."""
    backupPolicyLocation: Required[str]
    """The backup policy location."""
    backupVaultResourceId: Required[str]
    """The Id of the Backup Vault."""
    coolAccess: Required[bool]
    """If enabled (true) the pool can contain cool Access enabled volumes."""
    coolnessPeriod: Required[int]
    """Specifies the number of days after which data that is not accessed by clients will be tiered."""
    dailyBackupsToKeep: Required[int]
    """The daily backups to keep."""
    dailyHour: Required[int]
    """The daily snapshot hour."""
    dailyMinute: Required[int]
    """The daily snapshot minute."""
    dailySnapshotsToKeep: Required[int]
    """Daily snapshot count to keep."""
    dailyUsedBytes: Required[int]
    """Daily snapshot used bytes."""
    daysOfMonth: Required[str]
    """The monthly snapshot day."""
    encryptionKeySource: Required[str]
    """The source of the encryption key."""
    endpointType: Required[str]
    """Indicates whether the local volume is the source or destination for the Volume Replication (src/dst)."""
    hourlyMinute: Required[int]
    """The hourly snapshot minute."""
    hourlySnapshotsToKeep: Required[int]
    """Hourly snapshot count to keep."""
    hourlyUsedBytes: Required[int]
    """Hourly snapshot used bytes."""
    keyVaultPrivateEndpointResourceId: Required[str]
    """The resource ID of the key vault private endpoint."""
    monthlyBackupsToKeep: Required[int]
    """The monthly backups to keep."""
    monthlyHour: Required[int]
    """The monthly snapshot hour."""
    monthlyMinute: Required[int]
    """The monthly snapshot minute."""
    monthlySnapshotsToKeep: Required[int]
    """Monthly snapshot count to keep."""
    monthlyUsedBytes: Required[int]
    """Monthly snapshot used bytes."""
    name: Required[str]
    """The name of the pool volume."""
    remoteVolumeRegion: Required[str]
    """The remote region for the other end of the Volume Replication."""
    remoteVolumeResourceId: Required[str]
    """The resource ID of the remote volume."""
    replicationSchedule: Required[str]
    """The replication schedule for the volume."""
    snapshotName: Required[str]
    """The name of the snapshot."""
    snapshotPolicyLocation: Required[str]
    """The location of snashot policies."""
    snapshotPolicyName: Required[str]
    """The name of the snapshot policy."""
    subnetResourceId: Required[str]
    """The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes."""
    usageThreshold: Required[int]
    """Maximum storage quota allowed for a file system in bytes."""
    useExistingSnapshot: Required[bool]
    """Indicates whether to use an existing snapshot."""
    volumeResourceId: Required[str]
    """The resource ID of the volume."""
    volumeType: Required[str]
    """The type of the volume. DataProtection volumes are used for replication."""
    weeklyBackupsToKeep: Required[int]
    """The weekly backups to keep."""
    weeklyDay: Required[str]
    """The weekly snapshot day."""
    weeklyHour: Required[int]
    """The weekly snapshot hour."""
    weeklyMinute: Required[int]
    """The weekly snapshot minute."""
    weeklySnapshotsToKeep: Required[int]
    """Weekly snapshot count to keep."""
    weeklyUsedBytes: Required[int]
    """Weekly snapshot used bytes."""
    backupEnabled: bool
    """Indicates whether the backup policy is enabled."""
    backupPolicyName: str
    """The name of the backup policy."""
    backupVaultLocation: str
    """The location of the backup vault."""
    backupVaultName: str
    """The name of the backup vault."""
    coolAccessRetrievalPolicy: str
    """determines the data retrieval behavior from the cool tier to standard storage based on the read pattern for cool access enabled volumes (Default/Never/Read)."""
    creationToken: str
    """A unique file path for the volume. This is the name of the volume export. A volume is mounted using the export path. File path must start with an alphabetical character and be unique within the subscription."""
    exportPolicyRules: List[object]
    """Export policy rules."""
    location: str
    """Location of the pool volume."""
    networkFeatures: Literal['Basic', 'Basic_Standard', 'Standard', 'Standard_Basic']
    """Network feature for the volume."""
    policyEnforced: bool
    """If Backup policy is enforced."""
    protocolTypes: List[object]
    """Set of protocol types."""
    replicationEnabled: bool
    """Enables replication."""
    serviceLevel: Literal['Premium', 'Standard', 'StandardZRS', 'Ultra']
    """The pool service level. Must match the one of the parent capacity pool."""
    smbContinuouslyAvailable: bool
    """Enables continuously available share property for SMB volume. Only applicable for SMB volume."""
    smbEncryption: bool
    """Enables SMB encryption. Only applicable for SMB/DualProtocol volume."""
    smbNonBrowsable: Literal['Disabled', 'Enabled']
    """Enables non-browsable property for SMB Shares. Only applicable for SMB/DualProtocol volume."""
    snapEnabled: bool
    """Indicates whether the snapshot policy is enabled."""
    zones: List[object]
    """Zone where the volume will be placed."""


class VolumeOutputs(TypedDict, total=False):
    """Outputs for Volume"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Volume."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Volume was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the Volume."""


class VolumeBicep(Module):
    outputs: VolumeOutputs

