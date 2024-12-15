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


class AuthorizationRule(TypedDict, total=False):
    """Authorization Rules for the Service Bus namespace."""
    name: Required[str]
    """The name of the authorization rule."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


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


class DisasterRecoveryConfig(TypedDict, total=False):
    """The disaster recovery configuration."""
    alternateName: str
    """Primary/Secondary eventhub namespace name, which is part of GEO DR pairing."""
    name: str
    """The name of the disaster recovery config."""
    partnerNamespace: str
    """Resource ID of the Primary/Secondary event hub namespace name, which is part of GEO DR pairing."""


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


class MigrationConfiguration(TypedDict, total=False):
    """The migration configuration."""
    postMigrationName: Required[str]
    """Name to access Standard Namespace after migration."""
    targetNamespace: Required[str]
    """Existing premium Namespace resource ID which has no entities, will be used for migration."""


class NetworkRuleSet(TypedDict, total=False):
    """Configure networking options for Premium SKU Service Bus. This object contains IPs/Subnets to allow or restrict access to private endpoints only. For security reasons, it is recommended to configure this object on the Namespace."""
    defaultAction: Literal['Allow', 'Deny']
    """Default Action for Network Rule Set. Default is "Allow". It will not be set if publicNetworkAccess is "Disabled". Otherwise, it will be set to "Deny" if ipRules or virtualNetworkRules are being used."""
    publicNetworkAccess: Literal['Disabled', 'Enabled']
    """This determines if traffic is allowed over public network. Default is "Enabled". If set to "Disabled", traffic to this namespace will be restricted over Private Endpoints only and network rules will not be applied."""
    trustedServiceAccessEnabled: bool
    """Value that indicates whether Trusted Service Access is enabled or not. Default is "true". It will not be set if publicNetworkAccess is "Disabled"."""


class IpRule(TypedDict, total=False):
    """List of IpRules. It will not be set if publicNetworkAccess is "Disabled". Otherwise, when used, defaultAction will be set to "Deny"."""
    action: Required[Literal['Allow', 'Deny']]
    """The IP filter action."""
    ipMask: Required[str]
    """The IP mask."""


class VirtualNetworkRule(TypedDict, total=False):
    """List virtual network rules. It will not be set if publicNetworkAccess is "Disabled". Otherwise, when used, defaultAction will be set to "Deny"."""
    ignoreMissingVnetServiceEndpoint: Required[bool]
    """The virtual network rule name."""
    subnetResourceId: Required[str]
    """The ID of the subnet."""


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


class Queue(TypedDict, total=False):
    """The queues to create in the service bus namespace."""
    name: Required[str]
    """The name of the queue."""
    autoDeleteOnIdle: str
    """ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes (PT5M)."""
    deadLetteringOnMessageExpiration: bool
    """A value that indicates whether this queue has dead letter support when a message expires."""
    defaultMessageTimeToLive: str
    """ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """Value that indicates whether server-side batched operations are enabled."""
    enableExpress: bool
    """A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage. This property is only used if the """
    enablePartitioning: bool
    """A value that indicates whether the queue is to be partitioned across multiple message brokers."""
    forwardDeadLetteredMessagesTo: str
    """Queue/Topic name to forward the Dead Letter message."""
    forwardTo: str
    """Queue/Topic name to forward the messages."""
    lockDuration: str
    """ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute."""
    maxDeliveryCount: int
    """The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10."""
    maxMessageSizeInKilobytes: int
    """Maximum size (in KB) of the message payload that can be accepted by the queue. This property is only used in Premium today and default is 1024."""
    maxSizeInMegabytes: int
    """The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024."""
    requiresDuplicateDetection: bool
    """A value indicating if this queue requires duplicate detection."""
    requiresSession: bool
    """A value that indicates whether the queue supports the concept of sessions."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""


class AuthorizationRule(TypedDict, total=False):
    """Authorization Rules for the Service Bus Queue."""
    name: Required[str]
    """The name of the authorization rule."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


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


class SkuObject(TypedDict, total=False):
    """The SKU of the Service Bus Namespace. Defaulted to Premium for ZoneRedundant configurations by default."""
    name: Required[Literal['Basic', 'Premium', 'Standard']]
    """Name of this SKU. - Basic, Standard, Premium."""
    capacity: int
    """The specified messaging units for the tier. Only used for Premium Sku tier."""


