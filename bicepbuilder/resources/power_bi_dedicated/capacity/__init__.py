from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Sku(TypedDict, total=False):
    """Sku configuration of the resource."""
    capacity: Required[int]
    """The capacity of the SKU."""
    name: Literal['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
    """The name of the SKU."""
    tier: Literal['AutoPremiumHost', 'PBIE_Azure', 'Premium']
    """The tier of the SKU."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Log Analytics Contributor', 'Log Analytics Reader', 'Owner', 'Reader', 'Role Based Access Control Administrator (Preview)', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class PowerBiDedicatedCapacity(TypedDict, total=False):
    """"""
    members: Required[List[object]]
    """Members of the resource."""
    name: Required[str]
    """Name of the PowerBI Embedded."""
    sku: Required['Sku']
    """Sku configuration of the resource."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    mode: Literal['Gen1', 'Gen2']
    """Mode of the resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""


class PowerBiDedicatedCapacityOutputs(TypedDict, total=False):
    """Outputs for PowerBiDedicatedCapacity"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The Name of the PowerBi Embedded instance."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the PowerBi Embedded was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the PowerBi Embedded instance."""


class PowerBiDedicatedCapacityModule(Module):
    outputs: PowerBiDedicatedCapacityOutputs

