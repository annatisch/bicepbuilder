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
    from .administrator import Administrator
    from .configuration import Configuration
    from .database import Database
    from .firewall_rule import FirewallRule


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Required if 'cMKKeyName' is not empty."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


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


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. Used when the desired connectivy mode is 'Public Access' and 'delegatedSubnetResourceId' is NOT used."""
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


class FlexibleServer(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the PostgreSQL flexible server."""
    skuName: Required[str]
    """The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3."""
    tier: Required[Literal['Burstable', 'GeneralPurpose', 'MemoryOptimized']]
    """The tier of the particular SKU. Tier must align with the 'skuName' property. Example, tier cannot be 'Burstable' if skuName is 'Standard_D4s_v3'."""
    pointInTimeUTC: str
    """Required if 'createMode' is set to 'PointInTimeRestore'."""
    sourceServerResourceId: str
    """Required if 'createMode' is set to 'PointInTimeRestore'."""
    administratorLogin: str
    """The administrator login name for the server. Can only be specified when the PostgreSQL server is being created."""
    administratorLoginPassword: str
    """The administrator login password."""
    administrators: List['Administrator']
    """The Azure AD administrators when AAD authentication enabled."""
    availabilityZone: Literal['', '1', '2', '3']
    """Availability zone information of the server. Default will have no preference set."""
    backupRetentionDays: int
    """Backup retention days for the server."""
    configurations: List['Configuration']
    """The configurations to create in the server."""
    createMode: Literal['Create', 'Default', 'GeoRestore', 'PointInTimeRestore', 'Replica', 'Update']
    """The mode to create a new PostgreSQL server."""
    databases: List['Database']
    """The databases to create in the server."""
    delegatedSubnetResourceId: str
    """Delegated subnet arm resource ID. Used when the desired connectivity mode is 'Private Access' - virtual network integration."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallRules: List['FirewallRule']
    """The firewall rules to create in the PostgreSQL flexible server."""
    geoRedundantBackup: Literal['Disabled', 'Enabled']
    """A value indicating whether Geo-Redundant backup is enabled on the server. Should be disabled if 'cMKKeyName' is not empty."""
    highAvailability: Literal['Disabled', 'SameZone', 'ZoneRedundant']
    """The mode for high availability."""
    location: str
    """Location for all resources."""
    maintenanceWindow: Dict[str, object]
    """Properties for the maintenence window. If provided, 'customWindow' property must exist and set to 'Enabled'."""
    privateDnsZoneArmResourceId: str
    """Private dns zone arm resource ID. Used when the desired connectivity mode is 'Private Access' and required when 'delegatedSubnetResourceId' is used. The Private DNS Zone must be linked to the Virtual Network referenced in 'delegatedSubnetResourceId'."""
    storageSizeGB: Literal[32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    """Max storage allowed for a server."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tenantId: str
    """Tenant id of the server."""
    version: Literal['11', '12', '13', '14', '15', '16']
    """PostgreSQL Server version."""


class FlexibleServerOutputs(TypedDict, total=False):
    """Outputs for FlexibleServer"""
    fqdn: Output[Literal['string']]
    """The FQDN of the PostgreSQL Flexible server."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed PostgreSQL Flexible server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed PostgreSQL Flexible server."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed PostgreSQL Flexible server."""


class FlexibleServerBicep(Module):
    outputs: FlexibleServerOutputs


def flexible_server(
        bicep: IO[str],
        /,
        *,
        params: FlexibleServer,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.6.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'db-for-postgre-sql/flexible-server',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> FlexibleServerBicep:
    symbol = "flexible_server_" + generate_suffix()
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
    output = FlexibleServerBicep(symbol)
    output.outputs = {
            'fqdn': Output(symbol, 'fqdn', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
