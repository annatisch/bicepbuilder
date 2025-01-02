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


class Application(TypedDict, total=False):
    """"""
    filePath: Required[str]
    """Specifies a path for the executable file for the Application."""
    friendlyName: Required[str]
    """Friendly name of the Application."""
    name: Required[str]
    """Name of the Application to be created in the Application Group."""
    commandLineArguments: str
    """Command-Line Arguments for the Application."""
    commandLineSetting: Literal['Allow', 'DoNotAllow', 'Require']
    """Specifies whether this published Application can be launched with command-line arguments provided by the client, command-line arguments specified at publish time, or no command-line arguments at all."""
    description: str
    """Description of the Application."""
    iconIndex: int
    """Index of the icon."""
    iconPath: str
    """Path to icon."""
    showInPortal: bool
    """Specifies whether to show the RemoteApp program in the RD Web Access server."""


class ApplicationOutputs(TypedDict, total=False):
    """Outputs for Application"""
    name: Output[Literal['string']]
    """The name of the Application."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Application was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Application."""


class ApplicationBicep(Module):
    outputs: ApplicationOutputs

