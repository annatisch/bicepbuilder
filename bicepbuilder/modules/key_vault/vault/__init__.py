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


class AccessPolicy(TypedDict, total=False):
    """All access policies to create."""
    objectId: Required[str]
    """The object ID of a user, service principal or security group in the tenant for the vault."""
    applicationId: str
    """Application ID of the client making request on behalf of a principal."""
    tenantId: str
    """The tenant ID that is used for authenticating requests to the key vault."""


class Permission(TypedDict, total=False):
    """Permissions the identity has for keys, secrets and certificates."""
    certificates: Literal['all', 'backup', 'create', 'delete', 'deleteissuers', 'get', 'getissuers', 'import', 'list', 'listissuers', 'managecontacts', 'manageissuers', 'purge', 'recover', 'restore', 'setissuers', 'update']
    """Permissions to certificates."""
    keys: Literal['all', 'backup', 'create', 'decrypt', 'delete', 'encrypt', 'get', 'getrotationpolicy', 'import', 'list', 'purge', 'recover', 'release', 'restore', 'rotate', 'setrotationpolicy', 'sign', 'unwrapKey', 'update', 'verify', 'wrapKey']
    """Permissions to keys."""
    secrets: Literal['all', 'backup', 'delete', 'get', 'list', 'purge', 'recover', 'restore', 'set']
    """Permissions to secrets."""
    storage: Literal['all', 'backup', 'delete', 'deletesas', 'get', 'getsas', 'list', 'listsas', 'purge', 'recover', 'regeneratekey', 'restore', 'set', 'setsas', 'update']
    """Permissions to storage accounts."""


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


class Key(TypedDict, total=False):
    """All keys to create."""
    name: Required[str]
    """The name of the key."""
    curveName: Literal['P-256', 'P-256K', 'P-384', 'P-521']
    """The elliptic curve name. Only works if "keySize" equals "EC" or "EC-HSM". Default is "P-256"."""
    keyOps: Literal['decrypt', 'encrypt', 'import', 'release', 'sign', 'unwrapKey', 'verify', 'wrapKey']
    """The allowed operations on this key."""
    keySize: Literal[2048, 3072, 4096]
    """The key size in bits. Only works if "keySize" equals "RSA" or "RSA-HSM". Default is "4096"."""
    kty: Literal['EC', 'EC-HSM', 'RSA', 'RSA-HSM']
    """The type of the key. Default is "EC"."""
    tags: Dict[str, object]
    """Resource tags."""


class Attribute(TypedDict, total=False):
    """Contains attributes of the key."""
    enabled: bool
    """Defines whether the key is enabled or disabled."""
    exp: int
    """Defines when the key will become invalid. Defined in seconds since 1970-01-01T00:00:00Z."""
    nbf: int
    """If set, defines the date from which onwards the key becomes valid. Defined in seconds since 1970-01-01T00:00:00Z."""


class ReleasePolicy(TypedDict, total=False):
    """Key release policy."""
    contentType: str
    """Content type and version of key release policy."""
    data: str
    """Blob encoding the policy rules under which the key can be released."""


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


class RotationPolicy(TypedDict, total=False):
    """Key rotation policy."""


class Attribute(TypedDict, total=False):
    """The attributes of key rotation policy."""
    expiryTime: str
    """The expiration time for the new key version. It should be in ISO8601 format. Eg: "P90D", "P1Y"."""


class LifetimeAction(TypedDict, total=False):
    """The lifetimeActions for key rotation action."""


class Action(TypedDict, total=False):
    """The action of key rotation policy lifetimeAction."""
    type: Literal['Notify', 'Rotate']
    """The type of action."""


class Trigger(TypedDict, total=False):
    """The trigger of key rotation policy lifetimeAction."""
    timeAfterCreate: str
    """The time duration after key creation to rotate the key. It only applies to rotate. It will be in ISO 8601 duration format. Eg: "P90D", "P1Y"."""
    timeBeforeExpiry: str
    """The time duration before key expiring to rotate or notify. It will be in ISO 8601 duration format. Eg: "P90D", "P1Y"."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


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


class Secret(TypedDict, total=False):
    """All secrets to create."""
    name: Required[str]
    """The name of the secret."""
    value: Required[str]
    """The value of the secret. NOTE: "value" will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets."""
    contentType: str
    """The content type of the secret."""
    tags: Dict[str, object]
    """Resource tags."""


class Attribute(TypedDict, total=False):
    """Contains attributes of the secret."""
    enabled: bool
    """Defines whether the secret is enabled or disabled."""
    exp: int
    """Defines when the secret will become invalid. Defined in seconds since 1970-01-01T00:00:00Z."""
    nbf: int
    """If set, defines the date from which onwards the secret becomes valid. Defined in seconds since 1970-01-01T00:00:00Z."""


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


class Vault(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Key Vault. Must be globally unique."""
    createMode: str
    """The vault's create mode to indicate whether the vault need to be recovered or not. - recover or default."""
    enablePurgeProtection: bool
    """Provide 'true' to enable Key Vault's purge protection feature."""
    enableRbacAuthorization: bool
    """Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be ignored. When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. Note that management actions are always authorized with RBAC."""
    enableSoftDelete: bool
    """Switch to enable/disable Key Vault's soft delete feature."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    enableVaultForDeployment: bool
    """Specifies if the vault is enabled for deployment by script or compute."""
    enableVaultForDiskEncryption: bool
    """Specifies if the azure platform has access to the vault for enabling disk encryption scenarios."""
    enableVaultForTemplateDeployment: bool
    """Specifies if the vault is enabled for a template deployment."""
    location: str
    """Location for all resources."""
    networkAcls: Dict[str, object]
    """Rules governing the accessibility of the resource from specific network locations."""
    publicNetworkAccess: Literal['', 'Disabled', 'Enabled']
    """Whether or not public network access is allowed for this resource. For security reasons it should be disabled. If not specified, it will be disabled by default if private endpoints are set and networkAcls are not set."""
    sku: Literal['premium', 'standard']
    """Specifies the SKU for the vault."""
    softDeleteRetentionInDays: int
    """softDelete data retention days. It accepts >=7 and <=90."""
    tags: Dict[str, object]
    """Resource tags."""


class VaultOutputs(TypedDict, total=False):
    """Outputs for Vault"""
    keys: Output[Literal['array']]
    """The properties of the created keys."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the key vault."""
    privateEndpoints: Output[Literal['array']]
    """The private endpoints of the key vault."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the key vault was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the key vault."""
    secrets: Output[Literal['array']]
    """The properties of the created secrets."""
    uri: Output[Literal['string']]
    """The URI of the key vault."""


class VaultBicep(Module):
    outputs: VaultOutputs


def vault(
        bicep: IO[str],
        /,
        *,
        params: Vault,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'key-vault/vault',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> VaultBicep:
    symbol = "vault_" + generate_suffix()
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
    output = VaultBicep(symbol)
    output.outputs = {
            'keys': Output(symbol, 'keys', 'array'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'privateEndpoints': Output(symbol, 'privateEndpoints', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'secrets': Output(symbol, 'secrets', 'array'),
            'uri': Output(symbol, 'uri', 'string'),
        }

    return output
