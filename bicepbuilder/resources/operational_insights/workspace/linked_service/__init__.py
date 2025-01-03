from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LinkedService(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the link."""
    resourceId: str
    """The resource ID of the resource that will be linked to the workspace. This should be used for linking resources which require read access."""
    tags: Dict[str, object]
    """Tags to configure in the resource."""
    writeAccessResourceId: str
    """The resource ID of the resource that will be linked to the workspace. This should be used for linking resources which require write access."""


class LinkedServiceOutputs(TypedDict, total=False):
    """Outputs for LinkedService"""
    name: Output[Literal['string']]
    """The name of the deployed linked service."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the linked service is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed linked service."""


class LinkedServiceModule(Module):
    outputs: LinkedServiceOutputs

