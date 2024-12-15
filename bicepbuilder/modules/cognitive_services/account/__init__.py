from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class Deployment(TypedDict, total=False):
    """Array of deployments about cognitive service accounts to create."""
    name: str
    """Specify the name of cognitive service account deployment."""
    raiPolicyName: str
    """The name of RAI policy."""


class Model(TypedDict, total=False):
    """Properties of Cognitive Services account deployment model."""
    format: Required[str]
    """The format of Cognitive Services account deployment model."""
    name: Required[str]
    """The name of Cognitive Services account deployment model."""
    version: Required[str]
    """The version of Cognitive Services account deployment model."""


class Sku(TypedDict, total=False):
    """The resource model definition representing SKU."""
    name: Required[str]
    """The name of the resource model definition representing SKU."""
    capacity: int
    """The capacity of the resource model definition representing SKU."""


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
    """The name of the diagnostic setting."""
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
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the Private Endpoint IP configuration is included."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the Private Endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the Private Endpoint to."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the Private Endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different Resource Group than the main resource."""
    service: str
    """The subresource to deploy the Private Endpoint for. For example "vault" for a Key Vault Private Endpoint."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/Resource Groups in this deployment."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the Private Endpoint. This will be used to map to the first-party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class Lock(TypedDict, total=False):
    """Specify the type of lock."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS Zone Group to configure for the Private Endpoint."""
    name: str
    """The name of the Private DNS Zone Group."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS Zone Groups to associate the Private Endpoint. A DNS Zone Group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS Zone Group config."""


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


class SecretsExportConfiguration(TypedDict, total=False):
    """Key vault reference and secret settings for the module's secrets export."""
    keyVaultResourceId: Required[str]
    """The key vault name where to store the keys and connection strings generated by the modules."""
    accessKey1Name: str
    """The name for the accessKey1 secret to create."""
    accessKey2Name: str
    """The name for the accessKey2 secret to create."""


class Account(TypedDict, total=False):
    """"""
    kind: Required[Literal['AIServices', 'AnomalyDetector', 'CognitiveServices', 'ComputerVision', 'ContentModerator', 'ContentSafety', 'ConversationalLanguageUnderstanding', 'CustomVision.Prediction', 'CustomVision.Training', 'Face', 'FormRecognizer', 'HealthInsights', 'ImmersiveReader', 'Internal.AllInOne', 'LanguageAuthoring', 'LUIS', 'LUIS.Authoring', 'MetricsAdvisor', 'OpenAI', 'Personalizer', 'QnAMaker.v2', 'SpeechServices', 'TextAnalytics', 'TextTranslation']]
    """Kind of the Cognitive Services account. Use 'Get-AzCognitiveServicesAccountSku' to determine a valid combinations of 'kind' and 'SKU' for your Azure region."""
    name: Required[str]
    """The name of Cognitive Services account."""
    customSubDomainName: str
    """Subdomain name used for token-based authentication. Required if 'networkAcls' or 'privateEndpoints' are set."""
    allowedFqdnList: List[object]
    """List of allowed FQDN."""
    apiProperties: Dict[str, object]
    """The API properties for special APIs."""
    disableLocalAuth: bool
    """Allow only Azure AD authentication. Should be enabled for security reasons."""
    dynamicThrottlingEnabled: bool
    """The flag to enable dynamic throttling."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all Resources."""
    migrationToken: str
    """Resource migration token."""
    networkAcls: Dict[str, object]
    """A collection of rules governing the accessibility from specific network locations."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Whether or not public network access is allowed for this resource. For security reasons it should be disabled. If not specified, it will be disabled by default if private endpoints are set and networkAcls are not set."""
    restore: bool
    """Restore a soft-deleted cognitive service at deployment time. Will fail if no such soft-deleted resource exists."""
    restrictOutboundNetworkAccess: bool
    """Restrict outbound network access."""
    sku: Literal['C2', 'C3', 'C4', 'F0', 'F1', 'S', 'S0', 'S1', 'S10', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9']
    """SKU of the Cognitive Services account. Use 'Get-AzCognitiveServicesAccountSku' to determine a valid combinations of 'kind' and 'SKU' for your Azure region."""
    tags: Dict[str, object]
    """Tags of the resource."""
    userOwnedStorage: List[object]
    """The storage accounts for this resource."""


class AccountOutputs(TypedDict, total=False):
    """Outputs for Account"""
    endpoint: Output[Literal['string']]
    """The service endpoint of the cognitive services account."""
    endpoints: Output[Literal['object']]
    """All endpoints available for the cognitive services account, types depends on the cognitive service kind."""
    exportedSecrets: Output[Literal['object']]
    """A hashtable of references to the secrets exported to the provided Key Vault. The key of each reference is each secret's name."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the cognitive services account."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the congitive services account."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the cognitive services account was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the cognitive services account."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class AccountBicep(Module):
    outputs: AccountOutputs


def account(
        bicep: IO[str],
        /,
        *,
        params: Account,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.9.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'cognitive-services/account',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AccountBicep:
    symbol = "account_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} '{registry_prefix}/{path}:{tag}' = {{\n")
    bicep.write(f"  name: {resolve_value(name)}\n")
    if scope is not None:
        bicep.write(f"  scope: {resolve_value(scope)}\n")
    bicep.write(f"  params: {{\n")
    
    serialize_dict(bicep, params, indent="    ")
    bicep.write(f"  }}\n")
    if depends_on:
        bicep.write(f"  dependsOn: [\n")
        serialize_list(bicep, depends_on, indent="    ")
        bicep.write(f"  ]\n")
    bicep.write(f"}}\n")
    output = AccountBicep(symbol)
    output.outputs = {
            'endpoint': Output(symbol, 'endpoint', 'string'),
            'endpoints': Output(symbol, 'endpoints', 'object'),
            'exportedSecrets': Output(symbol, 'exportedSecrets', 'object'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
