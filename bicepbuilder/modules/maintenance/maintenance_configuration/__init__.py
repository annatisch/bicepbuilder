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


class MaintenanceConfiguration(TypedDict, total=False):
    """"""
    name: Required[str]
    """Maintenance Configuration Name."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    extensionProperties: Dict[str, object]
    """Gets or sets extensionProperties of the maintenanceConfiguration."""
    installPatches: Dict[str, object]
    """Configuration settings for VM guest patching with Azure Update Manager."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maintenanceScope: Literal['Extension', 'Host', 'InGuestPatch', 'OSImage', 'SQLDB', 'SQLManagedInstance']
    """Gets or sets maintenanceScope of the configuration."""
    maintenanceWindow: Dict[str, object]
    """Definition of a MaintenanceWindow."""
    namespace: str
    """Gets or sets namespace of the resource."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'Scheduled Patching Contributor', 'User Access Administrator']]]
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Gets or sets tags of the resource."""
    visibility: Literal['', 'Custom', 'Public']
    """Gets or sets the visibility of the configuration. The default value is 'Custom'."""


class MaintenanceConfigurationOutputs(TypedDict, total=False):
    """Outputs for MaintenanceConfiguration"""
    location: Output[Literal['string']]
    """The location the Maintenance Configuration was created in."""
    name: Output[Literal['string']]
    """The name of the Maintenance Configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Maintenance Configuration was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Maintenance Configuration."""


class MaintenanceConfigurationBicep(Module):
    outputs: MaintenanceConfigurationOutputs


def maintenance_configuration(
        bicep: IO[str],
        params: MaintenanceConfiguration,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> MaintenanceConfigurationBicep:
    symbol = "maintenance_configuration_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/maintenance/maintenance-configuration:{tag}' = {{\n")
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
    output = MaintenanceConfigurationBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output