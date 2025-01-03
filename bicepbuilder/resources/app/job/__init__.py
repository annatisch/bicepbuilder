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


class Env(TypedDict, total=False):
    """The environment variables to set in the container."""
    name: Required[str]
    """The environment variable name."""
    secretRef: str
    """The name of the Container App secret from which to pull the envrionment variable value. Required if """
    value: str
    """The environment variable value. Required if """


class HttpHeader(TypedDict, total=False):
    """Custom headers to set in the request."""
    name: Required[str]
    """The header field name."""
    value: Required[str]
    """The header field value."""


class HttpGet(TypedDict, total=False):
    """HTTPGet specifies the http request to perform."""
    path: Required[str]
    """Path to access on the HTTP server."""
    port: Required[int]
    """Name of the port to access on the container. If not specified, the containerPort is used."""
    host: str
    """Host name to connect to, defaults to the pod IP."""
    httpHeaders: List['HttpHeader']
    """Custom headers to set in the request."""
    scheme: Literal['HTTP', 'HTTPS']
    """Scheme to use for connecting to the host. Defaults to HTTP."""


class TcpSocket(TypedDict, total=False):
    """TCPSocket specifies an action involving a TCP port."""
    host: Required[str]
    """Host name to connect to, defaults to the pod IP."""
    port: Required[int]
    """Name of the port to access on the container. If not specified, the containerPort is used."""


class Probe(TypedDict, total=False):
    """The probes of the container."""
    type: Required[Literal['Liveness', 'Readiness', 'Startup']]
    """The type of probe."""
    failureThreshold: int
    """Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3."""
    httpGet: 'HttpGet'
    """HTTPGet specifies the http request to perform."""
    initialDelaySeconds: int
    """Number of seconds after the container has started before liveness probes are initiated. Defaults to 0 seconds."""
    periodSeconds: int
    """How often (in seconds) to perform the probe. Defaults to 10 seconds."""
    successThreshold: int
    """Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1."""
    tcpSocket: 'TcpSocket'
    """TCPSocket specifies an action involving a TCP port."""
    terminationGracePeriodSeconds: int
    """Duration in seconds the pod needs to terminate gracefully upon probe failure. This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate."""
    timeoutSeconds: int
    """Number of seconds after which the probe times out. Defaults to 1 second."""


class Resource(TypedDict, total=False):
    """The resources to allocate to the container."""
    cpu: Required[str]
    """The CPU limit of the container in cores."""
    memory: Required[str]
    """The required memory."""


class VolumeMount(TypedDict, total=False):
    """The volume mounts to attach to the container."""
    mountPath: Required[str]
    """The path within the container at which the volume should be mounted. Must not contain ':'."""
    volumeName: Required[str]
    """This must match the Name of a Volume."""
    subPath: str
    """Path within the volume from which the container's volume should be mounted."""


class Container(TypedDict, total=False):
    """List of container definitions for the Container App."""
    image: Required[str]
    """The image of the container."""
    name: Required[str]
    """The name of the container."""
    args: List[object]
    """Container start command arguments."""
    command: List[object]
    """The command to run in the container."""
    env: List['Env']
    """The environment variables to set in the container."""
    probes: List['Probe']
    """The probes of the container."""
    resources: 'Resource'
    """The resources to allocate to the container."""
    volumeMounts: List['VolumeMount']
    """The volume mounts to attach to the container."""


class Auth(TypedDict, total=False):
    """Authentication secrets for the scale rule."""
    secretRef: Required[str]
    """Name of the secret from which to pull the auth params."""
    triggerParameter: Required[str]
    """Trigger Parameter that uses the secret."""


class Rule(TypedDict, total=False):
    """Scaling rules for the job."""
    metadata: Required[Dict[str, object]]
    """Metadata properties to describe the scale rule."""
    name: Required[str]
    """The name of the scale rule."""
    type: Required[str]
    """The type of the rule."""
    auth: List['Auth']
    """Authentication secrets for the scale rule."""


class Scale(TypedDict, total=False):
    """Scaling configurations for event driven jobs."""
    rules: Required[List['Rule']]
    """Scaling rules for the job."""
    maxExecutions: int
    """Maximum number of job executions that are created for a trigger, default 100."""
    minExecutions: int
    """Minimum number of job executions that are created for a trigger, default 0."""
    pollingInterval: int
    """Interval to check each event source in seconds. Defaults to 30s."""


class EventTriggerConfig(TypedDict, total=False):
    """Configuration of an event driven job. Required if """
    scale: Required['Scale']
    """Scaling configurations for event driven jobs."""
    parallelism: int
    """Number of parallel replicas of a job that can run at a given time. Defaults to 1."""
    replicaCompletionCount: int
    """Minimum number of successful replica completions before overall job completion. Must be equal or or less than the parallelism. Defaults to 1."""


class ManualTriggerConfig(TypedDict, total=False):
    """Configuration of a manually triggered job. Required if """
    parallelism: int
    """Number of parallel replicas of a job that can run at a given time. Defaults to 1."""
    replicaCompletionCount: int
    """Minimum number of successful replica completions before overall job completion. Must be equal or or less than the parallelism. Defaults to 1."""


