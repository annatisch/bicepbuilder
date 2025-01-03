from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class PrivateDnsZoneConfig(TypedDict, total=False):
    """Array of private DNS zone configurations of the private DNS zone group. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """"""
    privateDnsZoneConfigs: Required[List['PrivateDnsZoneConfig']]
    """Array of private DNS zone configurations of the private DNS zone group. A DNS zone group can support up to 5 DNS zones."""
    name: str
    """The name of the private DNS zone group."""


class PrivateDnsZoneGroupOutputs(TypedDict, total=False):
    """Outputs for PrivateDnsZoneGroup"""
    name: Output[Literal['string']]
    """The name of the private endpoint DNS zone group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the private endpoint DNS zone group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the private endpoint DNS zone group."""


class PrivateDnsZoneGroupModule(Module):
    outputs: PrivateDnsZoneGroupOutputs

