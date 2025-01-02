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


class Parameter(TypedDict, total=False):
    """The parameters that this custom action uses."""
    name: Required[str]
    """The name of the parameter."""
    defaultValue: str
    """The default value of the parameter. Only applies to string types."""
    description: str
    """A description to help users understand what this parameter means."""
    required: bool
    """Indicates whether this parameter must be passed when running the custom action."""
    type: Literal['ConfigurationDataBlob', 'LogOutputBlob', 'String']
    """Specifies the type of the custom action parameter."""


class CustomAction(TypedDict, total=False):
    """A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application."""
    name: Required[str]
    """The name of the custom action. Must be unique within the Gallery Application Version."""
    script: Required[str]
    """The script to run when executing this custom action."""
    description: str
    """Description to help the users understand what this custom action does."""
    parameters: List['Parameter']
    """The parameters that this custom action uses."""


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


class Application(TypedDict, total=False):
    """Applications to create."""
    name: Required[str]
    """Name of the application definition."""
    supportedOSType: Required[Literal['Linux', 'Windows']]
    """The OS type of the application."""
    customActions: List['CustomAction']
    """A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application."""
    description: str
    """The description of this gallery application definition resource. This property is updatable."""
    endOfLifeDate: str
    """The end of life date of the gallery application definition. This property can be used for decommissioning purposes. This property is updatable."""
    eula: str
    """The Eula agreement for the gallery application definition."""
    privacyStatementUri: str
    """The privacy statement uri."""
    releaseNoteUri: str
    """The release note uri. Has to be a valid URL."""
    roleAssignments: List[Union['RoleAssignment', Literal['Compute Gallery Sharing Admin', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags for all resources."""


class Identifier(TypedDict, total=False):
    """This is the gallery image definition identifier."""
    offer: Required[str]
    """The name of the gallery image definition offer."""
    publisher: Required[str]
    """The name of the gallery image definition publisher."""
    sku: Required[str]
    """The name of the gallery image definition SKU."""


class Memory(TypedDict, total=False):
    """Describes the resource range (1-4000 GB RAM). Defaults to min=4, max=16."""
    max: int
    """The minimum number of the resource."""
    min: int
    """The minimum number of the resource."""


class PurchasePlan(TypedDict, total=False):
    """Describes the gallery image definition purchase plan. This is used by marketplace images."""
    name: Required[str]
    """The plan ID."""
    product: Required[str]
    """The product ID."""
    publisher: Required[str]
    """The publisher ID."""


class VCPU(TypedDict, total=False):
    """Describes the resource range (1-128 CPU cores). Defaults to min=1, max=4."""
    max: int
    """The minimum number of the resource."""
    min: int
    """The minimum number of the resource."""


class Image(TypedDict, total=False):
    """Images to create."""
    identifier: Required['Identifier']
    """This is the gallery image definition identifier."""
    name: Required[str]
    """Name of the image definition."""
    osState: Required[Literal['Generalized', 'Specialized']]
    """This property allows the user to specify the state of the OS of the image."""
    osType: Required[Literal['Linux', 'Windows']]
    """This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image."""
    architecture: Literal['Arm64', 'x64']
    """The architecture of the image. Applicable to OS disks only."""
    description: str
    """The description of this gallery image definition resource. This property is updatable."""
    endOfLife: str
    """The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable."""
    eula: str
    """The Eula agreement for the gallery image definition."""
    excludedDiskTypes: List[object]
    """Describes the disallowed disk types."""
    hyperVGeneration: Literal['V1', 'V2']
    """The hypervisor generation of the Virtual Machine. If this value is not specified, then it is determined by the securityType parameter. If the securityType parameter is specified, then the value of hyperVGeneration will be V2, else V1."""
    isAcceleratedNetworkSupported: bool
    """Specify if the image supports accelerated networking. Defaults to true."""
    isHibernateSupported: bool
    """Specify if the image supports hibernation."""
    memory: 'Memory'
    """Describes the resource range (1-4000 GB RAM). Defaults to min=4, max=16."""
    privacyStatementUri: str
    """The privacy statement uri."""
    purchasePlan: 'PurchasePlan'
    """Describes the gallery image definition purchase plan. This is used by marketplace images."""
    releaseNoteUri: str
    """The release note uri. Has to be a valid URL."""
    securityType: Literal['ConfidentialVM', 'ConfidentialVMSupported', 'Standard', 'TrustedLaunch', 'TrustedLaunchAndConfidentialVmSupported', 'TrustedLaunchSupported']
    """The security type of the image. Requires a hyperVGeneration V2. Defaults to """
    vCPUs: 'VCPU'
    """Describes the resource range (1-128 CPU cores). Defaults to min=1, max=4."""


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


class ComputeGallery(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Azure Compute Gallery."""
    applications: List['Application']
    """Applications to create."""
    description: str
    """Description of the Azure Shared Image Gallery."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    images: List['Image']
    """Images to create."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List[Union['RoleAssignment', Literal['Compute Gallery Sharing Admin', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    sharingProfile: Dict[str, object]
    """Profile for gallery sharing to subscription or tenant."""
    softDeletePolicy: Dict[str, object]
    """Soft deletion policy of the gallery."""
    tags: Dict[str, object]
    """Tags for all resources."""


class ComputeGalleryOutputs(TypedDict, total=False):
    """Outputs for ComputeGallery"""
    imageResourceIds: Output[Literal['array']]
    """The resource ids of the deployed images."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed image gallery."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed image gallery."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed image gallery."""


class ComputeGalleryBicep(Module):
    outputs: ComputeGalleryOutputs


def compute_gallery(
        bicep: IO[str],
        params: ComputeGallery,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ComputeGalleryBicep:
    symbol = "compute_gallery_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/gallery:{tag}' = {{\n")
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
    output = ComputeGalleryBicep(symbol)
    output.outputs = {
            'imageResourceIds': Output(symbol, 'imageResourceIds', 'array'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
