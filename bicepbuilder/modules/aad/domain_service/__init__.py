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


class ReplicaSet(TypedDict, total=False):
    """Additional replica set for the managed domain."""
    location: Required[str]
    """Virtual network location."""
    subnetId: Required[str]
    """The id of the subnet that Domain Services will be deployed on. The subnet has some requirements, which are outlined in the """


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


class AadDomainService(TypedDict, total=False):
    """"""
    domainName: Required[str]
    """The domain name specific to the Azure ADDS service."""
    pfxCertificate: str
    """The certificate required to configure Secure LDAP. Should be a base64encoded representation of the certificate PFX file and contain the domainName as CN. Required if secure LDAP is enabled and must be valid more than 30 days."""
    pfxCertificatePassword: str
    """The password to decrypt the provided Secure LDAP certificate PFX file. Required if secure LDAP is enabled."""
    additionalRecipients: List[object]
    """The email recipient value to receive alerts."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    domainConfigurationType: Literal['FullySynced', 'ResourceTrusting']
    """The value is to provide domain configuration type."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    externalAccess: Literal['Disabled', 'Enabled']
    """The value is to enable the Secure LDAP for external services of Azure ADDS Services."""
    filteredSync: Literal['Disabled', 'Enabled']
    """The value is to synchronize scoped users and groups."""
    kerberosArmoring: Literal['Disabled', 'Enabled']
    """The value is to enable to provide a protected channel between the Kerberos client and the KDC."""
    kerberosRc4Encryption: Literal['Disabled', 'Enabled']
    """The value is to enable Kerberos requests that use RC4 encryption."""
    ldaps: Literal['Disabled', 'Enabled']
    """A flag to determine whether or not Secure LDAP is enabled or disabled."""
    location: str
    """The location to deploy the Azure ADDS Services. Uses the resource group location if not specified."""
    lock: 'Lock'
    """The lock settings of the service."""
    name: str
    """The name of the AADDS resource. Defaults to the domain name specific to the Azure ADDS service. The prefix of your specified domain name (such as dscontoso in the dscontoso.com domain name) must contain 15 or fewer characters."""
    notifyDcAdmins: Literal['Disabled', 'Enabled']
    """The value is to notify the DC Admins."""
    notifyGlobalAdmins: Literal['Disabled', 'Enabled']
    """The value is to notify the Global Admins."""
    ntlmV1: Literal['Disabled', 'Enabled']
    """The value is to enable clients making request using NTLM v1."""
    replicaSets: List['ReplicaSet']
    """Additional replica set for the managed domain."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    sku: Literal['Enterprise', 'Premium', 'Standard']
    """The name of the SKU specific to Azure ADDS Services."""
    syncNtlmPasswords: Literal['Disabled', 'Enabled']
    """The value is to enable synchronized users to use NTLM authentication."""
    syncOnPremPasswords: Literal['Disabled', 'Enabled']
    """The value is to enable on-premises users to authenticate against managed domain."""
    tags: Dict[str, object]
    """Tags of the resource."""
    tlsV1: Literal['Disabled', 'Enabled']
    """The value is to enable clients making request using TLSv1."""


class AadDomainServiceOutputs(TypedDict, total=False):
    """Outputs for AadDomainService"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The domain name of the Azure Active Directory Domain Services(Azure ADDS)."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Azure Active Directory Domain Services(Azure ADDS) was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Azure Active Directory Domain Services(Azure ADDS)."""


class AadDomainServiceBicep(Module):
    outputs: AadDomainServiceOutputs


def aad_domain_service(
        bicep: IO[str],
        params: AadDomainService,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AadDomainServiceBicep:
    symbol = "aad_domain_service_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/aad/domain-service:{tag}' = {{\n")
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
    output = AadDomainServiceBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
