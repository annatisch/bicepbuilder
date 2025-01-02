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


class Subnet(TypedDict, total=False):
    """"""
    name: Required[str]
    """The Name of the subnet resource."""
    addressPrefix: str
    """The address prefix for the subnet. Required if """
    addressPrefixes: List[object]
    """List of address prefixes for the subnet. Required if """
    applicationGatewayIPConfigurations: List[object]
    """Application gateway IP configurations of virtual network resource."""
    defaultOutboundAccess: bool
    """Set this property to false to disable default outbound connectivity for all VMs in the subnet. This property can only be set at the time of subnet creation and cannot be updated for an existing subnet."""
    delegation: str
    """The delegation to enable on the subnet."""
    natGatewayResourceId: str
    """The resource ID of the NAT Gateway to use for the subnet."""
    networkSecurityGroupResourceId: str
    """The resource ID of the network security group to assign to the subnet."""
    privateEndpointNetworkPolicies: Literal['Disabled', 'Enabled', 'NetworkSecurityGroupEnabled', 'RouteTableEnabled']
    """Enable or disable apply network policies on private endpoint in the subnet."""
    privateLinkServiceNetworkPolicies: Literal['Disabled', 'Enabled']
    """Enable or disable apply network policies on private link service in the subnet."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    routeTableResourceId: str
    """The resource ID of the route table to assign to the subnet."""
    serviceEndpointPolicies: List[object]
    """An array of service endpoint policies."""
    serviceEndpoints: List[object]
    """The service endpoints to enable on the subnet."""
    sharingScope: Literal['DelegatedServices', 'Tenant']
    """Set this property to Tenant to allow sharing subnet with other subscriptions in your AAD tenant. This property can only be set if defaultOutboundAccess is set to false, both properties can only be set if subnet is empty."""


class SubnetOutputs(TypedDict, total=False):
    """Outputs for Subnet"""
    addressPrefix: Output[Literal['string']]
    """The address prefix for the subnet."""
    addressPrefixes: Output[Literal['array']]
    """List of address prefixes for the subnet."""
    name: Output[Literal['string']]
    """The name of the virtual network peering."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual network peering was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual network peering."""


class SubnetBicep(Module):
    outputs: SubnetOutputs

