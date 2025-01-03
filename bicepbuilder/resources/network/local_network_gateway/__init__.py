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


class NetworkLocalNetworkGateway(TypedDict, total=False):
    """"""
    localAddressPrefixes: Required[List[object]]
    """List of the local (on-premises) IP address ranges."""
    localGatewayPublicIpAddress: Required[str]
    """Public IP of the local gateway."""
    name: Required[str]
    """Name of the Local Network Gateway."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    fqdn: str
    """FQDN of local network gateway."""
    localAsn: str
    """The BGP speaker's ASN. Not providing this value will automatically disable BGP on this Local Network Gateway resource."""
    localBgpPeeringAddress: str
    """The BGP peering address and BGP identifier of this BGP speaker. Not providing this value will automatically disable BGP on this Local Network Gateway resource."""
    localPeerWeight: str
    """The weight added to routes learned from this BGP speaker. This will only take effect if both the localAsn and the localBgpPeeringAddress values are provided."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NetworkLocalNetworkGatewayOutputs(TypedDict, total=False):
    """Outputs for NetworkLocalNetworkGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the local network gateway."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the local network gateway was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the local network gateway."""


class NetworkLocalNetworkGatewayModule(Module):
    outputs: NetworkLocalNetworkGatewayOutputs

