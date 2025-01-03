from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class NetworkConnection(TypedDict, total=False):
    """"""
    name: Required[str]
    """Remote connection name."""
    virtualNetworkGateway1: Required[Dict[str, object]]
    """The primary Virtual Network Gateway."""
    authorizationKey: str
    """The Authorization Key to connect to an Express Route Circuit. Used for connection type [ExpressRoute]."""
    connectionMode: Literal['Default', 'InitiatorOnly', 'ResponderOnly']
    """The connection connectionMode for this connection. Available for IPSec connections."""
    connectionProtocol: Literal['IKEv1', 'IKEv2']
    """Connection connectionProtocol used for this connection. Available for IPSec connections."""
    connectionType: Literal['ExpressRoute', 'IPsec', 'Vnet2Vnet', 'VPNClient']
    """Gateway connection connectionType."""
    customIPSecPolicy: Dict[str, object]
    """The IPSec Policies to be considered by this connection."""
    dpdTimeoutSeconds: int
    """The dead peer detection timeout of this connection in seconds. Setting the timeout to shorter periods will cause IKE to rekey more aggressively, causing the connection to appear to be disconnected in some instances. The general recommendation is to set the timeout between 30 to 45 seconds."""
    enableBgp: bool
    """Value to specify if BGP is enabled or not."""
    enablePrivateLinkFastPath: bool
    """Bypass the ExpressRoute gateway when accessing private-links. ExpressRoute FastPath (expressRouteGatewayBypass) must be enabled. Only available when connection connectionType is Express Route."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    expressRouteGatewayBypass: bool
    """Bypass ExpressRoute Gateway for data forwarding. Only available when connection connectionType is Express Route."""
    localNetworkGateway2: Dict[str, object]
    """The local network gateway. Used for connection type [IPsec]."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    peer: Dict[str, object]
    """The remote peer. Used for connection connectionType [ExpressRoute]."""
    routingWeight: int
    """The weight added to routes learned from this BGP speaker."""
    tags: Dict[str, object]
    """Tags of the resource."""
    trafficSelectorPolicies: List[object]
    """The traffic selector policies to be considered by this connection."""
    useLocalAzureIpAddress: bool
    """Use private local Azure IP for the connection. Only available for IPSec Virtual Network Gateways that use the Azure Private IP Property."""
    usePolicyBasedTrafficSelectors: bool
    """Enable policy-based traffic selectors."""
    virtualNetworkGateway2: Dict[str, object]
    """The remote Virtual Network Gateway. Used for connection connectionType [Vnet2Vnet]."""
    vpnSharedKey: str
    """Specifies a VPN shared key. The same value has to be specified on both Virtual Network Gateways."""


class NetworkConnectionOutputs(TypedDict, total=False):
    """Outputs for NetworkConnection"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the remote connection."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the remote connection was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the remote connection."""


class NetworkConnectionModule(Module):
    outputs: NetworkConnectionOutputs

