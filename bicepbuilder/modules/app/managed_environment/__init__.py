from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class CertificateKeyVaultProperty(TypedDict, total=False):
    """A key vault reference to the certificate to use for the custom domain."""
    identityResourceId: Required[str]
    """The resource ID of the identity. This is the identity that will be used to access the key vault."""
    keyVaultUrl: Required[str]
    """A key vault URL referencing the wildcard certificate that will be used for the custom domain."""


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Storage(TypedDict, total=False):
    """The list of storages to mount on the environment."""
    accessMode: Required[Literal['ReadOnly', 'ReadWrite']]
    """Access mode for storage: "ReadOnly" or "ReadWrite"."""
    kind: Required[Literal['NFS', 'SMB']]
    """Type of storage: "SMB" or "NFS"."""
    shareName: Required[str]
    """File share name."""
    storageAccountName: Required[str]
    """Storage account name."""


class AppManagedEnvironment(TypedDict, total=False):
    """"""
    logAnalyticsWorkspaceResourceId: Required[str]
    """Existing Log Analytics Workspace resource ID. Note: This value is not required as per the resource type. However, not providing it currently causes an issue that is tracked """
    name: Required[str]
    """Name of the Container Apps Managed Environment."""
    dockerBridgeCidr: str
    """CIDR notation IP range assigned to the Docker bridge, network. It must not overlap with any other provided IP ranges and can only be used when the environment is deployed into a virtual network. If not provided, it will be set with a default value by the platform. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    infrastructureResourceGroupName: str
    """Name of the infrastructure resource group. If not provided, it will be set with a default value. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    infrastructureSubnetId: str
    """Resource ID of a subnet for infrastructure components. This is used to deploy the environment into a virtual network. Must not overlap with any other provided IP ranges. Required if "internal" is set to true. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    internal: bool
    """Boolean indicating the environment only has an internal load balancer. These environments do not have a public static IP resource. If set to true, then "infrastructureSubnetId" must be provided. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    platformReservedCidr: str
    """IP range in CIDR notation that can be reserved for environment infrastructure IP addresses. It must not overlap with any other provided IP ranges and can only be used when the environment is deployed into a virtual network. If not provided, it will be set with a default value by the platform. Required if zoneRedundant is set to true  to make the resource WAF compliant."""
    platformReservedDnsIP: str
    """An IP address from the IP range defined by "platformReservedCidr" that will be reserved for the internal DNS server. It must not be the first address in the range and can only be used when the environment is deployed into a virtual network. If not provided, it will be set with a default value by the platform. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    workloadProfiles: List[object]
    """Workload profiles configured for the Managed Environment. Required if zoneRedundant is set to true to make the resource WAF compliant."""
    appInsightsConnectionString: str
    """Application Insights connection string."""
    certificateKeyVaultProperties: 'CertificateKeyVaultProperty'
    """A key vault reference to the certificate to use for the custom domain."""
    certificatePassword: str
    """Password of the certificate used by the custom domain."""
    certificateValue: str
    """Certificate to use for the custom domain. PFX or PEM."""
    daprAIConnectionString: str
    """Application Insights connection string used by Dapr to export Service to Service communication telemetry."""
    daprAIInstrumentationKey: str
    """Azure Monitor instrumentation key used by Dapr to export Service to Service communication telemetry."""
    dnsSuffix: str
    """DNS suffix for the environment domain."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    logsDestination: str
    """Logs destination."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    openTelemetryConfiguration: Dict[str, object]
    """Open Telemetry configuration."""
    peerTrafficEncryption: bool
    """Whether or not to encrypt peer traffic."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    storages: List['Storage']
    """The list of storages to mount on the environment."""
    tags: Dict[str, object]
    """Tags of the resource."""
    zoneRedundant: bool
    """Whether or not this Managed Environment is zone-redundant."""


class AppManagedEnvironmentOutputs(TypedDict, total=False):
    """Outputs for AppManagedEnvironment"""
    defaultDomain: Output[Literal['string']]
    """The Default domain of the Managed Environment."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Managed Environment."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Managed Environment was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Managed Environment."""
    staticIp: Output[Literal['string']]
    """The IP address of the Managed Environment."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class AppManagedEnvironmentBicep(Module):
    outputs: AppManagedEnvironmentOutputs


def app_managed_environment(
        bicep: IO[str],
        params: AppManagedEnvironment,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.8.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AppManagedEnvironmentBicep:
    symbol = "app_managed_environment_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/managed-environment:{tag}' = {{\n")
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
    output = AppManagedEnvironmentBicep(symbol)
    output.outputs = {
            'defaultDomain': Output(symbol, 'defaultDomain', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'staticIp': Output(symbol, 'staticIp', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
