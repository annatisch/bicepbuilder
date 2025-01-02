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


class EnvironmentVariable(TypedDict, total=False):
    """The environment variables to pass over to the script."""
    name: Required[str]
    """The name of the environment variable."""
    secureValue: str
    """The value of the secure environment variable. Required if """
    value: str
    """The value of the environment variable. Required if """


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


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


class ResourcesDeploymentScript(TypedDict, total=False):
    """"""
    kind: Required[Literal['AzureCLI', 'AzurePowerShell']]
    """Specifies the Kind of the Deployment Script."""
    name: Required[str]
    """Name of the Deployment Script."""
    arguments: str
    """Command-line arguments to pass to the script. Arguments are separated by spaces."""
    azCliVersion: str
    """Azure CLI module version to be used. See a list of supported Azure CLI versions: https://mcr.microsoft.com/v2/azure-cli/tags/list."""
    azPowerShellVersion: str
    """Azure PowerShell module version to be used. See a list of supported Azure PowerShell versions: https://mcr.microsoft.com/v2/azuredeploymentscripts-powershell/tags/list."""
    cleanupPreference: Literal['Always', 'OnExpiration', 'OnSuccess']
    """The clean up preference when the script execution gets in a terminal state. Specify the preference on when to delete the deployment script resources. The default value is Always, which means the deployment script resources are deleted despite the terminal state (Succeeded, Failed, canceled)."""
    containerGroupName: str
    """Container group name, if not specified then the name will get auto-generated. Not specifying a 'containerGroupName' indicates the system to generate a unique name which might end up flagging an Azure Policy as non-compliant. Use 'containerGroupName' when you have an Azure Policy that expects a specific naming convention or when you want to fully control the name. 'containerGroupName' property must be between 1 and 63 characters long, must contain only lowercase letters, numbers, and dashes and it cannot start or end with a dash and consecutive dashes are not allowed."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    environmentVariables: List['EnvironmentVariable']
    """The environment variables to pass over to the script."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    primaryScriptUri: str
    """Uri for the external script. This is the entry point for the external script. To run an internal script, use the scriptContent parameter instead."""
    retentionInterval: str
    """Interval for which the service retains the script resource after it reaches a terminal state. Resource will be deleted when this duration expires. Duration is based on ISO 8601 pattern (for example P7D means one week)."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
    """Array of role assignments to create."""
    runOnce: bool
    """When set to false, script will run every time the template is deployed. When set to true, the script will only run once."""
    scriptContent: str
    """Script body. Max length: 32000 characters. To run an external script, use primaryScriptURI instead."""
    storageAccountResourceId: str
    """The resource ID of the storage account to use for this deployment script. If none is provided, the deployment script uses a temporary, managed storage account."""
    subnetResourceIds: List[object]
    """List of subnet IDs to use for the container group. This is required if you want to run the deployment script in a private network. When using a private network, the """
    supportingScriptUris: List[object]
    """List of supporting files for the external script (defined in primaryScriptUri). Does not work with internal scripts (code defined in scriptContent)."""
    tags: Dict[str, object]
    """Resource tags."""
    timeout: str
    """Maximum allowed script execution time specified in ISO 8601 format. Default value is PT1H - 1 hour; 'PT30M' - 30 minutes; 'P5D' - 5 days; 'P1Y' 1 year."""
    baseTime: str
    """Do not provide a value! This date value is used to make sure the script run every time the template is deployed."""


class ResourcesDeploymentScriptOutputs(TypedDict, total=False):
    """Outputs for ResourcesDeploymentScript"""
    deploymentScriptLogs: Output[Literal['array']]
    """The logs of the deployment script."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployment script."""
    outputs: Output[Literal['object']]
    """The output of the deployment script."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the deployment script was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployment script."""


class ResourcesDeploymentScriptBicep(Module):
    outputs: ResourcesDeploymentScriptOutputs


def resources_deployment_script(
        bicep: IO[str],
        params: ResourcesDeploymentScript,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ResourcesDeploymentScriptBicep:
    symbol = "resources_deployment_script_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/resources/deployment-script:{tag}' = {{\n")
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
    output = ResourcesDeploymentScriptBicep(symbol)
    output.outputs = {
            'deploymentScriptLogs': Output(symbol, 'deploymentScriptLogs', 'array'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'outputs': Output(symbol, 'outputs', 'object'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
