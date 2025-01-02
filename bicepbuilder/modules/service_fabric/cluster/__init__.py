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

if TYPE_CHECKING:
    from .application_type import ApplicationType


class Certificate(TypedDict, total=False):
    """The certificate to use for securing the cluster. The certificate provided will be used for node to node security within the cluster, SSL certificate for cluster management endpoint and default admin client. Required if the certificateCommonNames parameter is not used."""
    thumbprint: Required[str]
    """The thumbprint of the primary certificate."""
    thumbprintSecondary: str
    """The thumbprint of the secondary certificate."""
    x509StoreName: Literal['AddressBook', 'AuthRoot', 'CertificateAuthority', 'Disallowed', 'My', 'Root', 'TrustedPeople', 'TrustedPublisher']
    """The local certificate store location."""


class CommonName(TypedDict, total=False):
    """The list of server certificates referenced by common name that are used to secure the cluster."""
    certificateCommonName: Required[str]
    """The common name of the server certificate."""
    certificateIssuerThumbprint: Required[str]
    """The issuer thumbprint of the server certificate."""


class CertificateCommonName(TypedDict, total=False):
    """Describes a list of server certificates referenced by common name that are used to secure the cluster. Required if the certificate parameter is not used."""
    commonNames: Required[List['CommonName']]
    """The list of server certificates referenced by common name that are used to secure the cluster."""
    x509StoreName: Literal['AddressBook', 'AuthRoot', 'CertificateAuthority', 'Disallowed', 'My', 'Root', 'TrustedPeople', 'TrustedPublisher']
    """The local certificate store location."""


class ClientCertificateCommonName(TypedDict, total=False):
    """The list of client certificates referenced by common name that are allowed to manage the cluster. Cannot be used if the clientCertificateThumbprints parameter is used."""
    certificateCommonName: Required[str]
    """The common name of the client certificate."""
    certificateIssuerThumbprint: Required[str]
    """The issuer thumbprint of the client certificate."""
    isAdmin: Required[bool]
    """Indicates if the client certificate has admin access to the cluster. Non admin clients can perform only read only operations on the cluster."""


class ClientCertificateThumbprint(TypedDict, total=False):
    """The list of client certificates referenced by thumbprint that are allowed to manage the cluster. Cannot be used if the clientCertificateCommonNames parameter is used."""
    certificateThumbprint: Required[str]
    """The thumbprint of the client certificate."""
    isAdmin: Required[bool]
    """Indicates if the client certificate has admin access to the cluster. Non admin clients can perform only read only operations on the cluster."""


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


