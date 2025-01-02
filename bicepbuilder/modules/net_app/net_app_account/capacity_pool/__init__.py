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
    from .volume import Volume


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


class CapacityPool(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the capacity pool."""
    size: Required[int]
    """Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104)."""
    coolAccess: bool
    """If enabled (true) the pool can contain cool Access enabled volumes."""
    encryptionType: Literal['Double', 'Single']
    """Encryption type of the capacity pool, set encryption type for data at rest for this pool and all volumes in it. This value can only be set when creating new pool."""
    location: str
    """Location of the pool volume."""
    qosType: Literal['Auto', 'Manual']
    """The qos type of the pool."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    serviceLevel: Literal['Premium', 'Standard', 'StandardZRS', 'Ultra']
    """The pool service level."""
    tags: Dict[str, object]
    """Tags for all resources."""
    volumes: List['Volume']
    """List of volumnes to create in the capacity pool."""


class CapacityPoolOutputs(TypedDict, total=False):
    """Outputs for CapacityPool"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Capacity Pool."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Capacity Pool was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Capacity Pool."""
    volumeResourceId: Output[Literal['string']]
    """The resource IDs of the volume created in the capacity pool."""


class CapacityPoolBicep(Module):
    outputs: CapacityPoolOutputs

