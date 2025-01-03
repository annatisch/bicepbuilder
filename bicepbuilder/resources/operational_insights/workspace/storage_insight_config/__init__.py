from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class StorageInsightConfig(TypedDict, total=False):
    """"""
    storageAccountResourceId: Required[str]
    """The Azure Resource Manager ID of the storage account resource."""
    containers: List[object]
    """The names of the blob containers that the workspace should read."""
    name: str
    """The name of the storage insights config."""
    tables: List[object]
    """The names of the Azure tables that the workspace should read."""
    tags: Dict[str, object]
    """Tags to configure in the resource."""


class StorageInsightConfigOutputs(TypedDict, total=False):
    """Outputs for StorageInsightConfig"""
    name: Output[Literal['string']]
    """The name of the storage insights configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the storage insight configuration is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed storage insights configuration."""


class StorageInsightConfigModule(Module):
    outputs: StorageInsightConfigOutputs

