from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
    Output,
)

if TYPE_CHECKING:
    from .ca_certificate import CaCertificate
    from .client_group import ClientGroup
    from .client import Client
    from .permission_binding import PermissionBinding
    from .topic import Topic
    from .topic_space import TopicSpace


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


class CustomDnsConfig(TypedDict, total=False):
    """Custom DNS configurations."""
    ipAddresses: Required[List[object]]
    """A list of private IP addresses of the private endpoint."""
    fqdn: str
    """FQDN that resolves to private endpoint IP address."""


class IpConfigurationProperties(TypedDict, total=False):
    """Properties of private endpoint IP configurations."""
    groupId: Required[str]
    """The ID of a group obtained from the remote resource that this private endpoint should connect to."""
    memberName: Required[str]
    """The member name of a group obtained from the remote resource that this private endpoint should connect to."""
    privateIPAddress: Required[str]
    """A private IP address obtained from the private endpoint's subnet."""


class IpConfiguration(TypedDict, total=False):
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    name: Required[str]
    """The name of the resource that is unique within a resource group."""
    properties: Required['IpConfigurationProperties']
    """Properties of private endpoint IP configurations."""


class Lock(TypedDict, total=False):
    """Specify the type of lock."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class PrivateDnsZoneGroupConfig(TypedDict, total=False):
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    privateDnsZoneResourceId: Required[str]
    """The resource id of the private DNS zone."""
    name: str
    """The name of the private DNS zone group config."""


class PrivateDnsZoneGroup(TypedDict, total=False):
    """The private DNS zone group to configure for the private endpoint."""
    privateDnsZoneGroupConfigs: Required[List['PrivateDnsZoneGroupConfig']]
    """The private DNS zone groups to associate the private endpoint. A DNS zone group can support up to 5 DNS zones."""
    name: str
    """The name of the Private DNS Zone Group."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator (Preview)']]]
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


class PrivateEndpoint(TypedDict, total=False):
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    subnetResourceId: Required[str]
    """Resource ID of the subnet where the endpoint needs to be created."""
    applicationSecurityGroupResourceIds: List[object]
    """Application security groups in which the private endpoint IP configuration is included."""
    customDnsConfigs: List['CustomDnsConfig']
    """Custom DNS configurations."""
    customNetworkInterfaceName: str
    """The custom name of the network interface attached to the private endpoint."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    ipConfigurations: List['IpConfiguration']
    """A list of IP configurations of the private endpoint. This will be used to map to the First Party Service endpoints."""
    isManualConnection: bool
    """If Manual Private Link Connection is required."""
    location: str
    """The location to deploy the private endpoint to."""
    lock: 'Lock'
    """Specify the type of lock."""
    manualConnectionRequestMessage: str
    """A message passed to the owner of the remote resource with the manual connection request."""
    name: str
    """The name of the private endpoint."""
    privateDnsZoneGroup: 'PrivateDnsZoneGroup'
    """The private DNS zone group to configure for the private endpoint."""
    privateLinkServiceConnectionName: str
    """The name of the private link connection to create."""
    resourceGroupName: str
    """Specify if you want to deploy the Private Endpoint into a different resource group than the main resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    service: str
    """The subresource to deploy the private endpoint for. For example "vault", "mysqlServer" or "dataFactory"."""
    tags: Dict[str, object]
    """Tags to be applied on all resources/resource groups in this deployment."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Resource Notifications System Topics Subscriber', 'Contributor', 'EventGrid Contributor', 'EventGrid Data Contributor', 'EventGrid Data Receiver', 'EventGrid Data Sender', 'EventGrid EventSubscription Contributor', 'EventGrid EventSubscription Reader', 'EventGrid TopicSpaces Publisher', 'EventGrid TopicSpaces Subscriber', 'Owner', 'Reader', 'User Access Administrator']]]
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


class EventGridNamespace(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Event Grid Namespace to create."""
    routingIdentityInfo: Dict[str, object]
    """Routing identity info for topic spaces configuration. Required if the 'routeTopicResourceId' points to a topic outside of the current Event Grid Namespace.  Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled') and routing is enabled ('routeTopicResourceId' is set)."""
    alternativeAuthenticationNameSources: Literal['ClientCertificateDns', 'ClientCertificateEmail', 'ClientCertificateIp', 'ClientCertificateSubject', 'ClientCertificateUri']
    """Alternative authentication name sources related to client authentication settings for namespace resource. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    caCertificates: List['CaCertificate']
    """CA certificates (Root or intermediate) used to sign the client certificates for clients authenticated using CA-signed certificates.  Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    clientGroups: List['ClientGroup']
    """All namespace Client Groups to create. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    clients: List['Client']
    """All namespace Clients to create. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    inboundIpRules: List[object]
    """This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled."""
    isZoneRedundant: bool
    """Allows the user to specify if the namespace resource supports zone-redundancy capability or not. If this property is not specified explicitly by the user, its default value depends on the following conditions: a. For Availability Zones enabled regions - The default property value would be true. b. For non-Availability Zones enabled regions - The default property value would be false. Once specified, this property cannot be updated."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    maximumClientSessionsPerAuthenticationName: int
    """The maximum number of sessions per authentication name. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    maximumSessionExpiryInHours: int
    """The maximum session expiry in hours. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    permissionBindings: List['PermissionBinding']
    """All namespace Permission Bindings to create. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    privateEndpoints: List['PrivateEndpoint']
    """Configuration details for private endpoints. For security reasons, it is recommended to use private endpoints whenever possible."""
    publicNetworkAccess: Literal['Disabled', 'Enabled', 'SecuredByPerimeter']
    """This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    routeTopicResourceId: str
    """Resource Id for the Event Grid Topic to which events will be routed to from TopicSpaces under a namespace. This enables routing of the MQTT messages to an Event Grid Topic. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled'). Note that the topic must exist prior to deployment, meaning: if referencing a topic in the same namespace, the deployment must be launched twice: 1. To create the topic 2. To enable the routing this topic."""
    routingEnrichments: Dict[str, object]
    """Routing enrichments for topic spaces configuration.  Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled') and routing is enabled ('routeTopicResourceId' is set)."""
    tags: Dict[str, object]
    """Resource tags."""
    topics: List['Topic']
    """All namespace Topics to create."""
    topicSpaces: List['TopicSpace']
    """All namespace Topic Spaces to create. Used only when MQTT broker is enabled ('topicSpacesState' is set to 'Enabled')."""
    topicSpacesState: Literal['Disabled', 'Enabled']
    """Indicates if Topic Spaces Configuration is enabled for the namespace. This enables the MQTT Broker functionality for the namespace. Once enabled, this property cannot be disabled."""


class EventGridNamespaceOutputs(TypedDict, total=False):
    """Outputs for EventGridNamespace"""
    location: Output[Literal['string']]
    """The location the EventGrid Namespace was deployed into."""
    name: Output[Literal['string']]
    """The name of the EventGrid Namespace."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the EventGrid Namespace."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the EventGrid Namespace was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the EventGrid Namespace."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    topicResourceIds: Output[Literal['array']]
    """The Resources IDs of the EventGrid Namespace Topics."""


class EventGridNamespaceModule(Module):
    outputs: EventGridNamespaceOutputs


def _event_grid_namespace(
        bicep: IO[str],
        params: EventGridNamespace,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> EventGridNamespaceModule:
    symbol = "event_grid_namespace_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/event-grid/namespace:{tag}' = {{\n")
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
    output = EventGridNamespaceModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
            'topicResourceIds': Output(symbol, 'topicResourceIds', 'array'),
        }

    return output
