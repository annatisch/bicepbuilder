from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .authorization_rule import AuthorizationRule


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Relay Listener', 'Azure Relay Owner', 'Azure Relay Sender', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class HybridConnection(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the hybrid connection."""
    userMetadata: Required[str]
    """The user metadata is a placeholder to store user-defined string data for the hybrid connection endpoint. For example, it can be used to store descriptive data, such as a list of teams and their contact information. Also, user-defined configuration settings can be stored."""
    authorizationRules: List['AuthorizationRule']
    """Authorization Rules for the Relay Hybrid Connection."""
    lock: 'Lock'
    """The lock settings of the service."""
    requiresClientAuthorization: bool
    """A value indicating if this hybrid connection requires client authorization."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""


class HybridConnectionOutputs(TypedDict, total=False):
    """Outputs for HybridConnection"""
    name: Output[Literal['string']]
    """The name of the deployed hybrid connection."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed hybrid connection."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed hybrid connection."""


class HybridConnectionModule(Module):
    outputs: HybridConnectionOutputs

