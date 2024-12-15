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


class VpnConnection(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the VPN connection."""
    connectionBandwidth: int
    """Expected bandwidth in MBPS."""
    enableBgp: bool
    """Enable BGP flag."""
    enableInternetSecurity: bool
    """Enable internet security."""
    enableRateLimiting: bool
    """Enable rate limiting."""
    ipsecPolicies: List[object]
    """The IPSec policies to be considered by this connection."""
    remoteVpnSiteResourceId: str
    """Reference to a VPN site to link to."""
    routingConfiguration: Dict[str, object]
    """Routing configuration indicating the associated and propagated route tables for this connection."""
    routingWeight: int
    """Routing weight for VPN connection."""
    sharedKey: str
    """SharedKey for the VPN connection."""
    trafficSelectorPolicies: List[object]
    """The traffic selector policies to be considered by this connection."""
    useLocalAzureIpAddress: bool
    """Use local Azure IP to initiate connection."""
    usePolicyBasedTrafficSelectors: bool
    """Enable policy-based traffic selectors."""
    vpnConnectionProtocolType: Literal['IKEv1', 'IKEv2']
    """Gateway connection protocol."""
    vpnLinkConnections: List[object]
    """List of all VPN site link connections to the gateway."""


class VpnConnectionOutputs(TypedDict, total=False):
    """Outputs for VpnConnection"""
    name: Output[Literal['string']]
    """The name of the VPN connection."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the VPN connection was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the VPN connection."""


class VpnConnectionBicep(Module):
    outputs: VpnConnectionOutputs

