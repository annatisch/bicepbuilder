from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
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


class RouteProperties(TypedDict, total=False):
    """Properties of the route."""
    nextHopType: Required[Literal['Internet', 'None', 'VirtualAppliance', 'VirtualNetworkGateway', 'VnetLocal']]
    """The type of Azure hop the packet should be sent to."""
    addressPrefix: str
    """The destination CIDR to which the route applies."""
    hasBgpOverride: bool
    """A value indicating whether this route overrides overlapping BGP routes regardless of LPM."""
    nextHopIpAddress: str
    """The IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is VirtualAppliance."""


class Route(TypedDict, total=False):
    """An array of routes to be established within the hub route table."""
    name: Required[str]
    """Name of the route."""
    properties: Required['RouteProperties']
    """Properties of the route."""


class NetworkRouteTable(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name given for the hub route table."""
    disableBgpRoutePropagation: bool
    """Switch to disable BGP route propagation."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    routes: List['Route']
    """An array of routes to be established within the hub route table."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NetworkRouteTableOutputs(TypedDict, total=False):
    """Outputs for NetworkRouteTable"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the route table."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the route table was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the route table."""


class NetworkRouteTableBicep(Module):
    outputs: NetworkRouteTableOutputs


def network_route_table(
        bicep: IO[str],
        params: NetworkRouteTable,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkRouteTableBicep:
    symbol = "network_route_table_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/route-table:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = NetworkRouteTableBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
