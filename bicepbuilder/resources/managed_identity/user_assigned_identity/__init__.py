from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class FederatedIdentityCredential(TypedDict, total=False):
    """The federated identity credentials list to indicate which token from the external IdP should be trusted by your application. Federated identity credentials are supported on applications only. A maximum of 20 federated identity credentials can be added per application object."""
    audiences: Required[List[object]]
    """The list of audiences that can appear in the issued token."""
    issuer: Required[str]
    """The URL of the issuer to be trusted."""
    name: Required[str]
    """The name of the federated identity credential."""
    subject: Required[str]
    """The identifier of the external identity."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Managed Identity Contributor', 'Managed Identity Operator', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class ManagedIdentityUserAssignedIdentity(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the User Assigned Identity."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    federatedIdentityCredentials: List['FederatedIdentityCredential']
    """The federated identity credentials list to indicate which token from the external IdP should be trusted by your application. Federated identity credentials are supported on applications only. A maximum of 20 federated identity credentials can be added per application object."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""


class ManagedIdentityUserAssignedIdentityOutputs(TypedDict, total=False):
    """Outputs for ManagedIdentityUserAssignedIdentity"""
    clientId: Output[Literal['string']]
    """The client ID (application ID) of the user assigned identity."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the user assigned identity."""
    principalId: Output[Literal['string']]
    """The principal ID (object ID) of the user assigned identity."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the user assigned identity was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the user assigned identity."""


class ManagedIdentityUserAssignedIdentityModule(Module):
    outputs: ManagedIdentityUserAssignedIdentityOutputs

