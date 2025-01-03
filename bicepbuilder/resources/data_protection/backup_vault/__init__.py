from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .backup_policy import BackupPolicy


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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Backup Contributor', 'Backup Operator', 'Backup Reader', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class DataProtectionBackupVault(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Backup Vault."""
    azureMonitorAlertSettingsAlertsForAllJobFailures: Literal['Disabled', 'Enabled']
    """Settings for Azure Monitor based alerts for job failures."""
    backupPolicies: List['BackupPolicy']
    """List of all backup policies."""
    dataStoreType: Literal['ArchiveStore', 'OperationalStore', 'VaultStore']
    """The datastore type to use. ArchiveStore does not support ZoneRedundancy."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    featureSettings: Dict[str, object]
    """Feature settings for the backup vault."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    securitySettings: Dict[str, object]
    """Security settings for the backup vault."""
    tags: Dict[str, object]
    """Tags of the Recovery Service Vault resource."""
    type: Literal['GeoRedundant', 'LocallyRedundant', 'ZoneRedundant']
    """The vault redundancy level to use."""


class DataProtectionBackupVaultOutputs(TypedDict, total=False):
    """Outputs for DataProtectionBackupVault"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The Name of the backup vault."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the recovery services vault was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the backup vault."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class DataProtectionBackupVaultModule(Module):
    outputs: DataProtectionBackupVaultOutputs

