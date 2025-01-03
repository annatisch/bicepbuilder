from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .secret import Secret


class LoadBalancingSetting(TypedDict, total=False):
    """Load balancing settings for a backend pool."""
    additionalLatencyInMilliseconds: Required[int]
    """Additional latency in milliseconds for probes to the backend. Must be between 0 and 1000."""
    sampleSize: Required[int]
    """Number of samples to consider for load balancing decisions."""
    successfulSamplesRequired: Required[int]
    """Number of samples within the sample window that must be successful to mark the backend as healthy."""


class Origin(TypedDict, total=False):
    """The list of origins within the origin group."""
    hostName: Required[str]
    """The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint."""
    name: Required[str]
    """The name of the origion."""
    enabledState: Literal['Disabled', 'Enabled']
    """Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool."""
    enforceCertificateNameCheck: bool
    """Whether to enable certificate name check at origin level."""
    httpPort: int
    """The value of the HTTP port. Must be between 1 and 65535."""
    httpsPort: int
    """The value of the HTTPS port. Must be between 1 and 65535."""
    originHostHeader: str
    """The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure Front Door origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint."""
    priority: int
    """Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5."""
    sharedPrivateLinkResource: Dict[str, object]
    """The properties of the private link resource for private origin."""
    weight: int
    """Weight of the origin in given origin group for load balancing. Must be between 1 and 1000."""


class HealthProbeSetting(TypedDict, total=False):
    """Health probe settings to the origin that is used to determine the health of the origin."""
    probeIntervalInSeconds: int
    """The number of seconds between health probes.Default is 240sec."""
    probePath: str
    """The path relative to the origin that is used to determine the health of the origin."""
    probeProtocol: Literal['Http', 'Https', 'NotSet']
    """Protocol to use for health probe."""
    probeRequestType: Literal['GET', 'HEAD', 'NotSet']
    """The request type to probe."""


class OriginGroup(TypedDict, total=False):
    """Array of origin group objects. Required if the afdEndpoints is specified."""
    loadBalancingSettings: Required['LoadBalancingSetting']
    """Load balancing settings for a backend pool."""
    name: Required[str]
    """The name of the origin group."""
    origins: Required[List['Origin']]
    """The list of origins within the origin group."""
    healthProbeSettings: 'HealthProbeSetting'
    """Health probe settings to the origin that is used to determine the health of the origin."""
    sessionAffinityState: Literal['Disabled', 'Enabled']
    """Whether to allow session affinity on this host."""
    trafficRestorationTimeToHealedOrNewEndpointsInMinutes: int
    """Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins."""


class CompressionSetting(TypedDict, total=False):
    """Compression settings."""
    contentTypesToCompress: Required[List[object]]
    """List of content types on which compression applies. The value should be a valid MIME type."""
    iscontentTypeToCompressAll: bool
    """Indicates whether content compression is enabled on AzureFrontDoor. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB."""


class CacheConfiguration(TypedDict, total=False):
    """The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object."""
    compressionSettings: Required['CompressionSetting']
    """Compression settings."""
    queryParameters: Required[str]
    """Query parameters to include or exclude (comma separated)."""
    queryStringCachingBehavior: Required[Literal['IgnoreQueryString', 'IgnoreSpecifiedQueryStrings', 'IncludeSpecifiedQueryStrings', 'UseQueryString']]
    """Defines how Frontdoor caches requests that include query strings."""


class Route(TypedDict, total=False):
    """The list of routes for this AFD Endpoint."""
    name: Required[str]
    """The name of the route."""
    originGroupName: Required[str]
    """The name of the origin group."""
    cacheConfiguration: 'CacheConfiguration'
    """The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object."""
    customDomainNames: List[object]
    """The names of the custom domains."""
    enabledState: Literal['Disabled', 'Enabled']
    """Whether to enable use of this rule."""
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
    """The rule sets of the rule."""
    supportedProtocols: List[object]
    """The supported protocols of the rule."""


class AfdEndpoint(TypedDict, total=False):
    """Array of AFD endpoint objects."""
    name: Required[str]
    """The name of the AFD Endpoint."""
    autoGeneratedDomainNameLabelScope: Literal['NoReuse', 'ResourceGroupReuse', 'SubscriptionReuse', 'TenantReuse']
    """The scope of the auto-generated domain name label."""
    enabledState: Literal['Disabled', 'Enabled']
    """The state of the AFD Endpoint."""
    routes: List['Route']
    """The list of routes for this AFD Endpoint."""
    tags: Dict[str, object]
    """The tags for the AFD Endpoint."""


