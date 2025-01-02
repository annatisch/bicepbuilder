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

if TYPE_CHECKING:
    from .diagnostics import Diagnostic
    from .policy import Policy


class Api(TypedDict, total=False):
    """"""
    displayName: Required[str]
    """API name. Must be 1 to 300 characters long."""
    name: Required[str]
    """API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number."""
    path: Required[str]
    """Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API."""
    loggerName: str
    """The name of the API management service logger. Required if using api/diagnostics."""
    apiDescription: str
    """Description of the API. May include HTML formatting tags."""
    apiRevision: str
    """Describes the Revision of the API. If no value is provided, default revision 1 is created."""
    apiRevisionDescription: str
    """Description of the API Revision."""
    apiType: Literal['graphql', 'http', 'soap', 'websocket']
    """Type of API to create. * http creates a REST API * soap creates a SOAP pass-through API * websocket creates websocket API * graphql creates GraphQL API."""
    apiVersion: str
    """Indicates the Version identifier of the API if the API is versioned."""
    apiVersionDescription: str
    """Description of the API Version."""
    apiVersionSetId: str
    """Indicates the Version identifier of the API version set."""
    authenticationSettings: Dict[str, object]
    """Collection of authentication settings included into this API."""
    diagnostics: List['Diagnostic']
    """Array of diagnostics to apply to the Service API."""
    format: Literal['openapi', 'openapi-link', 'openapi+json', 'openapi+json-link', 'swagger-json', 'swagger-link-json', 'wadl-link-json', 'wadl-xml', 'wsdl', 'wsdl-link']
    """Format of the Content in which the API is getting imported."""
    isCurrent: bool
    """Indicates if API revision is current API revision."""
    policies: List['Policy']
    """Array of Policies to apply to the Service API."""
    protocols: List[object]
    """Describes on which protocols the operations in this API can be invoked. - HTTP or HTTPS."""
    serviceUrl: str
    """Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long."""
    sourceApiId: str
    """API identifier of the source API."""
    subscriptionKeyParameterNames: Dict[str, object]
    """Protocols over which API is made available."""
    subscriptionRequired: bool
    """Specifies whether an API or Product subscription is required for accessing the API."""
    type: Literal['graphql', 'http', 'soap', 'websocket']
    """Type of API."""
    value: str
    """Content value when Importing an API."""
    wsdlSelector: Dict[str, object]
    """Criteria to limit import of WSDL to a subset of the document."""


class ApiOutputs(TypedDict, total=False):
    """Outputs for Api"""
    name: Output[Literal['string']]
    """The name of the API management service API."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service API was deployed to."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service API."""


class ApiBicep(Module):
    outputs: ApiOutputs

