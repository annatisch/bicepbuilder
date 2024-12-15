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


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Only one type of identity is supported: system-assigned or user-assigned, but not both."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceId: str
    """The resource ID(s) to assign to the resource."""


class EndpointServiceBu(TypedDict, total=False):
    """"""
    primaryConnectionString: str
    """PrimaryConnectionString of the endpoint for key-based authentication. Will be obfuscated during read. Required if the """
    authenticationType: Literal['IdentityBased', 'KeyBased']
    """Specifies the authentication type being used for connecting to the endpoint. If 'KeyBased' is selected, a connection string must be specified (at least the primary connection string). If 'IdentityBased' is selected, the endpointUri and entityPath properties must be specified."""
    deadLetterSecret: str
    """Dead letter storage secret for key-based authentication. Will be obfuscated during read."""
    deadLetterUri: str
    """Dead letter storage URL for identity-based authentication."""
    endpointUri: str
    """The URL of the ServiceBus namespace for identity-based authentication. It must include the protocol 'sb://' (e.g. sb://xyz.servicebus.windows.net)."""
    entityPath: str
    """The ServiceBus Topic name for identity-based authentication."""
    name: str
    """The name of the Digital Twin Endpoint."""
    secondaryConnectionString: str
    """SecondaryConnectionString of the endpoint for key-based authentication. Will be obfuscated during read. Only used if the """


class EndpointServiceBuOutputs(TypedDict, total=False):
    """Outputs for EndpointServiceBu"""
    name: Output[Literal['string']]
    """The name of the Endpoint."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the resource was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Endpoint."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity. Note: As of 2024-03 is not exported by API."""


class EndpointServiceBuBicep(Module):
    outputs: EndpointServiceBuOutputs

