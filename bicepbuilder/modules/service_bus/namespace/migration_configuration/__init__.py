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


class MigrationConfiguration(TypedDict, total=False):
    """"""
    postMigrationName: Required[str]
    """Name to access Standard Namespace after migration."""
    targetNamespaceResourceId: Required[str]
    """Existing premium Namespace resource ID which has no entities, will be used for migration."""


class MigrationConfigurationOutputs(TypedDict, total=False):
    """Outputs for MigrationConfiguration"""
    name: Output[Literal['string']]
    """The name of the migration configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the migration configuration was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the migration configuration."""


class MigrationConfigurationBicep(Module):
    outputs: MigrationConfigurationOutputs

