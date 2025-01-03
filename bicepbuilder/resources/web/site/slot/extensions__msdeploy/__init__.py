from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class ExtensionsMsdeploy(TypedDict, total=False):
    """"""
    appName: Required[str]
    """The name of the parent site resource."""
    msDeployConfiguration: Dict[str, object]
    """Sets the MSDeployment Properties."""


class ExtensionsMsdeployOutputs(TypedDict, total=False):
    """Outputs for ExtensionsMsdeploy"""
    name: Output[Literal['string']]
    """The name of the MSDeploy Package."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the site config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Site Extension."""


class ExtensionsMsdeployModule(Module):
    outputs: ExtensionsMsdeployOutputs

