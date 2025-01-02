from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class ConfigAuthsettingsv2(TypedDict, total=False):
    """"""
    authSettingV2Configuration: Required[Dict[str, object]]
    """The auth settings V2 configuration."""
    kind: Required[Literal['api', 'app', 'app,container,windows', 'app,linux', 'app,linux,container', 'functionapp', 'functionapp,linux', 'functionapp,linux,container', 'functionapp,linux,container,azurecontainerapps', 'functionapp,workflowapp', 'functionapp,workflowapp,linux', 'linux,api']]
    """Type of site to deploy."""
    slotName: Required[str]
    """Slot name to be configured."""


class ConfigAuthsettingsv2Outputs(TypedDict, total=False):
    """Outputs for ConfigAuthsettingsv2"""
    name: Output[Literal['string']]
    """The name of the slot config."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the slot config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the slot config."""


class ConfigAuthsettingsv2Bicep(Module):
    outputs: ConfigAuthsettingsv2Outputs

