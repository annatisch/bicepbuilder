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


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


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
    roleDefinitionIdOrName: Required[str]
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


class Fhirservice(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the FHIR service."""
    accessPolicyObjectIds: List[object]
    """List of Azure AD object IDs (User or Apps) that is allowed access to the FHIR service."""
    acrLoginServers: List[object]
    """The list of the Azure container registry login servers."""
    acrOciArtifacts: List[object]
    """The list of Open Container Initiative (OCI) artifacts."""
    authenticationAudience: str
    """The audience url for the service."""
    authenticationAuthority: str
    """The authority url for the service."""
    corsAllowCredentials: bool
    """Use this setting to indicate that cookies should be included in CORS requests."""
    corsHeaders: List[object]
    """Specify HTTP headers which can be used during the request. Use "*" for any header."""
    corsMaxAge: int
    """Specify how long a result from a request can be cached in seconds. Example: 600 means 10 minutes."""
    corsMethods: Literal['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
    """Specify the allowed HTTP methods."""
    corsOrigins: List[object]
    """Specify URLs of origin sites that can access this API, or use "*" to allow access from any site."""
    exportStorageAccountName: str
    """The name of the default export storage account."""
    importEnabled: bool
    """If the import operation is enabled."""
    importStorageAccountName: str
    """The name of the default integration storage account."""
    initialImportMode: bool
    """If the FHIR service is in InitialImportMode."""
    kind: Literal['fhir-R4', 'fhir-Stu3']
    """The kind of the service. Defaults to R4."""
    location: str
    """Location for all resources."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Control permission for data plane traffic coming from public networks while private endpoint is enabled."""
    resourceVersionOverrides: Dict[str, object]
    """A list of FHIR Resources and their version policy overrides."""
    resourceVersionPolicy: Literal['no-version', 'versioned', 'versioned-update']
    """The default value for tracking history across all resources."""
    smartProxyEnabled: bool
    """If the SMART on FHIR proxy is enabled."""
    tags: Dict[str, object]
    """Tags of the resource."""


class FhirserviceOutputs(TypedDict, total=False):
    """Outputs for Fhirservice"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the fhir service."""
    resourceGroupName: Output[Literal['string']]
    """The resource group where the namespace is deployed."""
    resourceId: Output[Literal['string']]
    """The resource ID of the fhir service."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    workspaceName: Output[Literal['string']]
    """The name of the fhir workspace."""


class FhirserviceBicep(Module):
    outputs: FhirserviceOutputs

