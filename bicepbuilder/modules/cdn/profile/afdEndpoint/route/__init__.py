from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Route(TypedDict, total=False):
    """"""
    afdEndpointName: Required[str]
    """The name of the AFD endpoint."""
    name: Required[str]
    """The name of the route."""
    originGroupName: Required[str]
    """The name of the origin group. The origin group must be defined in the profile originGroups."""
    profileName: Required[str]
    """The name of the parent CDN profile."""
    cacheConfiguration: Dict[str, object]
    """The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object."""
    customDomainNames: List[object]
    """The names of the custom domains. The custom domains must be defined in the profile customDomains array."""
    enabledState: Literal['Disabled', 'Enabled']
    """Whether this route is enabled."""
    forwardingProtocol: Literal['HttpOnly', 'HttpsOnly', 'MatchRequest']
    """The protocol this rule will use when forwarding traffic to backends."""
    httpsRedirect: Literal['Disabled', 'Enabled']
    """Whether to automatically redirect HTTP traffic to HTTPS traffic."""
    linkToDefaultDomain: Literal['Disabled', 'Enabled']
    """Whether this route will be linked to the default endpoint domain."""
    originPath: str
    """A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath."""
    patternsToMatch: List[object]
    """The route patterns of the rule."""
    ruleSets: List[object]
    """The rule sets of the rule. The rule sets must be defined in the profile ruleSets."""
    supportedProtocols: Literal['Http', 'Https']
    """The supported protocols of the rule."""


class RouteOutputs(TypedDict, total=False):
    """Outputs for Route"""
    name: Output[Literal['string']]
    """The name of the route."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the route was created in."""
    resourceId: Output[Literal['string']]
    """The ID of the route."""


class RouteBicep(Module):
    outputs: RouteOutputs