class CustomDomain(TypedDict, total=False):
    """Array of custom domain objects."""
    certificateType: Required[Literal['AzureFirstPartyManagedCertificate', 'CustomerCertificate', 'ManagedCertificate']]
    """The type of the certificate."""
    hostName: Required[str]
    """The host name of the custom domain."""
    name: Required[str]
    """The name of the custom domain."""
    azureDnsZoneResourceId: str
    """The resource ID of the Azure DNS zone."""
    extendedProperties: Dict[str, object]
    """Extended properties."""
    minimumTlsVersion: Literal['TLS10', 'TLS12']
    """The minimum TLS version."""
    preValidatedCustomDomainResourceId: str
    """The resource ID of the pre-validated custom domain."""
    secretName: str
    """The name of the secret."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['CDN Endpoint Contributor', 'CDN Endpoint Reader', 'CDN Profile Contributor', 'CDN Profile Reader', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """The role to assign. You can provide either the display name of the role definition, the role definition GUID, or its fully qualified ID in the following format: '/providers/Microsoft.Authorization/roleDefinitions/c2f4ef07-c644-48eb-af81-4b1b4947fb11'."""
    condition: str
    """The conditions on the role assignment. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase "foo_storage_container"."""
    conditionVersion: Literal['2.0']
    """Version of the condition."""
    delegatedManagedIdentityResourceId: str
    """The Resource Id of the delegated managed identity resource."""
    description: str
    """The description of the role assignment."""
    name: str
    """The name (as GUID) of the role assignment. If not provided, a GUID will be generated."""
    principalType: Literal['Device', 'ForeignGroup', 'Group', 'ServicePrincipal', 'User']
    """The principal type of the assigned principal ID."""


class Rule(TypedDict, total=False):
    """Array of rules."""
    name: Required[str]
    """The name of the rule."""
    order: Required[int]
    """The order in which the rules are applied for the endpoint."""
    actions: List[object]
    """A list of actions that are executed when all the conditions of a rule are satisfied.."""
    conditions: List[object]
    """A list of conditions that must be matched for the actions to be executed."""
    matchProcessingBehavior: Literal['Continue', 'Stop']
    """If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue."""


class RuleSet(TypedDict, total=False):
    """Array of rule set objects."""
    name: Required[str]
    """Name of the rule set."""
    rules: List['Rule']
    """Array of rules."""


class Domain(TypedDict, total=False):
    """List of domain resource id to associate with this resource."""
    id: Required[str]
    """ResourceID to domain that will be associated."""


class Association(TypedDict, total=False):
    """Domain names and URL patterns to match with this association."""
    domains: Required[List['Domain']]
    """List of domain resource id to associate with this resource."""
    patternsToMatch: Required[List[object]]
    """List of patterns to match with this association."""


class SecurityPolicy(TypedDict, total=False):
    """Array of Security Policy objects (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/securitypolicies for details)."""
    associations: Required[List['Association']]
    """Domain names and URL patterns to match with this association."""
    name: Required[str]
    """Name of the security policy."""
    wafPolicyResourceId: Required[str]
    """Resource ID of WAF policy."""


class CdnProfile(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the CDN profile."""
    sku: Required[Literal['Custom_Verizon', 'Premium_AzureFrontDoor', 'Premium_Verizon', 'Standard_955BandWidth_ChinaCdn', 'Standard_AvgBandWidth_ChinaCdn', 'Standard_AzureFrontDoor', 'Standard_ChinaCdn', 'Standard_Microsoft', 'Standard_Verizon', 'StandardPlus_955BandWidth_ChinaCdn', 'StandardPlus_AvgBandWidth_ChinaCdn', 'StandardPlus_ChinaCdn']]
    """The pricing tier (defines a CDN provider, feature list and rate) of the CDN profile."""
    originGroups: List['OriginGroup']
    """Array of origin group objects. Required if the afdEndpoints is specified."""
    afdEndpoints: List['AfdEndpoint']
    """Array of AFD endpoint objects."""
    customDomains: List['CustomDomain']
    """Array of custom domain objects."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    endpointName: str
    """Name of the endpoint under the profile which is unique globally."""
    endpointProperties: Dict[str, object]
    """Endpoint properties (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/endpoints?pivots=deployment-language-bicep#endpointproperties for details)."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    originResponseTimeoutSeconds: int
    """Send and receive timeout on forwarding request to the origin."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ruleSets: List['RuleSet']
    """Array of rule set objects."""
    secrets: List['Secret']
    """Array of secret objects."""
    securityPolicies: List['SecurityPolicy']
    """Array of Security Policy objects (see https://learn.microsoft.com/en-us/azure/templates/microsoft.cdn/profiles/securitypolicies for details)."""
    tags: Dict[str, object]
    """Endpoint tags."""


class CdnProfileOutputs(TypedDict, total=False):
    """Outputs for CdnProfile"""
    endpointId: Output[Literal['string']]
    """The resource ID of the CDN profile endpoint."""
    endpointName: Output[Literal['string']]
    """The name of the CDN profile endpoint."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the CDN profile."""
    profileType: Output[Literal['string']]
    """The type of the CDN profile."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the CDN profile is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the CDN profile."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    uri: Output[Literal['string']]
    """The uri of the CDN profile endpoint."""


class CdnProfileModule(Module):
    outputs: CdnProfileOutputs

