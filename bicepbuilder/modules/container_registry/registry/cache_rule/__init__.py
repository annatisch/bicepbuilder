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


class CacheRule(TypedDict, total=False):
    """"""
    credentialSetResourceId: Required[str]
    """The resource ID of the credential store which is associated with the cache rule."""
    sourceRepository: Required[str]
    """Source repository pulled from upstream."""
    name: str
    """The name of the cache rule. Will be derived from the source repository name if not defined."""
    targetRepository: str
    """Target repository specified in docker pull command. E.g.: docker pull myregistry.azurecr.io/{targetRepository}:{tag}."""


class CacheRuleOutputs(TypedDict, total=False):
    """Outputs for CacheRule"""
    name: Output[Literal['string']]
    """The Name of the Cache Rule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Cache Rule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Cache Rule."""


class CacheRuleBicep(Module):
    outputs: CacheRuleOutputs

