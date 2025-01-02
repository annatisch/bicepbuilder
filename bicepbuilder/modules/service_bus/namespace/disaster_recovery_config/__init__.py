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


class DisasterRecoveryConfig(TypedDict, total=False):
    """"""
    alternateName: str
    """Primary/Secondary eventhub namespace name, which is part of GEO DR pairing."""
    name: str
    """The name of the disaster recovery config."""
    partnerNamespaceResourceID: str
    """Resource ID of the Primary/Secondary event hub namespace name, which is part of GEO DR pairing."""


class DisasterRecoveryConfigOutputs(TypedDict, total=False):
    """Outputs for DisasterRecoveryConfig"""
    name: Output[Literal['string']]
    """The name of the disaster recovery config."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the disaster recovery config was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the disaster recovery config."""


class DisasterRecoveryConfigBicep(Module):
    outputs: DisasterRecoveryConfigOutputs

