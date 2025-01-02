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


class Plan(TypedDict, total=False):
    """Plan for solution object supported by the OperationsManagement resource provider."""
    product: Required[str]
    """The product name of the deployed solution."""
    name: str
    """Name of the solution to be created."""
    publisher: str
    """The publisher name of the deployed solution. For Microsoft published gallery solution, it is """


class OperationsManagementSolution(TypedDict, total=False):
    """"""
    logAnalyticsWorkspaceName: Required[str]
    """Name of the Log Analytics workspace where the solution will be deployed/enabled."""
    name: Required[str]
    """Name of the solution."""
    plan: Required['Plan']
    """Plan for solution object supported by the OperationsManagement resource provider."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""


class OperationsManagementSolutionOutputs(TypedDict, total=False):
    """Outputs for OperationsManagementSolution"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed solution."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the solution is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed solution."""


class OperationsManagementSolutionBicep(Module):
    outputs: OperationsManagementSolutionOutputs


def operations_management_solution(
        bicep: IO[str],
        params: OperationsManagementSolution,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> OperationsManagementSolutionBicep:
    symbol = "operations_management_solution_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/operations-management/solution:{tag}' = {{\n")
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
    output = OperationsManagementSolutionBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
