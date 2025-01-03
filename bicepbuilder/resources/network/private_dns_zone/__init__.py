from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ARecord(TypedDict, total=False):
    """The list of A records in the record set."""
    ipv4Address: Required[str]
    """The IPv4 address of this A record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class A(TypedDict, total=False):
    """Array of A records."""
    name: Required[str]
    """The name of the record."""
    aRecords: List['ARecord']
    """The list of A records in the record set."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""


class AaaaRecord(TypedDict, total=False):
    """The list of AAAA records in the record set."""
    ipv6Address: Required[str]
    """The IPv6 address of this AAAA record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Aaaa(TypedDict, total=False):
    """Array of AAAA records."""
    name: Required[str]
    """The name of the record."""
    aaaaRecords: List['AaaaRecord']
    """The list of AAAA records in the record set."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""


class CnameRecord(TypedDict, total=False):
    """The CNAME record in the record set."""
    cname: Required[str]
    """The canonical name of the CNAME record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Cname(TypedDict, total=False):
    """Array of CNAME records."""
    name: Required[str]
    """The name of the record."""
    cnameRecord: 'CnameRecord'
    """The CNAME record in the record set."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class MxRecord(TypedDict, total=False):
    """The list of MX records in the record set."""
    exchange: Required[str]
    """The domain name of the mail host for this MX record."""
    preference: Required[int]
    """The preference value for this MX record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Mx(TypedDict, total=False):
    """Array of MX records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    mxRecords: List['MxRecord']
    """The list of MX records in the record set."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""


class PtrRecord(TypedDict, total=False):
    """The list of PTR records in the record set."""
    ptrdname: Required[str]
    """The PTR target domain name for this PTR record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Ptr(TypedDict, total=False):
    """Array of PTR records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    ptrRecords: List['PtrRecord']
    """The list of PTR records in the record set."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator']]]
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


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class SoaRecord(TypedDict, total=False):
    """The SOA record in the record set."""
    email: Required[str]
    """The email contact for this SOA record."""
    expireTime: Required[int]
    """The expire time for this SOA record."""
    host: Required[str]
    """The domain name of the authoritative name server for this SOA record."""
    minimumTtl: Required[int]
    """The minimum value for this SOA record. By convention this is used to determine the negative caching duration."""
    refreshTime: Required[int]
    """The refresh value for this SOA record."""
    retryTime: Required[int]
    """The retry time for this SOA record."""
    serialNumber: Required[int]
    """The serial number for this SOA record."""


class Soa(TypedDict, total=False):
    """Array of SOA records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    soaRecord: 'SoaRecord'
    """The SOA record in the record set."""
    ttl: int
    """The TTL of the record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class SrvRecord(TypedDict, total=False):
    """The list of SRV records in the record set."""
    port: Required[int]
    """The port value for this SRV record."""
    priority: Required[int]
    """The priority value for this SRV record."""
    target: Required[str]
    """The target domain name for this SRV record."""
    weight: Required[int]
    """The weight value for this SRV record."""


class Srv(TypedDict, total=False):
    """Array of SRV records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    srvRecords: List['SrvRecord']
    """The list of SRV records in the record set."""
    ttl: int
    """The TTL of the record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Private DNS Zone Contributor', 'Network Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class TxtRecord(TypedDict, total=False):
    """The list of TXT records in the record set."""
    value: Required[List[object]]
    """The text value of this TXT record."""


class Txt(TypedDict, total=False):
    """Array of TXT records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    ttl: int
    """The TTL of the record."""
    txtRecords: List['TxtRecord']
    """The list of TXT records in the record set."""


class VirtualNetworkLink(TypedDict, total=False):
    """Array of custom objects describing vNet links of the DNS zone. Each object should contain properties 'virtualNetworkResourceId' and 'registrationEnabled'. The 'vnetResourceId' is a resource ID of a vNet to link, 'registrationEnabled' (bool) enables automatic DNS registration in the zone for the linked vNet."""
    virtualNetworkResourceId: Required[str]
    """The resource ID of the virtual network to link."""
    location: str
    """The Azure Region where the resource lives."""
    name: str
    """The resource name."""
    registrationEnabled: bool
    """Is auto-registration of virtual machine records in the virtual network in the Private DNS zone enabled?."""
    resolutionPolicy: Literal['Default', 'NxDomainRedirect']
    """The resolution type of the private-dns-zone fallback machanism."""
    tags: Dict[str, object]
    """Resource tags."""


class NetworkPrivateDnsZone(TypedDict, total=False):
    """"""
    name: Required[str]
    """Private DNS zone name."""
    a: List['A']
    """Array of A records."""
    aaaa: List['Aaaa']
    """Array of AAAA records."""
    cname: List['Cname']
    """Array of CNAME records."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """The location of the PrivateDNSZone. Should be global."""
    lock: 'Lock'
    """The lock settings of the service."""
    mx: List['Mx']
    """Array of MX records."""
    ptr: List['Ptr']
    """Array of PTR records."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    soa: List['Soa']
    """Array of SOA records."""
    srv: List['Srv']
    """Array of SRV records."""
    tags: Dict[str, object]
    """Tags of the resource."""
    txt: List['Txt']
    """Array of TXT records."""
    virtualNetworkLinks: List['VirtualNetworkLink']
    """Array of custom objects describing vNet links of the DNS zone. Each object should contain properties 'virtualNetworkResourceId' and 'registrationEnabled'. The 'vnetResourceId' is a resource ID of a vNet to link, 'registrationEnabled' (bool) enables automatic DNS registration in the zone for the linked vNet."""


class NetworkPrivateDnsZoneOutputs(TypedDict, total=False):
    """Outputs for NetworkPrivateDnsZone"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the private DNS zone."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the private DNS zone was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the private DNS zone."""


class NetworkPrivateDnsZoneModule(Module):
    outputs: NetworkPrivateDnsZoneOutputs

