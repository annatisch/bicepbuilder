from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'Scheduled Patching Contributor', 'User Access Administrator']]]
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
    roleAssignments: List['RoleAssignment']
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


class MaintenanceConfigurationModule(Module):
    outputs: MaintenanceConfigurationOutputs

