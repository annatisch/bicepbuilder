from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class RestoredLog(TypedDict, total=False):
    """Restore parameters."""
    endRestoreTime: str
    """The timestamp to end the restore by (UTC)."""
    sourceTable: str
    """The table to restore data from."""
    startRestoreTime: str
    """The timestamp to start the restore from (UTC)."""


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


class Schema(TypedDict, total=False):
    """Table's schema."""
    name: Required[str]
    """The table name."""
    description: str
    """The table description."""
    displayName: str
    """The table display name."""


class Column(TypedDict, total=False):
    """A list of table custom columns."""
    name: Required[str]
    """The column name."""
    type: Required[Literal['boolean', 'dateTime', 'dynamic', 'guid', 'int', 'long', 'real', 'string']]
    """The column type."""
    dataTypeHint: Literal['armPath', 'guid', 'ip', 'uri']
    """The column data type logical hint."""
    description: str
    """The column description."""
    displayName: str
    """Column display name."""


class SearchResult(TypedDict, total=False):
    """Parameters of the search job that initiated this table."""
    query: Required[str]
    """The search job query."""
    description: str
    """The search description."""
    endSearchTime: str
    """The timestamp to end the search by (UTC)."""
    limit: int
    """Limit the search job to return up to specified number of rows."""
    startSearchTime: str
    """The timestamp to start the search from (UTC)."""


class Table(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the table."""
    plan: Literal['Analytics', 'Basic']
    """Instruct the system how to handle and charge the logs ingested to this table."""
    retentionInDays: int
    """The table retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention."""
    totalRetentionInDays: int
    """The table total retention in days, between 4 and 2555. Setting this property to -1 will default to table retention."""


class TableOutputs(TypedDict, total=False):
    """Outputs for Table"""
    name: Output[Literal['string']]
    """The name of the table."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the table was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the table."""


class TableBicep(Module):
    outputs: TableOutputs

