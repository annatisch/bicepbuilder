from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class InboundEndpoint(TypedDict, total=False):
    """Inbound Endpoints for DNS Private Resolver."""
    name: Required[str]
    """Name of the inbound endpoint."""
    subnetResourceId: Required[str]
    """The reference to the subnet bound to the IP configuration."""
    location: str
    """Location for all resources."""
    privateIpAddress: str
    """Private IP address of the IP configuration."""
    privateIpAllocationMethod: Literal['Dynamic', 'Static']
    """Private IP address allocation method."""
    tags: Dict[str, object]
    """Tags for the resource."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class OutboundEndpoint(TypedDict, total=False):
    """Outbound Endpoints for DNS Private Resolver."""
    name: Required[str]
    """Name of the outbound endpoint."""
    subnetResourceId: Required[str]
    """ResourceId of the subnet to attach the outbound endpoint to."""
    location: str
    """Location for all resources."""
    tags: Dict[str, object]
    """Tags of the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator']]]
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


class NetworkDnsResolver(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the DNS Private Resolver."""
    virtualNetworkResourceId: Required[str]
    """ResourceId of the virtual network to attach the DNS Private Resolver to."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    inboundEndpoints: List['InboundEndpoint']
    """Inbound Endpoints for DNS Private Resolver."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    outboundEndpoints: List['OutboundEndpoint']
    """Outbound Endpoints for DNS Private Resolver."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NetworkDnsResolverOutputs(TypedDict, total=False):
    """Outputs for NetworkDnsResolver"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the DNS Private Resolver."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the DNS Private Resolver was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the DNS Private Resolver."""


class NetworkDnsResolverModule(Module):
    outputs: NetworkDnsResolverOutputs

