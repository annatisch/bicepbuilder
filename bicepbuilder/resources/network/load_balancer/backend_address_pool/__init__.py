from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class BackendAddressPool(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the backend address pool."""
    drainPeriodInSeconds: int
    """Amount of seconds Load Balancer waits for before sending RESET to client and backend address. if value is 0 then this property will be set to null. Subscription must register the feature Microsoft.Network/SLBAllowConnectionDraining before using this property."""
    loadBalancerBackendAddresses: List[object]
    """An array of backend addresses."""
    syncMode: Literal['', 'Automatic', 'Manual']
    """Backend address synchronous mode for the backend pool."""
    tunnelInterfaces: List[object]
    """An array of gateway load balancer tunnel interfaces."""


class BackendAddressPoolOutputs(TypedDict, total=False):
    """Outputs for BackendAddressPool"""
    name: Output[Literal['string']]
    """The name of the backend address pool."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the backend address pool was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the backend address pool."""


class BackendAddressPoolModule(Module):
    outputs: BackendAddressPoolOutputs

