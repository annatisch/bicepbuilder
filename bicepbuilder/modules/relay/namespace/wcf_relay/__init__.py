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


class WcfRelay(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the WCF Relay."""
    relayType: Required[Literal['Http', 'NetTcp']]
    """Type of WCF Relay."""
    authorizationRules: List['AuthorizationRule']
    """Authorization Rules for the WCF Relay."""
    lock: 'Lock'
    """The lock settings of the service."""
    requiresClientAuthorization: bool
    """A value indicating if this relay requires client authorization."""
    requiresTransportSecurity: bool
    """A value indicating if this relay requires transport security."""
    roleAssignments: List[Union['RoleAssignment', Literal['Azure Relay Listener', 'Azure Relay Owner', 'Azure Relay Sender', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    userMetadata: str
    """User-defined string data for the WCF Relay."""


class WcfRelayOutputs(TypedDict, total=False):
    """Outputs for WcfRelay"""
    name: Output[Literal['string']]
    """The name of the deployed wcf relay."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed wcf relay."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed wcf relay."""


class WcfRelayBicep(Module):
    outputs: WcfRelayOutputs

