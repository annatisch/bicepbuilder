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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Arc machine Administrator Login', 'Arc machine Contributor', 'Arc machine User Login', 'Windows Admin Center Administrator Login']]]
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


class HybridComputeMachine(TypedDict, total=False):
    """"""
    kind: Required[str]
    """Kind of Arc machine to be created. Possible values are: HCI, SCVMM, VMware."""
    name: Required[str]
    """The name of the Arc machine to be created. You should use a unique prefix to reduce name collisions in Active Directory."""
    osType: Literal['Linux', 'Windows']
    """Required if you are providing OS-type specified configurations, such as patch settings. The chosen OS type, either Windows or Linux."""
    privateLinkScopeResourceId: str
    """The resource ID of an Arc Private Link Scope which which to associate this machine. Required if you are using Private Link for Arc and your Arc Machine will resolve a Private Endpoint for connectivity to Azure."""
    clientPublicKey: str
    """The Public Key that the client provides to be used during initial resource onboarding."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    guestConfiguration: Dict[str, object]
    """The guest configuration for the Arc machine. Needs the Guest Configuration extension to be enabled."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    parentClusterResourceId: str
    """Parent cluster resource ID (Azure Stack HCI)."""
    patchAssessmentMode: Literal['AutomaticByPlatform', 'ImageDefault']
    """VM guest patching assessment mode. Set it to 'AutomaticByPlatform' to enable automatically check for updates every 24 hours."""
    patchMode: Literal['AutomaticByOS', 'AutomaticByPlatform', 'ImageDefault', 'Manual']
    """VM guest patching orchestration mode. 'AutomaticByOS' & 'Manual' are for Windows only, 'ImageDefault' for Linux only."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vmId: str
    """The GUID of the on-premises virtual machine from your hypervisor."""


class HybridComputeMachineOutputs(TypedDict, total=False):
    """Outputs for HybridComputeMachine"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the machine."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the VM was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the machine."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class HybridComputeMachineModule(Module):
    outputs: HybridComputeMachineOutputs

