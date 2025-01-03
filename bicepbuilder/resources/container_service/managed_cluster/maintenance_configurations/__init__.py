from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class MaintenanceConfiguration(TypedDict, total=False):
    """"""
    maintenanceWindow: Required[Dict[str, object]]
    """Maintenance window for the maintenance configuration."""
    name: str
    """Name of the maintenance configuration."""


class MaintenanceConfigurationOutputs(TypedDict, total=False):
    """Outputs for MaintenanceConfiguration"""
    name: Output[Literal['string']]
    """The name of the maintenance configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the agent pool was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the maintenance configuration."""


class MaintenanceConfigurationModule(Module):
    outputs: MaintenanceConfigurationOutputs

