from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class ImmutabilityPolicy(TypedDict, total=False):
    """"""
    allowProtectedAppendWrites: bool
    """This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to an append blob while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API."""
    allowProtectedAppendWritesAll: bool
    """This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to both "Append and Block Blobs" while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API. The "allowProtectedAppendWrites" and "allowProtectedAppendWritesAll" properties are mutually exclusive."""
    immutabilityPeriodSinceCreationInDays: int
    """The immutability period for the blobs in the container since the policy creation, in days."""


class ImmutabilityPolicyOutputs(TypedDict, total=False):
    """Outputs for ImmutabilityPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed immutability policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed immutability policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed immutability policy."""


class ImmutabilityPolicyBicep(Module):
    outputs: ImmutabilityPolicyOutputs

