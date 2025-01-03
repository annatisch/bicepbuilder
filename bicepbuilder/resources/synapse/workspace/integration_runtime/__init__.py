from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class IntegrationRuntime(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Integration Runtime."""
    type: Required[Literal['Managed', 'SelfHosted']]
    """The type of Integration Runtime."""
    typeProperties: Dict[str, object]
    """Integration Runtime type properties. Required if type is "Managed"."""


class IntegrationRuntimeOutputs(TypedDict, total=False):
    """Outputs for IntegrationRuntime"""
    name: Output[Literal['string']]
    """The name of the Integration Runtime."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the Integration Runtime was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Integration Runtime."""


class IntegrationRuntimeModule(Module):
    outputs: IntegrationRuntimeOutputs

