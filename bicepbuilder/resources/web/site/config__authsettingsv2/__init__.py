from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConfigAuthsettingsv2(TypedDict, total=False):
    """"""
    authSettingV2Configuration: Required[Dict[str, object]]
    """The auth settings V2 configuration."""
    kind: Required[Literal['api', 'app', 'app,container,windows', 'app,linux', 'app,linux,container', 'functionapp', 'functionapp,linux', 'functionapp,linux,container', 'functionapp,linux,container,azurecontainerapps', 'functionapp,workflowapp', 'functionapp,workflowapp,linux', 'linux,api']]
    """Type of site to deploy."""


class ConfigAuthsettingsv2Outputs(TypedDict, total=False):
    """Outputs for ConfigAuthsettingsv2"""
    name: Output[Literal['string']]
    """The name of the site config."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the site config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the site config."""


class ConfigAuthsettingsv2Module(Module):
    outputs: ConfigAuthsettingsv2Outputs

