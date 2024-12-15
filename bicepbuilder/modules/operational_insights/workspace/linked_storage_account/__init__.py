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


class LinkedStorageAccountBicep(Module):
    outputs: LinkedStorageAccountOutputs

