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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class NetworkPrivateLinkService(TypedDict, total=False):
    """"""
    ipConfigurations: Required[List[object]]
    """An array of private link service IP configurations. At least one IP configuration is required on the private link service."""
    loadBalancerFrontendIpConfigurations: Required[List[object]]
    """An array of references to the load balancer IP configurations. The Private Link service is tied to the frontend IP address of a Standard Load Balancer. All traffic destined for the service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running. Load balancer frontend IP configurations are different than NAT IP configurations. At least one load balancer frontend IP configuration is required on the private link service."""
    name: Required[str]
    """The name of the private link service to create."""
    autoApproval: Dict[str, object]
    """The auto-approval list of the private link service."""
    enableProxyProtocol: bool
    """Lets the service provider use tcp proxy v2 to retrieve connection information about the service consumer. Service Provider is responsible for setting up receiver configs to be able to parse the proxy protocol v2 header."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    extendedLocation: Dict[str, object]
    """The extended location of the load balancer."""
    fqdns: List[object]
    """The list of Fqdn."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""
    visibility: Dict[str, object]
    """Controls the exposure settings for your Private Link service. Service providers can choose to limit the exposure to their service to subscriptions with Azure role-based access control (Azure RBAC) permissions, a restricted set of subscriptions, or all Azure subscriptions."""


class NetworkPrivateLinkServiceOutputs(TypedDict, total=False):
    """Outputs for NetworkPrivateLinkService"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the private link service."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the private link service was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the private link service."""


class NetworkPrivateLinkServiceModule(Module):
    outputs: NetworkPrivateLinkServiceOutputs

