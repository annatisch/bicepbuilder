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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class NetworkNatGateway(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Azure Bastion resource."""
    zone: Required[Literal[0, 1, 2, 3]]
    """A list of availability zones denoting the zone in which Nat Gateway should be deployed."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    idleTimeoutInMinutes: int
    """The idle timeout of the NAT gateway."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    publicIPAddressObjects: List[object]
    """Specifies the properties of the Public IPs to create and be used by the NAT Gateway."""
    publicIPPrefixObjects: List[object]
    """Specifies the properties of the Public IP Prefixes to create and be used by the NAT Gateway."""
    publicIPPrefixResourceIds: List[object]
    """Existing Public IP Prefixes resource IDs to use for the NAT Gateway."""
    publicIpResourceIds: List[object]
    """Existing Public IP Address resource IDs to use for the NAT Gateway."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags for the resource."""


class NetworkNatGatewayOutputs(TypedDict, total=False):
    """Outputs for NetworkNatGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the NAT Gateway."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the NAT Gateway was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the NAT Gateway."""


class NetworkNatGatewayModule(Module):
    outputs: NetworkNatGatewayOutputs

