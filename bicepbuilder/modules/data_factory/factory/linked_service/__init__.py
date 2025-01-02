from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class LinkedService(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Linked Service."""
    type: Required[str]
    """The type of Linked Service. See https://learn.microsoft.com/en-us/azure/templates/microsoft.datafactory/factories/linkedservices?pivots=deployment-language-bicep#linkedservice-objects for more information."""
    description: str
    """The description of the Integration Runtime."""
    integrationRuntimeName: str
    """The name of the Integration Runtime to use."""
    parameters: Dict[str, object]
    """Use this to add parameters for a linked service connection string."""
    typeProperties: Dict[str, object]
    """Used to add connection properties for your linked services."""


class LinkedServiceOutputs(TypedDict, total=False):
    """Outputs for LinkedService"""
    name: Output[Literal['string']]
    """The name of the Linked Service."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Linked Service was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Linked Service."""


class LinkedServiceBicep(Module):
    outputs: LinkedServiceOutputs

