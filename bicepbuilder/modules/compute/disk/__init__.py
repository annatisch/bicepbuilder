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


class ComputeDisk(TypedDict, total=False):
    """"""
    availabilityZone: Required[Literal[0, 1, 2, 3]]
    """If set to 1, 2 or 3, the availability zone is hardcoded to that value. If zero, then availability zones are not used. Note that the availability zone number here are the logical availability zone in your Azure subscription. Different subscriptions might have a different mapping of the physical zone and logical zone.To understand more, please refer to """
    name: Required[str]
    """The name of the disk that is being created."""
    sku: Required[Literal['Premium_LRS', 'Premium_ZRS', 'PremiumV2_LRS', 'Standard_LRS', 'StandardSSD_LRS', 'UltraSSD_LRS']]
    """The disks sku name. Can be ."""
    diskSizeGB: int
    """The size of the disk to create. Required if create option is Empty."""
    storageAccountId: str
    """The resource ID of the storage account containing the blob to import as a disk. Required if create option is Import."""
    acceleratedNetwork: bool
    """True if the image from which the OS disk is created supports accelerated networking."""
    architecture: Literal['', 'Arm64', 'x64']
    """CPU architecture supported by an OS disk."""
    burstingEnabled: bool
    """Set to true to enable bursting beyond the provisioned performance target of the disk."""
    completionPercent: int
    """Percentage complete for the background copy when a resource is created via the CopyStart operation."""
    createOption: Literal['Attach', 'Copy', 'CopyStart', 'Empty', 'FromImage', 'Import', 'ImportSecure', 'Restore', 'Upload', 'UploadPreparedSecure']
    """Sources of a disk creation."""
    diskIOPSReadWrite: int
    """The number of IOPS allowed for this disk; only settable for UltraSSD disks."""
    diskMBpsReadWrite: int
    """The bandwidth allowed for this disk; only settable for UltraSSD disks."""
    edgeZone: Literal['', 'EdgeZone']
    """Specifies the Edge Zone within the Azure Region where this Managed Disk should exist. Changing this forces a new Managed Disk to be created."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    hyperVGeneration: Literal['V1', 'V2']
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only."""
    imageReferenceId: str
    """A relative uri containing either a Platform Image Repository or user image reference."""
    location: str
    """Resource location."""
    lock: 'Lock'
    """The lock settings of the service."""
    logicalSectorSize: int
    """Logical sector size in bytes for Ultra disks. Supported values are 512 ad 4096."""
    maxShares: int
    """The maximum number of VMs that can attach to the disk at the same time. Default value is 0."""
    networkAccessPolicy: Literal['AllowAll', 'AllowPrivate', 'DenyAll']
    """Policy for accessing the disk via network."""
    optimizedForFrequentAttach: bool
    """Setting this property to true improves reliability and performance of data disks that are frequently (more than 5 times a day) by detached from one virtual machine and attached to another. This property should not be set for disks that are not detached and attached frequently as it causes the disks to not align with the fault domain of the virtual machine."""
    osType: Literal['', 'Linux', 'Windows']
    """Sources of a disk creation."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Policy for controlling export on the disk."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Data Operator for Managed Disks', 'Disk Backup Reader', 'Disk Pool Operator', 'Disk Restore Operator', 'Disk Snapshot Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    securityDataUri: str
    """If create option is ImportSecure, this is the URI of a blob to be imported into VM guest state."""
    sourceResourceId: str
    """If create option is Copy, this is the ARM ID of the source snapshot or disk."""
    sourceUri: str
    """If create option is Import, this is the URI of a blob to be imported into a managed disk."""
    tags: Dict[str, object]
    """Tags of the availability set resource."""
    uploadSizeBytes: int
    """If create option is Upload, this is the size of the contents of the upload including the VHD footer."""


class ComputeDiskOutputs(TypedDict, total=False):
    """Outputs for ComputeDisk"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the disk."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the  disk was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the disk."""


class ComputeDiskBicep(Module):
    outputs: ComputeDiskOutputs


def compute_disk(
        bicep: IO[str],
        params: ComputeDisk,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ComputeDiskBicep:
    symbol = "compute_disk_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/disk:{tag}' = {{\n")
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
    output = ComputeDiskBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
