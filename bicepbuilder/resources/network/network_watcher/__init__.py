from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .connection_monitor import ConnectionMonitor
    from .flow_log import FlowLog


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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class NetworkWatcher(TypedDict, total=False):
    """"""
    connectionMonitors: List['ConnectionMonitor']
    """Array that contains the Connection Monitors."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    flowLogs: List['FlowLog']
    """Array that contains the Flow Logs."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    name: str
    """Name of the Network Watcher resource (hidden)."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags of the resource."""


class NetworkWatcherOutputs(TypedDict, total=False):
    """Outputs for NetworkWatcher"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the deployed network watcher."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the network watcher was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed network watcher."""


class NetworkWatcherModule(Module):
    outputs: NetworkWatcherOutputs

