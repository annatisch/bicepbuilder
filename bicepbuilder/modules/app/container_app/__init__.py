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


class Env(TypedDict, total=False):
    """Container environment variables."""
    name: Required[str]
    """Environment variable name."""
    secretRef: str
    """Name of the Container App secret from which to pull the environment variable value."""
    value: str
    """Non-secret environment variable value."""


class HttpHeader(TypedDict, total=False):
    """HTTP headers to set in the request."""
    name: Required[str]
    """Name of the header."""
    value: Required[str]
    """Value of the header."""


class HttpGet(TypedDict, total=False):
    """HTTPGet specifies the http request to perform."""
    path: Required[str]
    """Path to access on the HTTP server."""
    port: Required[int]
    """Name or number of the port to access on the container."""
    host: str
    """Host name to connect to. Defaults to the pod IP."""
    httpHeaders: List['HttpHeader']
    """HTTP headers to set in the request."""
    scheme: Literal['HTTP', 'HTTPS']
    """Scheme to use for connecting to the host. Defaults to HTTP."""


class TcpSocket(TypedDict, total=False):
    """TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported."""
    port: Required[int]
    """Number of the port to access on the container. Name must be an IANA_SVC_NAME."""
    host: str
    """Host name to connect to, defaults to the pod IP."""


class Probe(TypedDict, total=False):
    """List of probes for the container."""
    failureThreshold: int
    """Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3."""
    httpGet: 'HttpGet'
    """HTTPGet specifies the http request to perform."""
    initialDelaySeconds: int
    """Number of seconds after the container has started before liveness probes are initiated."""
    periodSeconds: int
    """How often (in seconds) to perform the probe. Default to 10 seconds."""
    successThreshold: int
    """Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup."""
    tcpSocket: 'TcpSocket'
    """TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported."""
    terminationGracePeriodSeconds: int
    """Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate. Maximum value is 3600 seconds (1 hour)."""
    timeoutSeconds: int
    """Number of seconds after which the probe times out. Defaults to 1 second."""
    type: Literal['Liveness', 'Readiness', 'Startup']
    """The type of probe."""


class VolumeMount(TypedDict, total=False):
    """Container volume mounts."""
    mountPath: Required[str]
    """Path within the container at which the volume should be mounted.Must not contain ':'."""
    volumeName: Required[str]
    """This must match the Name of a Volume."""
    subPath: str
    """Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root)."""


class Container(TypedDict, total=False):
    """List of container definitions for the Container App."""
    image: Required[str]
    """Container image tag."""
    resources: Required[Dict[str, object]]
    """Container resource requirements."""
    args: List[object]
    """Container start command arguments."""
    command: List[object]
    """Container start command."""
    env: List['Env']
    """Container environment variables."""
    name: str
    """Custom container name."""
    probes: List['Probe']
    """List of probes for the container."""
    volumeMounts: List['VolumeMount']
    """Container volume mounts."""


class AdditionalPortMapping(TypedDict, total=False):
    """Settings to expose additional ports on container app."""
    external: Required[bool]
    """Specifies whether the app port is accessible outside of the environment."""
    targetPort: Required[int]
    """Specifies the port the container listens on."""
    exposedPort: int
    """Specifies the exposed port for the target port. If not specified, it defaults to target port."""


