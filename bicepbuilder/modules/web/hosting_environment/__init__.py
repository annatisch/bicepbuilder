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


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to '' to disable log collection."""
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to 'AllLogs' to collect all logs."""


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to '' to disable log collection."""
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator (Preview)', 'User Access Administrator']]]
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


class WebHostingEnvironment(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the resource to create."""
    subnetResourceId: Required[str]
    """ResourceId for the subnet."""
    clusterSettings: List[object]
    """Custom settings for changing the behavior of the App Service Environment."""
    customDnsSuffix: str
    """Enable the default custom domain suffix to use for all sites deployed on the ASE. If provided, then customDnsSuffixCertificateUrl and customDnsSuffixKeyVaultReferenceIdentity are required."""
    customDnsSuffixCertificateUrl: str
    """The URL referencing the Azure Key Vault certificate secret that should be used as the default SSL/TLS certificate for sites with the custom domain suffix. Required if customDnsSuffix is not empty."""
    customDnsSuffixKeyVaultReferenceIdentity: str
    """The user-assigned identity to use for resolving the key vault certificate reference. If not specified, the system-assigned ASE identity will be used if available. Required if customDnsSuffix is not empty."""
    dedicatedHostCount: int
    """The Dedicated Host Count. If """
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    dnsSuffix: str
    """DNS suffix of the App Service Environment."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    frontEndScaleFactor: int
    """Scale factor for frontends."""
    internalLoadBalancingMode: Literal['None', 'Publishing', 'Web', 'Web, Publishing']
    """Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. - None, Web, Publishing, Web,Publishing. "None" Exposes the ASE-hosted apps on an internet-accessible IP address."""
    kind: Literal['ASEv3']
    """Kind of resource."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    networkConfiguration: Dict[str, object]
    """Properties to configure additional networking features."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""
    upgradePreference: Literal['Early', 'Late', 'Manual', 'None']
    """Specify preference for when and how the planned maintenance is applied."""
    zoneRedundant: bool
    """Switch to make the App Service Environment zone redundant. If enabled, the minimum App Service plan instance count will be three, otherwise 1. If enabled, the """


class WebHostingEnvironmentOutputs(TypedDict, total=False):
    """Outputs for WebHostingEnvironment"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the App Service Environment."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the App Service Environment was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the App Service Environment."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class WebHostingEnvironmentBicep(Module):
    outputs: WebHostingEnvironmentOutputs


def web_hosting_environment(
        bicep: IO[str],
        params: WebHostingEnvironment,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.2.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> WebHostingEnvironmentBicep:
    symbol = "web_hosting_environment_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/web/hosting-environment:{tag}' = {{\n")
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
    output = WebHostingEnvironmentBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
