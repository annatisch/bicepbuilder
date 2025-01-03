from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Extension(TypedDict, total=False):
    """"""
    autoUpgradeMinorVersion: Required[bool]
    """Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true."""
    enableAutomaticUpgrade: Required[bool]
    """Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available."""
    name: Required[str]
    """The name of the virtual machine extension."""
    publisher: Required[str]
    """The name of the extension handler publisher."""
    type: Required[str]
    """Specifies the type of the extension; an example is "CustomScriptExtension"."""
    typeHandlerVersion: Required[str]
    """Specifies the version of the script handler."""
    forceUpdateTag: str
    """How the extension handler should be forced to update even if the extension configuration has not changed."""
    location: str
    """The location the extension is deployed to."""
    protectedSettings: Dict[str, object]
    """Any object that contains the extension specific protected settings."""
    settings: Dict[str, object]
    """Any object that contains the extension specific settings."""
    supressFailures: bool
    """Indicates whether failures stemming from the extension will be suppressed (Operational failures such as not connecting to the VM will not be suppressed regardless of this value). The default is false."""
    tags: Dict[str, object]
    """Tags of the resource."""


class ExtensionOutputs(TypedDict, total=False):
    """Outputs for Extension"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the extension."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the extension was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the extension."""


class ExtensionModule(Module):
    outputs: ExtensionOutputs

