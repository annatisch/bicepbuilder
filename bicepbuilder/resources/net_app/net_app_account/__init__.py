from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .capacity_pool import CapacityPool


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, the deployment will use the latest version available at deployment time."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


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


class NetAppAccount(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the NetApp account."""
    adName: str
    """Name of the active directory host as part of Kerberos Realm used for Kerberos authentication."""
    aesEncryption: bool
    """Enable AES encryption on the SMB Server."""
    capacityPools: List['CapacityPool']
    """Capacity pools to create."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition."""
    dnsServers: str
    """Required if domainName is specified. Comma separated list of DNS server IP addresses (IPv4 only) required for the Active Directory (AD) domain join and SMB authentication operations to succeed."""
    domainJoinOU: str
    """Used only if domainName is specified. LDAP Path for the Organization Unit (OU) where SMB Server machine accounts will be created (i.e. 'OU=SecondLevel,OU=FirstLevel')."""
    domainJoinPassword: str
    """Required if domainName is specified. Password of the user specified in domainJoinUser parameter."""
    domainJoinUser: str
    """Required if domainName is specified. Username of Active Directory domain administrator, with permissions to create SMB server machine account in the AD domain."""
    domainName: str
    """Fully Qualified Active Directory DNS Domain Name (e.g. 'contoso.com')."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptDCConnections: bool
    """Specifies whether encryption should be used for communication between SMB server and domain controller (DC). SMB3 only."""
    kdcIP: str
    """Kerberos Key Distribution Center (KDC) as part of Kerberos Realm used for Kerberos authentication."""
    ldapOverTLS: bool
    """Specifies whether to use TLS when NFS (with/without Kerberos) and SMB volumes communicate with an LDAP server. A server root CA certificate must be uploaded if enabled (serverRootCACertificate)."""
    ldapSigning: bool
    """Specifies whether or not the LDAP traffic needs to be signed."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    serverRootCACertificate: str
    """A server Root certificate is required of ldapOverTLS is enabled."""
    smbServerNamePrefix: str
    """Required if domainName is specified. NetBIOS name of the SMB server. A computer account with this prefix will be registered in the AD and used to mount volumes."""
    tags: Dict[str, object]
    """Tags for all resources."""


class NetAppAccountOutputs(TypedDict, total=False):
    """Outputs for NetAppAccount"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the NetApp account."""
    resourceGroupName: Output[Literal['string']]
    """The name of the Resource Group the NetApp account was created in."""
    resourceId: Output[Literal['string']]
    """The Resource ID of the NetApp account."""
    volumeResourceId: Output[Literal['string']]
    """The resource IDs of the volume created in the capacity pool."""


class NetAppAccountModule(Module):
    outputs: NetAppAccountOutputs

