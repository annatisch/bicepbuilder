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


class Queue(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the storage queue to deploy."""
    metadata: Dict[str, object]
    """A name-value pair that represents queue metadata."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Reader and Data Access', 'Role Based Access Control Administrator', 'Storage Account Backup Contributor', 'Storage Account Contributor', 'Storage Account Key Operator Service Role', 'Storage Queue Data Contributor', 'Storage Queue Data Message Processor', 'Storage Queue Data Message Sender', 'Storage Queue Data Reader', 'User Access Administrator']]]
    """Array of role assignments to create."""


class QueueOutputs(TypedDict, total=False):
    """Outputs for Queue"""
    name: Output[Literal['string']]
    """The name of the deployed queue."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed queue."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed queue."""


class QueueBicep(Module):
    outputs: QueueOutputs

