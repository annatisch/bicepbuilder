from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class LinkedServer(TypedDict, total=False):
    """"""
    linkedRedisCacheResourceId: Required[str]
    """The resource ID of the linked server."""
    redisCacheName: Required[str]
    """Primary Redis cache name."""
    linkedRedisCacheLocation: str
    """The location of the linked server. If not provided, the location of the primary Redis cache is used."""
    name: str
    """The name of the secondary Redis cache. If not provided, the primary Redis cache name is used."""
    serverRole: str
    """The role of the linked server. Possible values include: "Primary", "Secondary". Default value is "Secondary"."""


class LinkedServerOutputs(TypedDict, total=False):
    """Outputs for LinkedServer"""
    geoReplicatedPrimaryHostName: Output[Literal['string']]
    """The hostname of the linkedServer."""
    name: Output[Literal['string']]
    """The name of the linkedServer resource."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed linkedServer."""
    resourceId: Output[Literal['string']]
    """The resource ID of the linkedServer."""


class LinkedServerModule(Module):
    outputs: LinkedServerOutputs

