from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


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


class ComputeImage(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the image."""
    osDiskBlobUri: Required[str]
    """The Virtual Hard Disk."""
    osType: Required[str]
    """This property allows you to specify the type of the OS that is included in the disk if creating a VM from a custom image. - Windows or Linux."""
    dataDisks: List[object]
    """Specifies the parameters that are used to add a data disk to a virtual machine."""
    diskEncryptionSetResourceId: str
    """Specifies the customer managed disk encryption set resource ID for the managed image disk."""
    diskSizeGB: int
    """Specifies the size of empty data disks in gigabytes. This element can be used to overwrite the name of the disk in a virtual machine image. This value cannot be larger than 1023 GB."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    extendedLocation: Dict[str, object]
    """The extended location of the Image."""
    hyperVGeneration: str
    """Gets the HyperVGenerationType of the VirtualMachine created from the image. - V1 or V2."""
    location: str
    """Location for all resources."""
    managedDiskResourceId: str
    """The managedDisk."""
    osAccountType: Required[str]
    """Specifies the storage account type for the managed disk. NOTE: UltraSSD_LRS can only be used with data disks, it cannot be used with OS Disk. - Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS."""
    osDiskCaching: Required[str]
    """Specifies the caching requirements. Default: None for Standard storage. ReadOnly for Premium storage. - None, ReadOnly, ReadWrite."""
    osState: Literal['Generalized', 'Specialized']
    """The OS State. For managed images, use Generalized."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    snapshotResourceId: str
    """The snapshot resource ID."""
    sourceVirtualMachineResourceId: str
    """The source virtual machine from which Image is created."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneResilient: bool
    """Default is false. Specifies whether an image is zone resilient or not. Zone resilient images can be created only in regions that provide Zone Redundant Storage (ZRS)."""


class ComputeImageOutputs(TypedDict, total=False):
    """Outputs for ComputeImage"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the image."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the image was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the image."""


class ComputeImageModule(Module):
    outputs: ComputeImageOutputs

