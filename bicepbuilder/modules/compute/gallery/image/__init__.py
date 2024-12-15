from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Identifier(TypedDict, total=False):
    """This is the gallery image definition identifier."""
    offer: Required[str]
    """The name of the gallery image definition offer."""
    publisher: Required[str]
    """The name of the gallery image definition publisher."""
    sku: Required[str]
    """The name of the gallery image definition SKU."""


class Disallowed(TypedDict, total=False):
    """Describes the disallowed disk types."""
    diskTypes: Required[List[object]]
    """A list of disk types."""


class Memory(TypedDict, total=False):
    """Describes the resource range (1-4000 GB RAM)."""
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


class VCPU(TypedDict, total=False):
    """Describes the resource range (1-128 CPU cores)."""
    max: int
    """The minimum number of the resource."""
    min: int
    """The minimum number of the resource."""


class Image(TypedDict, total=False):
    """"""
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
    endOfLifeDate: str
    """The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable."""
    eula: str
    """The Eula agreement for the gallery image definition."""
    hyperVGeneration: Literal['V1', 'V2']
    """The hypervisor generation of the Virtual Machine. If this value is not specified, then it is determined by the securityType parameter. If the securityType parameter is specified, then the value of hyperVGeneration will be V2, else V1."""
    isAcceleratedNetworkSupported: bool
    """Specify if the image supports accelerated networking."""
    isHibernateSupported: bool
    """Specifiy if the image supports hibernation."""
    location: str
    """Location for all resources."""
    privacyStatementUri: str
    """The privacy statement uri."""
    releaseNoteUri: str
    """The release note uri. Has to be a valid URL."""
    securityType: Literal['ConfidentialVM', 'ConfidentialVMSupported', 'Standard', 'TrustedLaunch', 'TrustedLaunchAndConfidentialVmSupported', 'TrustedLaunchSupported']
    """The security type of the image. Requires a hyperVGeneration V2."""
    tags: Dict[str, object]
    """Tags for all the image."""


class ImageOutputs(TypedDict, total=False):
    """Outputs for Image"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the image."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the image was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the image."""


class ImageBicep(Module):
    outputs: ImageOutputs

