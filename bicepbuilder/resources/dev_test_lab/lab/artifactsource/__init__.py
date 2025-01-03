from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Artifactsource(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the artifact source."""
    uri: Required[str]
    """The artifact source's URI."""
    armTemplateFolderPath: str
    """The folder containing Azure Resource Manager templates. Required if "folderPath" is empty."""
    folderPath: str
    """The folder containing artifacts. At least one folder path is required. Required if "armTemplateFolderPath" is empty."""
    branchRef: str
    """The artifact source's branch reference (e.g. main or master)."""
    displayName: str
    """The artifact source's display name. Default is the name of the artifact source."""
    securityToken: str
    """The security token to authenticate to the artifact source."""
    sourceType: Literal['GitHub', 'StorageAccount', 'VsoGit']
    """The artifact source's type."""
    status: Literal['Disabled', 'Enabled']
    """Indicates if the artifact source is enabled (values: Enabled, Disabled). Default is "Enabled"."""
    tags: Dict[str, object]
    """Tags of the resource."""


class ArtifactsourceOutputs(TypedDict, total=False):
    """Outputs for Artifactsource"""
    name: Output[Literal['string']]
    """The name of the artifact source."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the artifact source was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the artifact source."""


class ArtifactsourceModule(Module):
    outputs: ArtifactsourceOutputs

