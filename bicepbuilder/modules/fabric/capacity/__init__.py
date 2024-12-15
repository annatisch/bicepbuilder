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


class Capacity(TypedDict, total=False):
    """"""
    adminMembers: Required[List[object]]
    """List of admin members. Format: ["something@domain.com"]."""
    name: Required[str]
    """Name of the resource to create."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    skuName: Literal['F1024', 'F128', 'F16', 'F2', 'F2048', 'F256', 'F32', 'F4', 'F512', 'F64', 'F8']
    """SKU tier of the Fabric resource."""
    skuTier: Literal['Fabric']
    """SKU name of the Fabric resource."""
    tags: Dict[str, object]
    """Tags of the resource."""


class CapacityOutputs(TypedDict, total=False):
    """Outputs for Capacity"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed Fabric resource."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the module was deployed to."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed Fabric resource."""


class CapacityBicep(Module):
    outputs: CapacityOutputs


def capacity(
        bicep: IO[str],
        /,
        *,
        params: Capacity,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'fabric/capacity',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> CapacityBicep:
    symbol = "capacity_" + generate_suffix()
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
    output = CapacityBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
