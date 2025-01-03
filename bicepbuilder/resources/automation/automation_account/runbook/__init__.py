from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Runbook(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Automation Account runbook."""
    type: Required[Literal['Graph', 'GraphPowerShell', 'GraphPowerShellWorkflow', 'PowerShell', 'PowerShell72', 'PowerShellWorkflow', 'Python2', 'Python3', 'Script']]
    """The type of the runbook."""
    description: str
    """The description of the runbook."""
    location: str
    """Location for all resources."""
    sasTokenValidityLength: str
    """SAS token validity length. Usage: 'PT8H' - valid for 8 hours; 'P5D' - valid for 5 days; 'P1Y' - valid for 1 year. When not provided, the SAS token will be valid for 8 hours."""
    scriptStorageAccountResourceId: str
    """Resource Id of the runbook storage account."""
    tags: Dict[str, object]
    """Tags of the Automation Account resource."""
    uri: str
    """The uri of the runbook content."""
    version: str
    """The version of the runbook content."""
    baseTime: str
    """Time used as a basis for e.g. the schedule start date."""


class RunbookOutputs(TypedDict, total=False):
    """Outputs for Runbook"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed runbook."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed runbook."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed runbook."""


class RunbookModule(Module):
    outputs: RunbookOutputs

