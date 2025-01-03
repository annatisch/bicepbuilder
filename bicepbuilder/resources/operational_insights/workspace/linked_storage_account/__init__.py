from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LinkedStorageAccount(TypedDict, total=False):
    """"""
    name: Required[Literal['Alerts', 'AzureWatson', 'CustomLogs', 'Query']]
    """Name of the link."""
    storageAccountIds: Required[List[object]]
    """Linked storage accounts resources Ids."""


class LinkedStorageAccountOutputs(TypedDict, total=False):
    """Outputs for LinkedStorageAccount"""
    name: Output[Literal['string']]
    """The name of the deployed linked storage account."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the linked storage account is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed linked storage account."""


class LinkedStorageAccountModule(Module):
    outputs: LinkedStorageAccountOutputs

