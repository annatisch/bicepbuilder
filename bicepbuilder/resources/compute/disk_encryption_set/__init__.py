from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. At least one identity type is required."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Data Operator for Managed Disks', 'Disk Backup Reader', 'Disk Pool Operator', 'Disk Restore Operator', 'Disk Snapshot Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class ComputeDiskEncryptionSet(TypedDict, total=False):
    """"""
    keyName: Required[str]
    """Key URL (with version) pointing to a key or secret in KeyVault."""
    keyVaultResourceId: Required[str]
    """Resource ID of the KeyVault containing the key or secret."""
    name: Required[str]
    """The name of the disk encryption set that is being created."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionType: Literal['EncryptionAtRestWithCustomerKey', 'EncryptionAtRestWithPlatformAndCustomerKeys']
    """The type of key used to encrypt the data of the disk. For security reasons, it is recommended to set encryptionType to EncryptionAtRestWithPlatformAndCustomerKeys."""
    federatedClientId: str
    """Multi-tenant application client ID to access key vault in a different tenant. Setting the value to "None" will clear the property."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the latest key version is used."""
    location: str
    """Resource location."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. At least one identity type is required."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    rotationToLatestKeyVersionEnabled: bool
    """Set this flag to true to enable auto-updating of this disk encryption set to the latest key version."""
    tags: Dict[str, object]
    """Tags of the disk encryption resource."""


class ComputeDiskEncryptionSetOutputs(TypedDict, total=False):
    """Outputs for ComputeDiskEncryptionSet"""
    identities: Output[Literal['object']]
    """The idenities of the disk encryption set."""
    keyVaultName: Output[Literal['string']]
    """The name of the key vault with the disk encryption key."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the disk encryption set."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the disk encryption set was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the disk encryption set."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class ComputeDiskEncryptionSetModule(Module):
    outputs: ComputeDiskEncryptionSetOutputs

