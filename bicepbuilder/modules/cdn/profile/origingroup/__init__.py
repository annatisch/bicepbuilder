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

if TYPE_CHECKING:
    from .origin import Origin


class Origingroup(TypedDict, total=False):
    """"""
    loadBalancingSettings: Required[Dict[str, object]]
    """Load balancing settings for a backend pool."""
    name: Required[str]
    """The name of the origin group."""
    origins: Required[List['Origin']]
    """The list of origins within the origin group."""
    profileName: Required[str]
    """The name of the CDN profile."""
    healthProbeSettings: Dict[str, object]
    """Health probe settings to the origin that is used to determine the health of the origin."""
    sessionAffinityState: Literal['Disabled', 'Enabled']
    """Whether to allow session affinity on this host."""
    trafficRestorationTimeToHealedOrNewEndpointsInMinutes: int
    """Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins."""


class OrigingroupOutputs(TypedDict, total=False):
    """Outputs for Origingroup"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the origin group."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the origin group was created in."""
    resourceId: Output[Literal['string']]
    """The resource id of the origin group."""


class OrigingroupBicep(Module):
    outputs: OrigingroupOutputs

