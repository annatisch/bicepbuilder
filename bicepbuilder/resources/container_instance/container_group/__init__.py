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


class Gpu(TypedDict, total=False):
    """The GPU request of this container instance."""
    count: Required[int]
    """The count of the GPU resource."""
    sku: Required[Literal['K80', 'P100', 'V100']]
    """The SKU of the GPU resource."""


class Request(TypedDict, total=False):
    """The resource requests of this container instance."""
    cpu: Required[int]
    """The CPU request of this container instance."""
    gpu: 'Gpu'
    """The GPU request of this container instance."""
    memoryInGB: str
    """The memory request in GB of this container instance."""


class Gpu(TypedDict, total=False):
    """The GPU limit of this container instance."""
    count: Required[int]
    """The count of the GPU resource."""
    sku: Required[Literal['K80', 'P100', 'V100']]
    """The SKU of the GPU resource."""


class Limit(TypedDict, total=False):
    """The resource limits of this container instance."""
    cpu: Required[int]
    """The CPU limit of this container instance."""
    gpu: 'Gpu'
    """The GPU limit of this container instance."""
    memoryInGB: str
    """The memory limit in GB of this container instance."""


class Capability(TypedDict, total=False):
    """The capabilities to add or drop for the container."""
    add: List[object]
    """The list of capabilities to add."""
    drop: List[object]
    """The list of capabilities to drop."""


class SecurityContext(TypedDict, total=False):
    """The security context of the container instance."""
    allowPrivilegeEscalation: bool
    """Whether privilege escalation is allowed for the container."""
    capabilities: 'Capability'
    """The capabilities to add or drop for the container."""
    privileged: bool
    """Whether the container is run in privileged mode."""
    runAsGroup: int
    """The GID to run the container as."""
    runAsUser: int
    """The UID to run the container as."""
    seccompProfile: str
    """The seccomp profile to use for the container."""


class Resource(TypedDict, total=False):
    """The resource requirements of the container instance."""
    requests: Required['Request']
    """The resource requests of this container instance."""
    limits: 'Limit'
    """The resource limits of this container instance."""
    securityContext: 'SecurityContext'
    """The security context of the container instance."""


class EnvironmentVariable(TypedDict, total=False):
    """The environment variables to set in the container instance."""
    name: Required[str]
    """The name of the environment variable."""
    secureValue: str
    """The value of the secure environment variable."""
    value: str
    """The value of the environment variable."""


class Port(TypedDict, total=False):
    """The exposed ports on the container instance."""
    port: Required[int]
    """The port number exposed on the container instance."""
    protocol: Required[str]
    """The protocol associated with the port number."""


class VolumeMount(TypedDict, total=False):
    """The volume mounts within the container instance."""
    mountPath: Required[str]
    """The path within the container where the volume should be mounted. Must not contain colon (:)."""
    name: Required[str]
    """The name of the volume mount."""
    readOnly: bool
    """The flag indicating whether the volume mount is read-only."""


class ContainerProperties(TypedDict, total=False):
    """The properties of the container instance."""
    image: Required[str]
    """The name of the container source image."""
    resources: Required['Resource']
    """The resource requirements of the container instance."""
    command: List[object]
    """The command to execute within the container instance."""
    environmentVariables: List['EnvironmentVariable']
    """The environment variables to set in the container instance."""
    livenessProbe: Dict[str, object]
    """The liveness probe."""
    ports: List['Port']
    """The exposed ports on the container instance."""
    volumeMounts: List['VolumeMount']
    """The volume mounts within the container instance."""


class Container(TypedDict, total=False):
    """The containers and their respective config within the container group."""
    name: Required[str]
    """The name of the container instance."""
    properties: Required['ContainerProperties']
    """The properties of the container instance."""


class IpAddressPort(TypedDict, total=False):
    """Ports to open on the public IP address. Must include all ports assigned on container level. Required if """
    port: Required[int]
    """The port number exposed on the container instance."""
    protocol: Required[str]
    """The protocol associated with the port number."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    autoRotationEnabled: bool
    """Enable or disable auto-rotating to the latest key version. Default is """
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, using version as per 'autoRotationEnabled' setting."""
    userAssignedIdentityResourceId: str
    """User assigned identity to use when fetching the customer managed key. Required if no system assigned identity is available for use."""


class ImageRegistryCredential(TypedDict, total=False):
    """The image registry credentials by which the container group is created from."""
    server: Required[str]
    """The Docker image registry server without a protocol such as "http" and "https"."""
    identity: str
    """The identity for the private registry."""
    identityUrl: str
    """The identity URL for the private registry."""
    password: str
    """The password for the private registry."""
    username: str
    """The username for the private registry."""


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
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class ContainerInstanceContainerGroup(TypedDict, total=False):
    """"""
    containers: Required[List['Container']]
    """The containers and their respective config within the container group."""
    name: Required[str]
    """Name for the container group."""
    ipAddressPorts: List['IpAddressPort']
    """Ports to open on the public IP address. Must include all ports assigned on container level. Required if """
    autoGeneratedDomainNameLabelScope: Literal['Noreuse', 'ResourceGroupReuse', 'SubscriptionReuse', 'TenantReuse', 'Unsecure']
    """Specify level of protection of the domain name label."""
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition."""
    dnsNameLabel: str
    """The Dns name label for the resource."""
    dnsNameServers: List[object]
    """List of dns servers used by the containers for lookups."""
    dnsSearchDomains: str
    """DNS search domain which will be appended to each DNS lookup."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    imageRegistryCredentials: List['ImageRegistryCredential']
    """The image registry credentials by which the container group is created from."""
    initContainers: List[object]
    """A list of container definitions which will be executed before the application container starts."""
    ipAddressType: Literal['Private', 'Public']
    """Specifies if the IP is exposed to the public internet or private VNET. - Public or Private."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    osType: str
    """The operating system type required by the containers in the container group. - Windows or Linux."""
    restartPolicy: Literal['Always', 'Never', 'OnFailure']
    """Restart policy for all containers within the container group. - Always: Always restart. OnFailure: Restart on failure. Never: Never restart. - Always, OnFailure, Never."""
    sku: Literal['Dedicated', 'Standard']
    """The container group SKU."""
    subnetResourceId: str
    """Resource ID of the subnet. Only specify when ipAddressType is Private."""
    tags: Dict[str, object]
    """Tags of the resource."""
    volumes: List[object]
    """Specify if volumes (emptyDir, AzureFileShare or GitRepo) shall be attached to your containergroup."""


class ContainerInstanceContainerGroupOutputs(TypedDict, total=False):
    """Outputs for ContainerInstanceContainerGroup"""
    iPv4Address: Output[Literal['string']]
    """The IPv4 address of the container group."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the container group."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the container group was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the container group."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class ContainerInstanceContainerGroupModule(Module):
    outputs: ContainerInstanceContainerGroupOutputs


def _container_instance_container_group(
        bicep: IO[str],
        params: ContainerInstanceContainerGroup,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ContainerInstanceContainerGroupModule:
    symbol = "container_instance_container_group_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/container-instance/container-group:{tag}' = {{\n")
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
    output = ContainerInstanceContainerGroupModule(symbol)
    output.outputs = {
            'iPv4Address': Output(symbol, 'iPv4Address', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
