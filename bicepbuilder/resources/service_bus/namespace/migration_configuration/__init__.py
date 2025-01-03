from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
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


class MigrationConfigurationModule(Module):
    outputs: MigrationConfigurationOutputs

