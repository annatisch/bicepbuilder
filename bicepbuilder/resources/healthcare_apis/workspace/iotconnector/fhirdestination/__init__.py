from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Fhirdestination(TypedDict, total=False):
    """"""
    fhirServiceResourceId: Required[str]
    """The resource identifier of the FHIR Service to connect to."""
    name: Required[str]
    """The name of the FHIR destination."""
    destinationMapping: Dict[str, object]
    """The mapping JSON that determines how normalized data is converted to FHIR Observations."""
    location: str
    """Location for all resources."""
    resourceIdentityResolutionType: Literal['Create', 'Lookup']
    """Determines how resource identity is resolved on the destination."""


class FhirdestinationOutputs(TypedDict, total=False):
    """Outputs for Fhirdestination"""
    iotConnectorName: Output[Literal['string']]
    """The name of the medtech service."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the FHIR destination."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the namespace is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the FHIR destination."""


class FhirdestinationModule(Module):
    outputs: FhirdestinationOutputs

