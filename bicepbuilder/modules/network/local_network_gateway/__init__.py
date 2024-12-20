from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
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


class LocalNetworkGateway(TypedDict, total=False):
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
    tags: Dict[str, object]
    """Tags of the resource."""


class LocalNetworkGatewayOutputs(TypedDict, total=False):
    """Outputs for LocalNetworkGateway"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the local network gateway."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the local network gateway was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the local network gateway."""


class LocalNetworkGatewayBicep(Module):
    outputs: LocalNetworkGatewayOutputs


def local_network_gateway(
        bicep: IO[str],
        /,
        *,
        params: LocalNetworkGateway,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'network/local-network-gateway',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> LocalNetworkGatewayBicep:
    symbol = "local_network_gateway_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} '{registry_prefix}/{path}:{tag}' = {{\n")
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
    output = LocalNetworkGatewayBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
