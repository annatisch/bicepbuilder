from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class AppliesToGroup(TypedDict, total=False):
    """Network Groups for the configuration. A connectivity configuration must be associated to at least one network group."""
    groupConnectivity: Required[Literal['DirectlyConnected', 'None']]
    """Group connectivity type."""
    networkGroupResourceId: Required[str]
    """Resource Id of the network group."""
    isGlobal: bool
    """Flag if global is supported."""
    useHubGateway: bool
    """Flag if use hub gateway."""


class Hub(TypedDict, total=False):
    """List of hub items. This will create peerings between the specified hub and the virtual networks in the network group specified. Required if connectivityTopology is of type "HubAndSpoke"."""
    resourceId: Required[str]
    """Resource Id of the hub."""
    resourceType: Required[Literal['Microsoft.Network/virtualNetworks']]
    """Resource type of the hub."""


class ConnectivityConfiguration(TypedDict, total=False):
    """"""
    appliesToGroups: Required[List['AppliesToGroup']]
    """Network Groups for the configuration. A connectivity configuration must be associated to at least one network group."""
    connectivityTopology: Required[Literal['HubAndSpoke', 'Mesh']]
    """Connectivity topology type."""
    name: Required[str]
    """The name of the connectivity configuration."""
    hubs: List['Hub']
    """List of hub items. This will create peerings between the specified hub and the virtual networks in the network group specified. Required if connectivityTopology is of type "HubAndSpoke"."""
    deleteExistingPeering: bool
    """Flag if need to remove current existing peerings. If set to "True", all peerings on virtual networks in selected network groups will be removed and replaced with the peerings defined by this configuration. Optional when connectivityTopology is of type "HubAndSpoke"."""
    description: str
    """A description of the connectivity configuration."""
    isGlobal: bool
    """Flag if global mesh is supported. By default, mesh connectivity is applied to virtual networks within the same region. If set to "True", a global mesh enables connectivity across regions."""


class ConnectivityConfigurationOutputs(TypedDict, total=False):
    """Outputs for ConnectivityConfiguration"""
    name: Output[Literal['string']]
    """The name of the deployed connectivity configuration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the connectivity configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed connectivity configuration."""


class ConnectivityConfigurationModule(Module):
    outputs: ConnectivityConfigurationOutputs

