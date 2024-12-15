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


class StorageInsightConfigBicep(Module):
    outputs: StorageInsightConfigOutputs

