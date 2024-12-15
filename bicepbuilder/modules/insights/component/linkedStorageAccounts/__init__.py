from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Linkedstorageaccount(TypedDict, total=False):
    """"""
    storageAccountResourceId: Required[str]
    """Linked storage account resource ID."""


class LinkedstorageaccountOutputs(TypedDict, total=False):
    """Outputs for Linkedstorageaccount"""
    name: Output[Literal['string']]
    """The name of the Linked Storage Account."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the agent pool was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Linked Storage Account."""


class LinkedstorageaccountBicep(Module):
    outputs: LinkedstorageaccountOutputs


def linkedStorageAccounts(
        bicep: IO[str],
        /,
        *,
        params: Linkedstorageaccount,
        scope: Optional[BicepExpression] = None,
        app_insights_name: Union[str, BicepExpression],
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'insights/component/linkedStorageAccounts',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> LinkedstorageaccountBicep:
    symbol = "linkedStorageAccounts_" + generate_suffix()
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
    file_handle.write(f"    {resolve_key('appInsightsName')}: {resolve_value(app_insights_name)}\n")
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = LinkedstorageaccountBicep(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
