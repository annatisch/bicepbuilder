from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
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


class OperationsManagementSolutionModule(Module):
    outputs: OperationsManagementSolutionOutputs

