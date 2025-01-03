from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
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


class LinkedstorageaccountModule(Module):
    outputs: LinkedstorageaccountOutputs


def _linkedStorageAccounts(
        bicep: IO[str],
        params: 'Linkedstorageaccount',
        /,
        *,
        app_insights_name: Union[str, BicepExpression],
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> 'LinkedstorageaccountModule':
    symbol = "linkedStorageAccounts_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/component/linkedStorageAccounts:{tag}' = {{\n")
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

    from .insights/component import LinkedstorageaccountModule
    output = LinkedstorageaccountModule(symbol)
    output.outputs = {
        'name': Output(symbol, 'name', 'string'),
        'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
        'resourceId': Output(symbol, 'resourceId', 'string'),
    }

    return output
