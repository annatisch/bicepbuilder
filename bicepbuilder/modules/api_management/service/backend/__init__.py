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


class Backend(TypedDict, total=False):
    """"""
    name: Required[str]
    """Backend Name."""
    url: Required[str]
    """Runtime URL of the Backend."""
    credentials: Dict[str, object]
    """Backend Credentials Contract Properties."""
    description: str
    """Backend Description."""
    protocol: str
    """Backend communication protocol. - http or soap."""
    proxy: Dict[str, object]
    """Backend Proxy Contract Properties."""
    resourceId: str
    """Management Uri of the Resource in External System. This URL can be the Arm Resource ID of Logic Apps, Function Apps or API Apps."""
    serviceFabricCluster: Dict[str, object]
    """Backend Service Fabric Cluster Properties."""
    title: str
    """Backend Title."""
    tls: Dict[str, object]
    """Backend TLS Properties."""


class BackendOutputs(TypedDict, total=False):
    """Outputs for Backend"""
    name: Output[Literal['string']]
    """The name of the API management service backend."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service backend was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service backend."""


class BackendBicep(Module):
    outputs: BackendOutputs

