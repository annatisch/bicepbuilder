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


class Secret(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the secret."""
    value: Required[str]
    """The value of the secret. NOTE: "value" will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets."""
    attributesEnabled: bool
    """Determines whether the object is enabled."""
    attributesExp: int
    """Expiry date in seconds since 1970-01-01T00:00:00Z. For security reasons, it is recommended to set an expiration date whenever possible."""
    attributesNbf: int
    """Not before date in seconds since 1970-01-01T00:00:00Z."""
    contentType: str
    """The content type of the secret."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Key Vault Administrator', 'Key Vault Contributor', 'Key Vault Reader', 'Key Vault Secrets Officer', 'Key Vault Secrets User', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Resource tags."""


class SecretOutputs(TypedDict, total=False):
    """Outputs for Secret"""
    name: Output[Literal['string']]
    """The name of the secret."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the secret was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the secret."""
    secretUri: Output[Literal['string']]
    """The uri of the secret."""
    secretUriWithVersion: Output[Literal['string']]
    """The uri with version of the secret."""


class SecretBicep(Module):
    outputs: SecretOutputs

