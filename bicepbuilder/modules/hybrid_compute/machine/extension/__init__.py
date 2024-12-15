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


class Extension(TypedDict, total=False):
    """"""
    arcMachineName: Required[str]
    """The name of the parent Arc Machine that extension is provisioned for."""
    autoUpgradeMinorVersion: Required[bool]
    """Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true."""
    enableAutomaticUpgrade: Required[bool]
    """Indicates whether the extension should be automatically upgraded by the platform if there is a newer version of the extension available."""
    name: Required[str]
    """The name of the Arc Machine extension."""
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


class ExtensionBicep(Module):
    outputs: ExtensionOutputs

