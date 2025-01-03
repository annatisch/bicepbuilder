from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    Deployment,
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    targetResourceId: str
    """A reference to an azure resource from where the dns resource value is taken. Also known as an alias record sets and are only supported for record types A, AAAA and CNAME. A resource ID can be an Azure Traffic Manager, Azure CDN, Front Door, Static Web App, or a resource ID of a record set of the same type in the DNS zone (i.e. A, AAAA or CNAME). Cannot be used in conjuction with the "aRecords" property."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    targetResourceId: str
    """A reference to an azure resource from where the dns resource value is taken. Also known as an alias record sets and are only supported for record types A, AAAA and CNAME. A resource ID can be an Azure Traffic Manager, Azure CDN, Front Door, Static Web App, or a resource ID of a record set of the same type in the DNS zone (i.e. A, AAAA or CNAME). Cannot be used in conjuction with the "aRecords" property."""
    ttl: int
    """The TTL of the record."""


class CaaRecord(TypedDict, total=False):
    """The list of CAA records in the record set."""
    flags: Required[int]
    """The flags for this CAA record as an integer between 0 and 255."""
    tag: Required[str]
    """The tag for this CAA record.."""
    value: Required[str]
    """The value for this CAA record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Caa(TypedDict, total=False):
    """Array of CAA records."""
    name: Required[str]
    """The name of the record."""
    caaRecords: List['CaaRecord']
    """The list of CAA records in the record set."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    targetResourceId: str
    """A reference to an azure resource from where the dns resource value is taken. Also known as an alias record sets and are only supported for record types A, AAAA and CNAME. A resource ID can be an Azure Traffic Manager, Azure CDN, Front Door, Static Web App, or a resource ID of a record set of the same type in the DNS zone (i.e. A, AAAA or CNAME). Cannot be used in conjuction with the "aRecords" property."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class NsRecord(TypedDict, total=False):
    """The list of NS records in the record set."""
    nsdname: Required[str]
    """The name server name for this NS record."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class N(TypedDict, total=False):
    """Array of NS records."""
    name: Required[str]
    """The name of the record."""
    metadata: Dict[str, object]
    """The metadata of the record."""
    nsRecords: List['NsRecord']
    """The list of NS records in the record set."""
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DNS Resolver Contributor', 'DNS Zone Contributor', 'Domain Services Contributor', 'Domain Services Reader', 'Network Contributor', 'Owner', 'Private DNS Zone Contributor', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class NetworkDnsZone(TypedDict, total=False):
    """"""
    name: Required[str]
    """DNS zone name."""
    a: List['A']
    """Array of A records."""
    aaaa: List['Aaaa']
    """Array of AAAA records."""
    caa: List['Caa']
    """Array of CAA records."""
    cname: List['Cname']
    """Array of CNAME records."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """The location of the dnsZone. Should be global."""
    lock: 'Lock'
    """The lock settings of the service."""
    mx: List['Mx']
    """Array of MX records."""
    ns: List['N']
    """Array of NS records."""
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


class NetworkDnsZoneOutputs(TypedDict, total=False):
    """Outputs for NetworkDnsZone"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the DNS zone."""
    nameServers: Output[Literal['array']]
    """The name servers of the DNS zone."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the DNS zone was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the DNS zone."""


class NetworkDnsZoneModule(Module):
    outputs: NetworkDnsZoneOutputs


def _network_dns_zone(
        bicep: IO[str],
        params: NetworkDnsZone,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> NetworkDnsZoneModule:
    symbol = "network_dns_zone_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/network/dns-zone:{tag}' = {{\n")
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
    output = NetworkDnsZoneModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'nameServers': Output(symbol, 'nameServers', 'array'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