class CorsPolicy(TypedDict, total=False):
    """Object userd to configure CORS policy."""
    allowCredentials: bool
    """Switch to determine whether the resource allows credentials."""
    allowedHeaders: List[object]
    """Specifies the content for the access-control-allow-headers header."""
    allowedMethods: List[object]
    """Specifies the content for the access-control-allow-methods header."""
    allowedOrigins: List[object]
    """Specifies the content for the access-control-allow-origins header."""
    exposeHeaders: List[object]
    """Specifies the content for the access-control-expose-headers header."""
    maxAge: int
    """Specifies the content for the access-control-max-age header."""


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
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['ContainerApp Reader', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class ServiceBind(TypedDict, total=False):
    """List of container app services bound to the app."""
    name: Required[str]
    """The name of the service."""
    serviceId: Required[str]
    """The service ID."""


class AppContainerApp(TypedDict, total=False):
    """"""
    containers: Required[List['Container']]
    """List of container definitions for the Container App."""
    environmentResourceId: Required[str]
    """Resource ID of environment."""
    name: Required[str]
    """Name of the Container App."""
    activeRevisionsMode: Literal['Multiple', 'Single']
    """Controls how active revisions are handled for the Container app."""
    additionalPortMappings: List['AdditionalPortMapping']
    """Settings to expose additional ports on container app."""
    clientCertificateMode: Literal['accept', 'ignore', 'require']
    """Client certificate mode for mTLS."""
    corsPolicy: 'CorsPolicy'
    """Object userd to configure CORS policy."""
    customDomains: List[object]
    """Custom domain bindings for Container App hostnames."""
    dapr: Dict[str, object]
    """Dapr configuration for the Container App."""
    disableIngress: bool
    """Bool to disable all ingress traffic for the container app."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    exposedPort: int
    """Exposed Port in containers for TCP traffic from ingress."""
    includeAddOns: bool
    """Toggle to include the service configuration."""
    ingressAllowInsecure: bool
    """Bool indicating if HTTP connections to is allowed. If set to false HTTP connections are automatically redirected to HTTPS connections."""
    ingressExternal: bool
    """Bool indicating if the App exposes an external HTTP endpoint."""
    ingressTargetPort: int
    """Target Port in containers for traffic from ingress."""
    ingressTransport: Literal['auto', 'http', 'http2', 'tcp']
    """Ingress transport protocol."""
    initContainersTemplate: List[object]
    """List of specialized containers that run before app containers."""
    ipSecurityRestrictions: List[object]
    """Rules to restrict incoming IP address."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    maxInactiveRevisions: int
    """Max inactive revisions a Container App can have."""
    registries: List[object]
    """Collection of private container registry credentials for containers used by the Container app."""
    revisionSuffix: str
    """User friendly suffix that is appended to the revision name."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    scaleMaxReplicas: int
    """Maximum number of container replicas. Defaults to 10 if not set."""
    scaleMinReplicas: int
    """Minimum number of container replicas. Defaults to 3 if not set."""
    scaleRules: List[object]
    """Scaling rules."""
    secrets: Dict[str, object]
    """The secrets of the Container App."""
    service: Dict[str, object]
    """Dev ContainerApp service type."""
    serviceBinds: List['ServiceBind']
    """List of container app services bound to the app."""
    stickySessionsAffinity: Literal['none', 'sticky']
    """Bool indicating if the Container App should enable session affinity."""
    tags: Dict[str, object]
    """Tags of the resource."""
    trafficLabel: str
    """Associates a traffic label with a revision. Label name should be consist of lower case alphanumeric characters or dashes."""
    trafficLatestRevision: bool
    """Indicates that the traffic weight belongs to a latest stable revision."""
    trafficRevisionName: str
    """Name of a revision."""
    trafficWeight: int
    """Traffic weight assigned to a revision."""
    volumes: List[object]
    """List of volume definitions for the Container App."""
    workloadProfileName: str
    """Workload profile name to pin for container app execution."""


class AppContainerAppOutputs(TypedDict, total=False):
    """Outputs for AppContainerApp"""
    fqdn: Output[Literal['string']]
    """The configuration of ingress fqdn."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Container App."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Container App was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Container App."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class AppContainerAppBicep(Module):
    outputs: AppContainerAppOutputs


def app_container_app(
        bicep: IO[str],
        params: AppContainerApp,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.11.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AppContainerAppBicep:
    symbol = "app_container_app_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/container-app:{tag}' = {{\n")
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
    output = AppContainerAppBicep(symbol)
    output.outputs = {
            'fqdn': Output(symbol, 'fqdn', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
