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
    from .sender_username import SenderUsername


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


class Domain(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the domain to create."""
    domainManagement: Literal['AzureManaged', 'CustomerManaged', 'CustomerManagedInExchangeOnline']
    """Describes how the Domain resource is being managed."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    senderUsernames: List['SenderUsername']
    """The domains to deploy into this namespace."""
    tags: Dict[str, object]
    """Endpoint tags."""
    userEngagementTracking: Literal['Disabled', 'Enabled']
    """Describes whether user engagement tracking is enabled or disabled."""


class DomainOutputs(TypedDict, total=False):
    """Outputs for Domain"""
    name: Output[Literal['string']]
    """The name of the domain."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the domain was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the domain."""


class DomainBicep(Module):
    outputs: DomainOutputs

