from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class DisasterRecoveryConfig(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the disaster recovery config."""
    partnerNamespaceId: str
    """Resource ID of the Primary/Secondary event hub namespace name, which is part of GEO DR pairing."""


class DisasterRecoveryConfigOutputs(TypedDict, total=False):
    """Outputs for DisasterRecoveryConfig"""
    name: Output[Literal['string']]
    """The name of the disaster recovery config."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the disaster recovery config was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the disaster recovery config."""


class DisasterRecoveryConfigModule(Module):
    outputs: DisasterRecoveryConfigOutputs