class Topic(TypedDict, total=False):
    """The topics to create in the service bus namespace."""
    name: Required[str]
    """The name of the topic."""
    autoDeleteOnIdle: str
    """ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes."""
    defaultMessageTimeToLive: str
    """ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """Value that indicates whether server-side batched operations are enabled."""
    enableExpress: bool
    """A value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage. This property is only used if the """
    enablePartitioning: bool
    """A value that indicates whether the topic is to be partitioned across multiple message brokers."""
    maxMessageSizeInKilobytes: int
    """Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024."""
    maxSizeInMegabytes: int
    """The maximum size of the topic in megabytes, which is the size of memory allocated for the topic. Default is 1024."""
    requiresDuplicateDetection: bool
    """A value indicating if this topic requires duplicate detection."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""
    supportOrdering: bool
    """Value that indicates whether the topic supports ordering."""


class AuthorizationRule(TypedDict, total=False):
    """Authorization Rules for the Service Bus Topic."""
    name: Required[str]
    """The name of the authorization rule."""
    rights: Literal['Listen', 'Manage', 'Send']
    """The rights associated with the rule."""


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


class Subscription(TypedDict, total=False):
    """The subscriptions of the topic."""
    name: Required[str]
    """The name of the service bus namespace topic subscription."""
    autoDeleteOnIdle: str
    """ISO 8601 timespan idle interval after which the syubscription is automatically deleted. The minimum duration is 5 minutes."""
    deadLetteringOnFilterEvaluationExceptions: bool
    """A value that indicates whether a subscription has dead letter support when a message expires."""
    deadLetteringOnMessageExpiration: bool
    """A value that indicates whether a subscription has dead letter support when a message expires."""
    defaultMessageTimeToLive: str
    """ISO 8601 timespan idle interval after which the message expires. The minimum duration is 5 minutes."""
    duplicateDetectionHistoryTimeWindow: str
    """ISO 8601 timespan that defines the duration of the duplicate detection history. The default value is 10 minutes."""
    enableBatchedOperations: bool
    """A value that indicates whether server-side batched operations are enabled."""
    forwardDeadLetteredMessagesTo: str
    """The name of the recipient entity to which all the messages sent to the subscription are forwarded to."""
    forwardTo: str
    """The name of the recipient entity to which all the messages sent to the subscription are forwarded to."""
    isClientAffine: bool
    """A value that indicates whether the subscription supports the concept of session."""
    lockDuration: str
    """ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute."""
    maxDeliveryCount: int
    """Number of maximum deliveries. A message is automatically deadlettered after this number of deliveries. Default value is 10."""
    requiresSession: bool
    """A value that indicates whether the subscription supports the concept of session."""
    status: Literal['Active', 'Creating', 'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring', 'SendDisabled', 'Unknown']
    """Enumerates the possible values for the status of a messaging entity. - Active, Disabled, Restoring, SendDisabled, ReceiveDisabled, Creating, Deleting, Renaming, Unknown."""


class ClientAffineProperty(TypedDict, total=False):
    """The properties that are associated with a subscription that is client-affine."""
    clientId: Required[str]
    """Indicates the Client ID of the application that created the client-affine subscription."""
    isDurable: bool
    """For client-affine subscriptions, this value indicates whether the subscription is durable or not."""
    isShared: bool
    """For client-affine subscriptions, this value indicates whether the subscription is shared or not."""


class Namespace(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Service Bus Namespace."""
    alternateName: str
    """Alternate name for namespace."""
    disableLocalAuth: bool
    """This property disables SAS authentication for the Service Bus namespace."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    minimumTlsVersion: Literal['1.0', '1.1', '1.2']
    """The minimum TLS version for the cluster to support."""
    premiumMessagingPartitions: int
    """The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4."""
    publicNetworkAccess: Literal['', 'Disabled', 'Enabled', 'SecuredByPerimeter']
    """Whether or not public network access is allowed for this resource. For security reasons it should be disabled. If not specified, it will be disabled by default if private endpoints are set."""
    requireInfrastructureEncryption: bool
    """Enable infrastructure encryption (double encryption). Note, this setting requires the configuration of Customer-Managed-Keys (CMK) via the corresponding module parameters."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneRedundant: bool
    """Enabled by default in order to align with resiliency best practices, thus requires Premium SKU."""


class NamespaceOutputs(TypedDict, total=False):
    """Outputs for Namespace"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed service bus namespace."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the service bus namespace."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed service bus namespace."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed service bus namespace."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class NamespaceBicep(Module):
    outputs: NamespaceOutputs


def namespace(
        bicep: IO[str],
        /,
        *,
        params: Namespace,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.10.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'service-bus/namespace',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NamespaceBicep:
    symbol = "namespace_" + generate_suffix()
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
    output = NamespaceBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
