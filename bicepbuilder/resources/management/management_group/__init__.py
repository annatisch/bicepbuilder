from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
    Output,
)


class ManagementGroup(TypedDict, total=False):
    """"""
    name: Required[str]
    """The group ID of the Management group."""
    displayName: str
    """The friendly name of the management group. If no value is passed then this field will be set to the group ID."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location deployment metadata."""
    parentId: str
    """The management group parent ID. Defaults to current scope."""


class ManagementGroupOutputs(TypedDict, total=False):
    """Outputs for ManagementGroup"""
    name: Output[Literal['string']]
    """The name of the management group."""
    resourceId: Output[Literal['string']]
    """The resource ID of the management group."""


class ManagementGroupModule(Module):
    outputs: ManagementGroupOutputs


def _management_group(
        bicep: IO[str],
        params: ManagementGroup,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.1.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ManagementGroupModule:
    symbol = "management_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/management/management-group:{tag}' = {{\n")
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
    output = ManagementGroupModule(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