class ServiceFabricCluster(TypedDict, total=False):
    """"""
    managementEndpoint: Required[str]
    """The http management endpoint of the cluster."""
    name: Required[str]
    """Name of the Service Fabric cluster."""
    nodeTypes: Required[List[object]]
    """The list of node types in the cluster."""
    reliabilityLevel: Required[Literal['Bronze', 'Gold', 'None', 'Platinum', 'Silver']]
    """The reliability level sets the replica set size of system services. Learn about ReliabilityLevel (https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-capacity). - None - Run the System services with a target replica set count of 1. This should only be used for test clusters. - Bronze - Run the System services with a target replica set count of 3. This should only be used for test clusters. - Silver - Run the System services with a target replica set count of 5. - Gold - Run the System services with a target replica set count of 7. - Platinum - Run the System services with a target replica set count of 9."""
    certificate: 'Certificate'
    """The certificate to use for securing the cluster. The certificate provided will be used for node to node security within the cluster, SSL certificate for cluster management endpoint and default admin client. Required if the certificateCommonNames parameter is not used."""
    certificateCommonNames: 'CertificateCommonName'
    """Describes a list of server certificates referenced by common name that are used to secure the cluster. Required if the certificate parameter is not used."""
    addOnFeatures: Literal['BackupRestoreService', 'DnsService', 'RepairManager', 'ResourceMonitorService']
    """The list of add-on features to enable in the cluster."""
    applicationTypes: List['ApplicationType']
    """Array of Service Fabric cluster application types."""
    azureActiveDirectory: Dict[str, object]
    """The settings to enable AAD authentication on the cluster."""
    clientCertificateCommonNames: List['ClientCertificateCommonName']
    """The list of client certificates referenced by common name that are allowed to manage the cluster. Cannot be used if the clientCertificateThumbprints parameter is used."""
    clientCertificateThumbprints: List['ClientCertificateThumbprint']
    """The list of client certificates referenced by thumbprint that are allowed to manage the cluster. Cannot be used if the clientCertificateCommonNames parameter is used."""
    clusterCodeVersion: str
    """The Service Fabric runtime version of the cluster. This property can only by set the user when upgradeMode is set to "Manual". To get list of available Service Fabric versions for new clusters use ClusterVersion API. To get the list of available version for existing clusters use availableClusterVersions."""
    diagnosticsStorageAccountConfig: Dict[str, object]
    """The storage account information for storing Service Fabric diagnostic logs."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    eventStoreServiceEnabled: bool
    """Indicates if the event store service is enabled."""
    fabricSettings: List[object]
    """The list of custom fabric settings to configure the cluster."""
    infrastructureServiceManager: bool
    """Indicates if infrastructure service manager is enabled."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maxUnusedVersionsToKeep: int
    """Number of unused versions per application type to keep."""
    notifications: List[object]
    """Indicates a list of notification channels for cluster events."""
    reverseProxyCertificate: Dict[str, object]
    """Describes the certificate details."""
    reverseProxyCertificateCommonNames: Dict[str, object]
    """Describes a list of server certificates referenced by common name that are used to secure the cluster."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    sfZonalUpgradeMode: Literal['Hierarchical', 'Parallel']
    """This property controls the logical grouping of VMs in upgrade domains (UDs). This property cannot be modified if a node type with multiple Availability Zones is already present in the cluster."""
    tags: Dict[str, object]
    """Tags of the resource."""
    upgradeDescription: Dict[str, object]
    """Describes the policy used when upgrading the cluster."""
    upgradeMode: Literal['Automatic', 'Manual']
    """The upgrade mode of the cluster when new Service Fabric runtime version is available."""
    upgradePauseEndTimestampUtc: str
    """Indicates the end date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC)."""
    upgradePauseStartTimestampUtc: str
    """Indicates the start date and time to pause automatic runtime version upgrades on the cluster for an specific period of time on the cluster (UTC)."""
    upgradeWave: Literal['Wave0', 'Wave1', 'Wave2']
    """Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0."""
    vmImage: str
    """The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used."""
    vmssZonalUpgradeMode: Literal['Hierarchical', 'Parallel']
    """This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a node type with multiple Availability Zones is added."""
    waveUpgradePaused: bool
    """Boolean to pause automatic runtime version upgrades to the cluster."""


class ServiceFabricClusterOutputs(TypedDict, total=False):
    """Outputs for ServiceFabricCluster"""
    endpoint: Output[Literal['string']]
    """The Service Fabric Cluster endpoint."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The Service Fabric Cluster name."""
    resourceGroupName: Output[Literal['string']]
    """The Service Fabric Cluster resource group."""
    resourceId: Output[Literal['string']]
    """The Service Fabric Cluster resource ID."""


class ServiceFabricClusterBicep(Module):
    outputs: ServiceFabricClusterOutputs


def service_fabric_cluster(
        bicep: IO[str],
        params: ServiceFabricCluster,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ServiceFabricClusterBicep:
    symbol = "service_fabric_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/service-fabric/cluster:{tag}' = {{\n")
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
    output = ServiceFabricClusterBicep(symbol)
    output.outputs = {
            'endpoint': Output(symbol, 'endpoint', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
