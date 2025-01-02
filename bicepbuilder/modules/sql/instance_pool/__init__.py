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


class SqlInstancePool(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the instance pool."""
    subnetResourceId: Required[str]
    """The subnet resource ID for the instance pool."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    licenseType: Literal['BasePrice', 'LicenseIncluded']
    """The license type to apply for this database."""
    location: str
    """Location for all resources."""
    skuFamily: str
    """If the service has different generations of hardware, for the same SKU, then that can be captured here."""
    skuName: str
    """The SKU name for the instance pool."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tier: Literal['GeneralPurpose']
    """The vCore service tier for the instance pool."""
    vCores: Literal[8, 16, 24, 32, 40, 64, 80, 96, 128, 160, 192, 224, 256]
    """The number of vCores for the instance pool."""


class SqlInstancePoolOutputs(TypedDict, total=False):
    """Outputs for SqlInstancePool"""
    instancePoolLocation: Output[Literal['string']]
    """The location of the SQL instance pool."""
    name: Output[Literal['string']]
    """The name of the SQL instance pool."""
    resourceGroupName: Output[Literal['string']]
    """The resource group name of the SQL instance pool."""
    resourceId: Output[Literal['string']]
    """The ID of the SQL instance pool."""


class SqlInstancePoolBicep(Module):
    outputs: SqlInstancePoolOutputs


def sql_instance_pool(
        bicep: IO[str],
        params: SqlInstancePool,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> SqlInstancePoolBicep:
    symbol = "sql_instance_pool_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/sql/instance-pool:{tag}' = {{\n")
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
    output = SqlInstancePoolBicep(symbol)
    output.outputs = {
            'instancePoolLocation': Output(symbol, 'instancePoolLocation', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
