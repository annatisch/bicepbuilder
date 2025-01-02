from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
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


class Container(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the storage container to deploy."""
    defaultEncryptionScope: str
    """Default the container to use specified encryption scope for all writes."""
    denyEncryptionScopeOverride: bool
    """Block override of encryption scope from the container default."""
    enableNfsV3AllSquash: bool
    """Enable NFSv3 all squash on blob container."""
    enableNfsV3RootSquash: bool
    """Enable NFSv3 root squash on blob container."""
    immutabilityPolicyName: str
    """Name of the immutable policy."""
    immutabilityPolicyProperties: Dict[str, object]
    """Configure immutability policy."""
    immutableStorageWithVersioningEnabled: bool
    """This is an immutable property, when set to true it enables object level immutability at the container level. The property is immutable and can only be set to true at the container creation time. Existing containers must undergo a migration process."""
    metadata: Dict[str, object]
    """A name-value pair to associate with the container as metadata."""
    publicAccess: Literal['Blob', 'Container', 'None']
    """Specifies whether data in the container may be accessed publicly and the level of access."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Reader and Data Access', 'Role Based Access Control Administrator', 'Storage Account Backup Contributor', 'Storage Account Contributor', 'Storage Account Key Operator Service Role', 'Storage Blob Data Contributor', 'Storage Blob Data Owner', 'Storage Blob Data Reader', 'Storage Blob Delegator', 'User Access Administrator']]]
    """Array of role assignments to create."""


class ContainerOutputs(TypedDict, total=False):
    """Outputs for Container"""
    name: Output[Literal['string']]
    """The name of the deployed container."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed container."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed container."""


class ContainerBicep(Module):
    outputs: ContainerOutputs

