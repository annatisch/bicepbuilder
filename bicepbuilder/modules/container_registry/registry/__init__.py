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

if TYPE_CHECKING:
    from .cache_rule import CacheRule
    from .credential_set import CredentialSet
    from .replication import Replication
    from .webhook import Webhook


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, using 'latest'."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


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


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible. Note, requires the 'acrSku' to be 'Premium'."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the private endpoint IP configuration is included."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the private endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the private endpoint to."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the private endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different resource group than the main resource."""
    service: str
    """The subresource to deploy the private endpoint for. For example "vault", "mysqlServer" or "dataFactory"."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
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
    """The private DNS zone group to configure for the private endpoint."""
    name: str
    """The name of the Private DNS Zone Group."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


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


class ScopeMap(TypedDict, total=False):
    """Scope maps setting."""
    actions: Required[List[object]]
    """The list of scoped permissions for registry artifacts."""
    description: str
    """The user friendly description of the scope map."""
    name: str
    """The name of the scope map."""


class Registry(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of your Azure Container Registry."""
    acrAdminUserEnabled: bool
    """Enable admin user that have push / pull permission to the registry."""
    acrSku: Literal['Basic', 'Premium', 'Standard']
    """Tier of your Azure container registry."""
    anonymousPullEnabled: bool
    """Enables registry-wide pull from unauthenticated clients. It's in preview and available in the Standard and Premium service tiers."""
    azureADAuthenticationAsArmPolicyStatus: Literal['disabled', 'enabled']
    """The value that indicates whether the policy for using ARM audience token for a container registr is enabled or not. Default is enabled."""
    cacheRules: List['CacheRule']
    """Array of Cache Rules."""
    credentialSets: List['CredentialSet']
    """Array of Credential Sets."""
    dataEndpointEnabled: bool
    """Enable a single data endpoint per region for serving data. Not relevant in case of disabled public access. Note, requires the 'acrSku' to be 'Premium'."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    exportPolicyStatus: Literal['disabled', 'enabled']
    """The value that indicates whether the export policy is enabled or not."""
    location: str
    """Location for all resources."""
    networkRuleBypassOptions: Literal['AzureServices', 'None']
    """Whether to allow trusted Azure services to access a network restricted registry."""
    networkRuleSetDefaultAction: Literal['Allow', 'Deny']
    """The default action of allow or deny when no other rules match."""
    networkRuleSetIpRules: List[object]
    """The IP ACL rules. Note, requires the 'acrSku' to be 'Premium'."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """Whether or not public network access is allowed for this resource. For security reasons it should be disabled. If not specified, it will be disabled by default if private endpoints are set and networkRuleSetIpRules are not set.  Note, requires the 'acrSku' to be 'Premium'."""
    quarantinePolicyStatus: Literal['disabled', 'enabled']
    """The value that indicates whether the quarantine policy is enabled or not. Note, requires the 'acrSku' to be 'Premium'."""
    replications: List['Replication']
    """All replications to create."""
    retentionPolicyDays: int
    """The number of days to retain an untagged manifest after which it gets purged."""
    retentionPolicyStatus: Literal['disabled', 'enabled']
    """The value that indicates whether the retention policy is enabled or not."""
    softDeletePolicyDays: int
    """The number of days after which a soft-deleted item is permanently deleted."""
    softDeletePolicyStatus: Literal['disabled', 'enabled']
    """Soft Delete policy status. Default is disabled."""
    tags: Dict[str, object]
    """Tags of the resource."""
    trustPolicyStatus: Literal['disabled', 'enabled']
    """The value that indicates whether the trust policy is enabled or not. Note, requires the 'acrSku' to be 'Premium'."""
    webhooks: List['Webhook']
    """All webhooks to create."""
    zoneRedundancy: Literal['Disabled', 'Enabled']
    """Whether or not zone redundancy is enabled for this container registry."""


class RegistryOutputs(TypedDict, total=False):
    """Outputs for Registry"""
    credentialSetsResourceIds: Output[Literal['array']]
    """The Resource IDs of the ACR Credential Sets."""
    credentialSetsSystemAssignedMIPrincipalIds: Output[Literal['array']]
    """The Principal IDs of the ACR Credential Sets system-assigned identities."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    loginServer: Output[Literal['string']]
    """The reference to the Azure container registry."""
    name: Output[Literal['string']]
    """The Name of the Azure container registry."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the Azure container registry."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Azure container registry."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Azure container registry."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class RegistryBicep(Module):
    outputs: RegistryOutputs


def registry(
        bicep: IO[str],
        /,
        *,
        params: Registry,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'container-registry/registry',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> RegistryBicep:
    symbol = "registry_" + generate_suffix()
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
    output = RegistryBicep(symbol)
    output.outputs = {
            'credentialSetsResourceIds': Output(symbol, 'credentialSetsResourceIds', 'array'),
            'credentialSetsSystemAssignedMIPrincipalIds': Output(symbol, 'credentialSetsSystemAssignedMIPrincipalIds', 'array'),
            'location': Output(symbol, 'location', 'string'),
            'loginServer': Output(symbol, 'loginServer', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
