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
    from .database import Database
    from .firewall_rule import FirewallRule


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Required if 'customerManagedKey' is not empty."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition to use for the managed service."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class CustomerManagedKeyGeo(TypedDict, total=False):
    """The customer managed key definition to use when geoRedundantBackup is "Enabled"."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
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
    """The name of the MySQL flexible server."""
    skuName: Required[str]
    """The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3."""
    tier: Required[Literal['Burstable', 'GeneralPurpose', 'MemoryOptimized']]
    """The tier of the particular SKU. Tier must align with the "skuName" property. Example, tier cannot be "Burstable" if skuName is "Standard_D4s_v3"."""
    privateDnsZoneResourceId: str
    """Private dns zone arm resource ID. Used when the desired connectivity mode is "Private Access". Required if "delegatedSubnetResourceId" is used and the Private DNS Zone name must end with mysql.database.azure.com in order to be linked to the MySQL Flexible Server."""
    restorePointInTime: str
    """Restore point creation time (ISO8601 format), specifying the time to restore from. Required if "createMode" is set to "PointInTimeRestore"."""
    sourceServerResourceId: str
    """The source MySQL server ID. Required if "createMode" is set to "PointInTimeRestore"."""
    storageAutoGrow: Literal['Disabled', 'Enabled']
    """Enable Storage Auto Grow or not. Storage auto-growth prevents a server from running out of storage and becoming read-only. Required if "highAvailability" is not "Disabled"."""
    administratorLogin: str
    """The administrator login name of a server. Can only be specified when the MySQL server is being created."""
    administratorLoginPassword: str
    """The administrator login password."""
    administrators: List['Administrator']
    """The Azure AD administrators when AAD authentication enabled."""
    availabilityZone: Literal['', '1', '2', '3']
    """Availability zone information of the server. Default will have no preference set."""
    backupRetentionDays: int
    """Backup retention days for the server."""
    createMode: Literal['Default', 'GeoRestore', 'PointInTimeRestore', 'Replica']
    """The mode to create a new MySQL server."""
    databases: List['Database']
    """The databases to create in the server."""
    delegatedSubnetResourceId: str
    """Delegated subnet arm resource ID. Used when the desired connectivity mode is "Private Access" - virtual network integration. Delegation must be enabled on the subnet for MySQL Flexible Servers and subnet CIDR size is /29."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    firewallRules: List['FirewallRule']
    """The firewall rules to create in the MySQL flexible server."""
    geoRedundantBackup: Literal['Disabled', 'Enabled']
    """A value indicating whether Geo-Redundant backup is enabled on the server. If "Enabled" and "cMKKeyName" is not empty, then "geoBackupCMKKeyVaultResourceId" and "cMKUserAssignedIdentityResourceId" are also required."""
    highAvailability: Literal['Disabled', 'SameZone', 'ZoneRedundant']
    """The mode for High Availability (HA). It is not supported for the Burstable pricing tier and Zone redundant HA can only be set during server provisioning."""
    highAvailabilityZone: str
    """Standby availability zone information of the server. Default will have no preference set."""
    location: str
    """Location for all resources."""
    maintenanceWindow: Dict[str, object]
    """Properties for the maintenence window. If provided, "customWindow" property must exist and set to "Enabled"."""
    replicationRole: Literal['None', 'Replica', 'Source']
    """The replication role."""
    storageAutoIoScaling: Literal['Disabled', 'Enabled']
    """Enable IO Auto Scaling or not. The server scales IOPs up or down automatically depending on your workload needs."""
    storageIOPS: int
    """Storage IOPS for a server. Max IOPS are determined by compute size."""
    storageSizeGB: Literal[20, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    """Max storage allowed for a server. In all compute tiers, the minimum storage supported is 20 GiB and maximum is 16 TiB."""
    tags: Dict[str, object]
    """Tags of the resource."""
    version: Literal['5.7', '8.0.21']
    """MySQL Server version."""


class FlexibleServerOutputs(TypedDict, total=False):
    """Outputs for FlexibleServer"""
    fqdn: Output[Literal['string']]
    """The FQDN of the MySQL Flexible server."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed MySQL Flexible server."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed MySQL Flexible server."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed MySQL Flexible server."""


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
        tag: str = '0.5.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'db-for-my-sql/flexible-server',
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
