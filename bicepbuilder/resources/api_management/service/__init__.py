from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .api import Api
    from .api_version_set import ApiVersionSet
    from .authorization_server import AuthorizationServer
    from .backend import Backend
    from .cache import Cache
    from .identity_provider import IdentityProvider
    from .logger import Logger
    from .named_value import NamedValue
    from .policy import Policy
    from .portalsetting import Portalsetting
    from .product import Product
    from .subscription import Subscription


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class MetricCategory(TypedDict, total=False):
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    category: Required[str]
    """Name of a Diagnostic Metric category for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    metricCategories: List['MetricCategory']
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['API Management Developer Portal Content Editor', 'API Management Service Contributor', 'API Management Service Operator Role', 'API Management Service Reader Role', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class ApiManagementService(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the API Management service."""
    publisherEmail: Required[str]
    """The email address of the owner of the service."""
    publisherName: Required[str]
    """The name of the owner of the service."""
    skuCapacity: int
    """The scale units for this API Management service. Required if using Basic, Standard, or Premium skus. For range of capacities for each sku, reference https://azure.microsoft.com/en-us/pricing/details/api-management/."""
    additionalLocations: List[object]
    """Additional datacenter locations of the API Management service. Not supported with V2 SKUs."""
    apiDiagnostics: List[object]
    """API Diagnostics."""
    apis: List['Api']
    """APIs."""
    apiVersionSets: List['ApiVersionSet']
    """API Version Sets."""
    authorizationServers: 'AuthorizationServer'
    """Authorization servers."""
    backends: List['Backend']
    """Backends."""
    caches: List['Cache']
    """Caches."""
    certificates: List[object]
    """List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10."""
    customProperties: Dict[str, object]
    """Custom properties of the API Management service. Not supported if SKU is Consumption."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableGateway: bool
    """Property only valid for an API Management service deployed in multiple locations. This can be used to disable the gateway in master region."""
    enableClientCertificate: bool
    """Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    hostnameConfigurations: List[object]
    """Custom hostname configuration of the API Management service."""
    identityProviders: List['IdentityProvider']
    """Identity providers."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    loggers: List['Logger']
    """Loggers."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    minApiVersion: str
    """Limit control plane API calls to API Management service with version equal to or newer than this value."""
    namedValues: List['NamedValue']
    """Named values."""
    newGuidValue: str
    """Necessary to create a new GUID."""
    notificationSenderEmail: str
    """The notification sender email address for the service."""
    policies: List['Policy']
    """Policies."""
    portalsettings: List['Portalsetting']
    """Portal settings."""
    products: List['Product']
    """Products."""
    publicIpAddressResourceId: str
    """Public Standard SKU IP V4 based IP address to be associated with Virtual Network deployed service in the region. Supported only for Developer and Premium SKU being deployed in Virtual Network."""
    restore: bool
    """Undelete API Management Service if it was previously soft-deleted. If this flag is specified and set to True all other properties will be ignored."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    sku: Literal['Basic', 'BasicV2', 'Consumption', 'Developer', 'Premium', 'Standard', 'StandardV2']
    """The pricing tier of this API Management service."""
    subnetResourceId: str
    """The full resource ID of a subnet in a virtual network to deploy the API Management service in."""
    subscriptions: List['Subscription']
    """Subscriptions."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualNetworkType: Literal['External', 'Internal', 'None']
    """The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only."""
    zones: List[object]
    """A list of availability zones denoting where the resource needs to come from. Only supported by Premium sku."""


class ApiManagementServiceOutputs(TypedDict, total=False):
    """Outputs for ApiManagementService"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the API management service."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class ApiManagementServiceModule(Module):
    outputs: ApiManagementServiceOutputs

