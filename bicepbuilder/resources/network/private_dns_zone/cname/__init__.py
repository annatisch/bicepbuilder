from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Cname(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the CNAME record."""
    cnameRecord: Dict[str, object]
    """A CNAME record."""
    metadata: Dict[str, object]
    """The metadata attached to the record set."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL (time-to-live) of the records in the record set."""


class CnameOutputs(TypedDict, total=False):
    """Outputs for Cname"""
    name: Output[Literal['string']]
    """The name of the deployed CNAME record."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed CNAME record."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed CNAME record."""


class CnameModule(Module):
    outputs: CnameOutputs