class ScheduleTriggerConfig(TypedDict, total=False):
    """Configuration of a schedule based job. Required if """
    cronExpression: Required[str]
    """Cron formatted repeating schedule ("* * * * *") of a Cron Job. It supports the standard """
    parallelism: int
    """Number of parallel replicas of a job that can run at a given time. Defaults to 1."""
    replicaCompletionCount: int
    """Number of successful completions of a job that are necessary to consider the job complete. Must be equal or or less than the parallelism. Defaults to 1."""


class Env(TypedDict, total=False):
    """The environment variables to set in the container."""
    name: Required[str]
    """The environment variable name."""
    secretRef: str
    """The name of the Container App secret from which to pull the envrionment variable value. Required if """
    value: str
    """The environment variable value. Required if """


class Resource(TypedDict, total=False):
    """Container resource requirements."""
    cpu: Required[str]
    """The CPU limit of the container in cores."""
    memory: Required[str]
    """The required memory."""


class VolumeMount(TypedDict, total=False):
    """The volume mounts to attach to the container."""
    mountPath: Required[str]
    """The path within the container at which the volume should be mounted. Must not contain ':'."""
    volumeName: Required[str]
    """This must match the Name of a Volume."""
    subPath: str
    """Path within the volume from which the container's volume should be mounted."""


class InitContainer(TypedDict, total=False):
    """List of specialized containers that run before app containers."""
    args: Required[List[object]]
    """Container start command arguments."""
    command: Required[List[object]]
    """Container start command."""
    image: Required[str]
    """The image of the container."""
    name: Required[str]
    """The name of the container."""
    env: List['Env']
    """The environment variables to set in the container."""
    resources: 'Resource'
    """Container resource requirements."""
    volumeMounts: List['VolumeMount']
    """The volume mounts to attach to the container."""


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


class Registry(TypedDict, total=False):
    """Collection of private container registry credentials for containers used by the Container app."""
    server: Required[str]
    """The FQDN name of the container registry."""
    passwordSecretRef: str
    """The name of the secret contains the login password. Required if """
    identity: str
    """The resource ID of the (user) managed identity, which is used to access the Azure Container Registry."""
    username: str
    """The username for the container registry."""


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


class Secret(TypedDict, total=False):
    """The secrets of the Container App."""
    keyVaultUrl: str
    """Azure Key Vault URL pointing to the secret referenced by the Container App Job. Required if """
    value: str
    """The secret value, if not fetched from Key Vault. Required if """
    identity: str
    """Resource ID of a managed identity to authenticate with Azure Key Vault, or System to use a system-assigned identity."""
    name: str
    """The name of the secret."""


class Secret(TypedDict, total=False):
    """List of secrets to be added in volume. If no secrets are provided, all secrets in collection will be added to volume."""
    path: Required[str]
    """Path to project secret to. If no path is provided, path defaults to name of secret listed in secretRef."""
    secretRef: Required[str]
    """Name of the Container App secret from which to pull the secret value."""


class Volume(TypedDict, total=False):
    """List of volume definitions for the Container App."""
    name: Required[str]
    """The name of the volume."""
    storageType: Required[Literal['AzureFile', 'EmptyDir', 'NfsAzureFile', 'Secret']]
    """The container name."""
    mountOptions: str
    """Mount options used while mounting the Azure file share or NFS Azure file share. Must be a comma-separated string. Required if """
    storageName: str
    """The storage account name. Not needed for EmptyDir and Secret. Required if """
    secrets: List['Secret']
    """List of secrets to be added in volume. If no secrets are provided, all secrets in collection will be added to volume."""


class AppJob(TypedDict, total=False):
    """"""
    containers: Required[List['Container']]
    """List of container definitions for the Container App."""
    environmentResourceId: Required[str]
    """Resource ID of Container Apps Environment."""
    name: Required[str]
    """Name of the Container App."""
    triggerType: Required[Literal['Event', 'Manual', 'Schedule']]
    """Trigger type of the job."""
    eventTriggerConfig: 'EventTriggerConfig'
    """Configuration of an event driven job. Required if """
    manualTriggerConfig: 'ManualTriggerConfig'
    """Configuration of a manually triggered job. Required if """
    scheduleTriggerConfig: 'ScheduleTriggerConfig'
    """Configuration of a schedule based job. Required if """
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    initContainers: List['InitContainer']
    """List of specialized containers that run before app containers."""
    location: str
    """Location for all Resources. Defaults to the location of the Resource Group."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    registries: List['Registry']
    """Collection of private container registry credentials for containers used by the Container app."""
    replicaRetryLimit: int
    """The maximum number of times a replica can be retried."""
    replicaTimeout: int
    """Maximum number of seconds a replica is allowed to run."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    secrets: List['Secret']
    """The secrets of the Container App."""
    tags: Dict[str, object]
    """Tags of the resource."""
    volumes: List['Volume']
    """List of volume definitions for the Container App."""
    workloadProfileName: str
    """The name of the workload profile to use. Leave empty to use a consumption based profile."""


class AppJobOutputs(TypedDict, total=False):
    """Outputs for AppJob"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the Container App Job."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Container App Job was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Container App Job."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class AppJobModule(Module):
    outputs: AppJobOutputs


def _app_job(
        bicep: IO[str],
        params: AppJob,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> AppJobModule:
    symbol = "app_job_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/app/job:{tag}' = {{\n")
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
    output = AppJobModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
