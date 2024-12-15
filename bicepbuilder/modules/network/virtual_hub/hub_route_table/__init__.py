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


class HubRouteTable(TypedDict, total=False):
    """"""
    name: Required[str]
    """The route table name."""
    labels: List[object]
    """List of labels associated with this route table."""
    routes: List[object]
    """List of all routes."""


class HubRouteTableOutputs(TypedDict, total=False):
    """Outputs for HubRouteTable"""
    name: Output[Literal['string']]
    """The name of the deployed virtual hub route table."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the virtual hub route table was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed virtual hub route table."""


class HubRouteTableBicep(Module):
    outputs: HubRouteTableOutputs

