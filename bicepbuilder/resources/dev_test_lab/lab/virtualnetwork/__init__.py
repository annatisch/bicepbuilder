from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class AllowedSubnet(TypedDict, total=False):
    """The allowed subnets of the virtual network."""
    labSubnetName: Required[str]
    """The name of the subnet as seen in the lab."""
    resourceId: Required[str]
    """The resource ID of the allowed subnet."""
    allowPublicIp: Literal['Allow', 'Default', 'Deny']
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""


class AllowedPort(TypedDict, total=False):
    """Backend ports that virtual machines on this subnet are allowed to expose."""
    backendPort: Required[int]
    """Backend port of the target virtual machine."""
    transportProtocol: Required[Literal['Tcp', 'Udp']]
    """Protocol type of the port."""


class SharedPublicIpAddressConfiguration(TypedDict, total=False):
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""
    allowedPorts: Required[List['AllowedPort']]
    """Backend ports that virtual machines on this subnet are allowed to expose."""


class SubnetOverride(TypedDict, total=False):
    """The subnet overrides of the virtual network."""
    labSubnetName: Required[str]
    """The name given to the subnet within the lab."""
    resourceId: Required[str]
    """The resource ID of the subnet."""
    sharedPublicIpAddressConfiguration: 'SharedPublicIpAddressConfiguration'
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""
    useInVmCreationPermission: Literal['Allow', 'Default', 'Deny']
    """Indicates whether this subnet can be used during virtual machine creation (i.e. Allow, Deny)."""
    usePublicIpAddressPermission: Literal['Allow', 'Default', 'Deny']
    """Indicates whether public IP addresses can be assigned to virtual machines on this subnet (i.e. Allow, Deny)."""
    virtualNetworkPoolName: str
    """The virtual network pool associated with this subnet."""


class Virtualnetwork(TypedDict, total=False):
    """"""
    externalProviderResourceId: Required[str]
    """The resource ID of the virtual network."""
    name: Required[str]
    """The name of the virtual network."""
    allowedSubnets: List['AllowedSubnet']
    """The allowed subnets of the virtual network."""
    description: str
    """The description of the virtual network."""
    subnetOverrides: List['SubnetOverride']
    """The subnet overrides of the virtual network."""
    tags: Dict[str, object]
    """Tags of the resource."""


class VirtualnetworkOutputs(TypedDict, total=False):
    """Outputs for Virtualnetwork"""
    name: Output[Literal['string']]
    """The name of the lab virtual network."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the lab virtual network was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the lab virtual network."""


class VirtualnetworkModule(Module):
    outputs: VirtualnetworkOutputs

