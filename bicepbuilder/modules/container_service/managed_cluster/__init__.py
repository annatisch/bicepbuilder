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


class PrimaryAgentPoolProfile(TypedDict, total=False):
    """Properties of the primary agent pool."""
    name: Required[str]
    """The name of the agent pool."""
    availabilityZones: List[object]
    """The availability zones of the agent pool."""
    count: int
    """The number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    enableAutoScaling: bool
    """Whether to enable auto-scaling for the agent pool."""
    enableDefaultTelemetry: bool
    """The enable default telemetry of the agent pool."""
    enableEncryptionAtHost: bool
    """Whether to enable encryption at host for the agent pool."""
    enableFIPS: bool
    """Whether to enable FIPS for the agent pool."""
    enableNodePublicIP: bool
    """Whether to enable node public IP for the agent pool."""
    enableUltraSSD: bool
    """Whether to enable Ultra SSD for the agent pool."""
    gpuInstanceProfile: Literal['MIG1g', 'MIG2g', 'MIG3g', 'MIG4g', 'MIG7g']
    """The GPU instance profile of the agent pool."""
    kubeletDiskType: str
    """The kubelet disk type of the agent pool."""
    maxCount: int
    """The maximum number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    maxPods: int
    """The maximum number of pods that can run on a node."""
    maxSurge: str
    """The maximum number of nodes that can be created during an upgrade."""
    minCount: int
    """The minimum number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    minPods: int
    """The minimum number of pods that can run on a node."""
    mode: Literal['System', 'User']
    """The mode of the agent pool."""
    nodeLabels: Dict[str, object]
    """The node labels of the agent pool."""
    nodePublicIpPrefixResourceId: str
    """The node public IP prefix ID of the agent pool."""
    nodeTaints: List[object]
    """The node taints of the agent pool."""
    orchestratorVersion: str
    """The Kubernetes version of the agent pool."""
    osDiskSizeGB: int
    """The OS disk size in GB of the agent pool."""
    osDiskType: str
    """The OS disk type of the agent pool."""
    osSku: str
    """The OS SKU of the agent pool."""
    osType: Literal['Linux', 'Windows']
    """The OS type of the agent pool."""
    podSubnetResourceId: str
    """The pod subnet ID of the agent pool."""
    proximityPlacementGroupResourceId: str
    """The proximity placement group resource ID of the agent pool."""
    scaleDownMode: Literal['Deallocate', 'Delete']
    """The scale down mode of the agent pool."""
    scaleSetEvictionPolicy: Literal['Deallocate', 'Delete']
    """The scale set eviction policy of the agent pool."""
    scaleSetPriority: Literal['Low', 'Regular', 'Spot']
    """The scale set priority of the agent pool."""
    sourceResourceId: str
    """The source resource ID to create the agent pool from."""
    spotMaxPrice: int
    """The spot max price of the agent pool."""
    tags: Dict[str, object]
    """The tags of the agent pool."""
    type: Literal['AvailabilitySet', 'VirtualMachineScaleSets']
    """The type of the agent pool."""
    vmSize: str
    """The VM size of the agent pool."""
    vnetSubnetResourceId: str
    """The VNet subnet ID of the agent pool."""
    workloadRuntime: str
    """The workload runtime of the agent pool."""


class AgentPool(TypedDict, total=False):
    """Define one or more secondary/additional agent pools."""
    name: Required[str]
    """The name of the agent pool."""
    availabilityZones: List[object]
    """The availability zones of the agent pool."""
    count: int
    """The number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    enableAutoScaling: bool
    """Whether to enable auto-scaling for the agent pool."""
    enableDefaultTelemetry: bool
    """The enable default telemetry of the agent pool."""
    enableEncryptionAtHost: bool
    """Whether to enable encryption at host for the agent pool."""
    enableFIPS: bool
    """Whether to enable FIPS for the agent pool."""
    enableNodePublicIP: bool
    """Whether to enable node public IP for the agent pool."""
    enableUltraSSD: bool
    """Whether to enable Ultra SSD for the agent pool."""
    gpuInstanceProfile: Literal['MIG1g', 'MIG2g', 'MIG3g', 'MIG4g', 'MIG7g']
    """The GPU instance profile of the agent pool."""
    kubeletDiskType: str
    """The kubelet disk type of the agent pool."""
    maxCount: int
    """The maximum number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    maxPods: int
    """The maximum number of pods that can run on a node."""
    maxSurge: str
    """The maximum number of nodes that can be created during an upgrade."""
    minCount: int
    """The minimum number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive)."""
    minPods: int
    """The minimum number of pods that can run on a node."""
    mode: Literal['System', 'User']
    """The mode of the agent pool."""
    nodeLabels: Dict[str, object]
    """The node labels of the agent pool."""
    nodePublicIpPrefixResourceId: str
    """The node public IP prefix ID of the agent pool."""
    nodeTaints: List[object]
    """The node taints of the agent pool."""
    orchestratorVersion: str
    """The Kubernetes version of the agent pool."""
    osDiskSizeGB: int
    """The OS disk size in GB of the agent pool."""
    osDiskType: str
    """The OS disk type of the agent pool."""
    osSku: str
    """The OS SKU of the agent pool."""
    osType: Literal['Linux', 'Windows']
    """The OS type of the agent pool."""
    podSubnetResourceId: str
    """The pod subnet ID of the agent pool."""
    proximityPlacementGroupResourceId: str
    """The proximity placement group resource ID of the agent pool."""
    scaleDownMode: Literal['Deallocate', 'Delete']
    """The scale down mode of the agent pool."""
    scaleSetEvictionPolicy: Literal['Deallocate', 'Delete']
    """The scale set eviction policy of the agent pool."""
    scaleSetPriority: Literal['Low', 'Regular', 'Spot']
    """The scale set priority of the agent pool."""
    sourceResourceId: str
    """The source resource ID to create the agent pool from."""
    spotMaxPrice: int
    """The spot max price of the agent pool."""
    tags: Dict[str, object]
    """The tags of the agent pool."""
    type: Literal['AvailabilitySet', 'VirtualMachineScaleSets']
    """The type of the agent pool."""
    vmSize: str
    """The VM size of the agent pool."""
    vnetSubnetResourceId: str
    """The VNet subnet ID of the agent pool."""
    workloadRuntime: str
    """The workload runtime of the agent pool."""


class CustomerManagedKey(TypedDict, total=False):
    """The customer managed key definition."""
    keyName: Required[str]
    """The name of the customer managed key to use for encryption."""
    keyVaultNetworkAccess: Required[Literal['Private', 'Public']]
    """Network access of key vault. The possible values are Public and Private. Public means the key vault allows public access from all networks. Private means the key vault disables public access and enables private link. The default value is Public."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a customer managed key for encryption from."""
    keyVersion: str
    """The version of the customer managed key to reference for encryption. If not provided, using 'latest'."""


class LogCategoriesAndGroup(TypedDict, total=False):
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    category: str
    """Name of a Diagnostic Log category for a resource type this setting is applied to. Set the specific logs to collect here."""
    categoryGroup: str
    """Name of a Diagnostic Log category group for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class MetricCategory(TypedDict, total=False):
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    category: Required[str]
    """Name of a Diagnostic Metric category for a resource type this setting is applied to. Set to """
    enabled: bool
    """Enable or disable the category explicitly. Default is """


class DiagnosticSetting(TypedDict, total=False):
    """The diagnostic settings of the service."""
    eventHubAuthorizationRuleResourceId: str
    """Resource ID of the diagnostic event hub authorization rule for the Event Hubs namespace in which the event hub should be created or streamed to."""
    eventHubName: str
    """Name of the diagnostic event hub within the namespace to which logs are streamed. Without this, an event hub is created for each log category. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    logAnalyticsDestinationType: Literal['AzureDiagnostics', 'Dedicated']
    """A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type."""
    logCategoriesAndGroups: List['LogCategoriesAndGroup']
    """The name of logs that will be streamed. "allLogs" includes all possible logs for the resource. Set to """
    marketplacePartnerResourceId: str
    """The full ARM resource ID of the Marketplace resource to which you would like to send Diagnostic Logs."""
    metricCategories: List['MetricCategory']
    """The name of metrics that will be streamed. "allMetrics" includes all possible metrics for the resource. Set to """
    name: str
    """The name of diagnostic setting."""
    storageAccountResourceId: str
    """Resource ID of the diagnostic storage account. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""
    workspaceResourceId: str
    """Resource ID of the diagnostic log analytics workspace. For security reasons, it is recommended to set diagnostic settings to send data to either storage account, log analytics workspace or event hub."""


class ConfigurationProtectedSetting(TypedDict, total=False):
    """The configuration protected settings of the extension."""
    sshPrivateKey: str
    """The SSH private key to use for Git authentication."""


class FluxExtension(TypedDict, total=False):
    """Settings and configurations for the flux extension."""
    configurationProtectedSettings: 'ConfigurationProtectedSetting'
    """The configuration protected settings of the extension."""
    configurations: List[object]
    """The flux configurations of the extension."""
    configurationSettings: Dict[str, object]
    """The configuration settings of the extension."""
    name: str
    """The name of the extension."""
    releaseNamespace: str
    """Namespace where the extension Release must be placed."""
    releaseTrain: str
    """The release train of the extension."""
    targetNamespace: str
    """Namespace where the extension will be created for an Namespace scoped extension."""
    version: str
    """The version of the extension."""


class IstioServiceMeshCertificateAuthority(TypedDict, total=False):
    """The Istio Certificate Authority definition."""
    certChainObjectName: Required[str]
    """The Certificate chain object name in Azure Key Vault."""
    certObjectName: Required[str]
    """The Intermediate certificate object name in Azure Key Vault."""
    keyObjectName: Required[str]
    """The Intermediate certificate private key object name in Azure Key Vault."""
    keyVaultResourceId: Required[str]
    """The resource ID of a key vault to reference a Certificate Authority from."""
    rootCertObjectName: Required[str]
    """Root certificate object name in Azure Key Vault."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class MaintenanceConfiguration(TypedDict, total=False):
    """Whether or not to use AKS Automatic mode."""
    maintenanceWindow: Required[Dict[str, object]]
    """Maintenance window for the maintenance configuration."""
    name: Required[Literal['aksManagedAutoUpgradeSchedule', 'aksManagedNodeOSUpgradeSchedule']]
    """Name of maintenance window."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. Only one type of identity is supported: system-assigned or user-assigned, but not both."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourcesIds: List[object]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Kubernetes Fleet Manager Contributor Role', 'Azure Kubernetes Fleet Manager RBAC Admin', 'Azure Kubernetes Fleet Manager RBAC Cluster Admin', 'Azure Kubernetes Fleet Manager RBAC Reader', 'Azure Kubernetes Fleet Manager RBAC Writer', 'Azure Kubernetes Service Cluster Admin Role', 'Azure Kubernetes Service Cluster Monitoring User', 'Azure Kubernetes Service Cluster User Role', 'Azure Kubernetes Service Contributor Role', 'Azure Kubernetes Service RBAC Admin', 'Azure Kubernetes Service RBAC Cluster Admin', 'Azure Kubernetes Service RBAC Reader', 'Azure Kubernetes Service RBAC Writer', 'Contributor', 'Kubernetes Agentless Operator', 'Owner', 'Reader', 'Role Based Access Control Administrator (Preview)', 'User Access Administrator']]]
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


class ContainerServiceManagedCluster(TypedDict, total=False):
    """"""
    name: Required[str]
    """Specifies the name of the AKS cluster."""
    primaryAgentPoolProfiles: Required[List['PrimaryAgentPoolProfile']]
    """Properties of the primary agent pool."""
    aksServicePrincipalProfile: Dict[str, object]
    """Information about a service principal identity for the cluster to use for manipulating Azure APIs. Required if no managed identities are assigned to the cluster."""
    appGatewayResourceId: str
    """Specifies the resource ID of connected application gateway. Required if """
    aadProfileAdminGroupObjectIDs: List[object]
    """Specifies the AAD group object IDs that will have admin role of the cluster."""
    aadProfileClientAppID: str
    """The client AAD application ID."""
    aadProfileEnableAzureRBAC: bool
    """Specifies whether to enable Azure RBAC for Kubernetes authorization."""
    aadProfileManaged: bool
    """Specifies whether to enable managed AAD integration."""
    aadProfileServerAppID: str
    """The server AAD application ID."""
    aadProfileServerAppSecret: str
    """The server AAD application secret."""
    aadProfileTenantId: str
    """Specifies the tenant ID of the Azure Active Directory used by the AKS cluster for authentication."""
    aciConnectorLinuxEnabled: bool
    """Specifies whether the aciConnectorLinux add-on is enabled or not."""
    adminUsername: str
    """Specifies the administrator username of Linux virtual machines."""
    agentPools: List['AgentPool']
    """Define one or more secondary/additional agent pools."""
    authorizedIPRanges: List[object]
    """IP ranges are specified in CIDR format, e.g. 137.117.106.88/29. This feature is not compatible with clusters that use Public IP Per Node, or clusters that are using a Basic Load Balancer."""
    autoNodeOsUpgradeProfileUpgradeChannel: Literal['NodeImage', 'None', 'SecurityPatch', 'Unmanaged']
    """Auto-upgrade channel on the Node Os."""
    autoScalerProfileBalanceSimilarNodeGroups: bool
    """Specifies the balance of similar node groups for the auto-scaler of the AKS cluster."""
    autoScalerProfileExpander: Literal['least-waste', 'most-pods', 'priority', 'random']
    """Specifies the expand strategy for the auto-scaler of the AKS cluster."""
    autoScalerProfileMaxEmptyBulkDelete: int
    """Specifies the maximum empty bulk delete for the auto-scaler of the AKS cluster."""
    autoScalerProfileMaxGracefulTerminationSec: int
    """Specifies the max graceful termination time interval in seconds for the auto-scaler of the AKS cluster."""
    autoScalerProfileMaxNodeProvisionTime: str
    """Specifies the maximum node provisioning time for the auto-scaler of the AKS cluster. Values must be an integer followed by an "m". No unit of time other than minutes (m) is supported."""
    autoScalerProfileMaxTotalUnreadyPercentage: int
    """Specifies the mximum total unready percentage for the auto-scaler of the AKS cluster. The maximum is 100 and the minimum is 0."""
    autoScalerProfileNewPodScaleUpDelay: str
    """For scenarios like burst/batch scale where you do not want CA to act before the kubernetes scheduler could schedule all the pods, you can tell CA to ignore unscheduled pods before they are a certain age. Values must be an integer followed by a unit ("s" for seconds, "m" for minutes, "h" for hours, etc)."""
    autoScalerProfileOkTotalUnreadyCount: int
    """Specifies the OK total unready count for the auto-scaler of the AKS cluster."""
    autoScalerProfileScaleDownDelayAfterAdd: str
    """Specifies the scale down delay after add of the auto-scaler of the AKS cluster."""
    autoScalerProfileScaleDownDelayAfterDelete: str
    """Specifies the scale down delay after delete of the auto-scaler of the AKS cluster."""
    autoScalerProfileScaleDownDelayAfterFailure: str
    """Specifies scale down delay after failure of the auto-scaler of the AKS cluster."""
    autoScalerProfileScaleDownUnneededTime: str
    """Specifies the scale down unneeded time of the auto-scaler of the AKS cluster."""
    autoScalerProfileScaleDownUnreadyTime: str
    """Specifies the scale down unready time of the auto-scaler of the AKS cluster."""
    autoScalerProfileScanInterval: str
    """Specifies the scan interval of the auto-scaler of the AKS cluster."""
    autoScalerProfileSkipNodesWithLocalStorage: bool
    """Specifies if nodes with local storage should be skipped for the auto-scaler of the AKS cluster."""
    autoScalerProfileSkipNodesWithSystemPods: bool
    """Specifies if nodes with system pods should be skipped for the auto-scaler of the AKS cluster."""
    autoScalerProfileUtilizationThreshold: str
    """Specifies the utilization threshold of the auto-scaler of the AKS cluster."""
    autoUpgradeProfileUpgradeChannel: Literal['node-image', 'none', 'patch', 'rapid', 'stable']
    """Auto-upgrade channel on the AKS cluster."""
    azurePolicyEnabled: bool
    """Specifies whether the azurepolicy add-on is enabled or not. For security reasons, this setting should be enabled."""
    azurePolicyVersion: str
    """Specifies the azure policy version to use."""
    backendPoolType: Literal['NodeIP', 'NodeIPConfiguration']
    """The type of the managed inbound Load Balancer BackendPool."""
    costAnalysisEnabled: bool
    """Specifies whether the cost analysis add-on is enabled or not. If Enabled """
    customerManagedKey: 'CustomerManagedKey'
    """The customer managed key definition."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableCustomMetrics: bool
    """Indicates whether custom metrics collection has to be disabled or not. If not specified the default is false. No custom metrics will be emitted if this field is false but the container insights enabled field is false."""
    disableLocalAccounts: bool
    """If set to true, getting static credentials will be disabled for this cluster. This must only be used on Managed Clusters that are AAD enabled."""
    disablePrometheusMetricsScraping: bool
    """Indicates whether prometheus metrics scraping is disabled or not. If not specified the default is false. No prometheus metrics will be emitted if this field is false but the container insights enabled field is false."""
    disableRunCommand: bool
    """Whether to disable run command for the cluster or not."""
    diskEncryptionSetResourceId: str
    """The resource ID of the disc encryption set to apply to the cluster. For security reasons, this value should be provided."""
    dnsPrefix: str
    """Specifies the DNS prefix specified when creating the managed cluster."""
    dnsServiceIP: str
    """Specifies the IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range specified in serviceCidr."""
    dnsZoneResourceId: str
    """Specifies the resource ID of connected DNS zone. It will be ignored if """
    enableAzureDefender: bool
    """Whether to enable Azure Defender."""
    enableAzureMonitorProfileMetrics: bool
    """Whether the metric state of the kubenetes cluster is enabled."""
    enableContainerInsights: bool
    """Indicates if Azure Monitor Container Insights Logs Addon is enabled."""
    enableDnsZoneContributorRoleAssignment: bool
    """Specifies whether assing the DNS zone contributor role to the cluster service principal. It will be ignored if """
    enableImageCleaner: bool
    """Whether to enable Image Cleaner for Kubernetes."""
    enableKeyvaultSecretsProvider: bool
    """Specifies whether the KeyvaultSecretsProvider add-on is enabled or not."""
    enableOidcIssuerProfile: bool
    """Whether the The OIDC issuer profile of the Managed Cluster is enabled."""
    enablePodSecurityPolicy: bool
    """Whether to enable Kubernetes pod security policy. Requires enabling the pod security policy feature flag on the subscription."""
    enablePrivateCluster: bool
    """Specifies whether to create the cluster as a private cluster or not."""
    enablePrivateClusterPublicFQDN: bool
    """Whether to create additional public FQDN for private cluster or not."""
    enableRBAC: bool
    """Whether to enable Kubernetes Role-Based Access Control."""
    enableSecretRotation: bool
    """Specifies whether the KeyvaultSecretsProvider add-on uses secret rotation."""
    enableStorageProfileBlobCSIDriver: bool
    """Whether the AzureBlob CSI Driver for the storage profile is enabled."""
    enableStorageProfileDiskCSIDriver: bool
    """Whether the AzureDisk CSI Driver for the storage profile is enabled."""
    enableStorageProfileFileCSIDriver: bool
    """Whether the AzureFile CSI Driver for the storage profile is enabled."""
    enableStorageProfileSnapshotController: bool
    """Whether the snapshot controller for the storage profile is enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    enableWorkloadIdentity: bool
    """Whether to enable Workload Identity. Requires OIDC issuer profile to be enabled."""
    fluxExtension: 'FluxExtension'
    """Settings and configurations for the flux extension."""
    httpApplicationRoutingEnabled: bool
    """Specifies whether the httpApplicationRouting add-on is enabled or not."""
    httpProxyConfig: Dict[str, object]
    """Configurations for provisioning the cluster with HTTP proxy servers."""
    identityProfile: Dict[str, object]
    """Identities associated with the cluster."""
    imageCleanerIntervalHours: int
    """The interval in hours Image Cleaner will run. The maximum value is three months."""
    ingressApplicationGatewayEnabled: bool
    """Specifies whether the ingressApplicationGateway (AGIC) add-on is enabled or not."""
    istioServiceMeshCertificateAuthority: 'IstioServiceMeshCertificateAuthority'
    """The Istio Certificate Authority definition."""
    istioServiceMeshEnabled: bool
    """Specifies whether the Istio ServiceMesh add-on is enabled or not."""
    istioServiceMeshExternalIngressGatewayEnabled: bool
    """Specifies whether the External Istio Ingress Gateway is enabled or not."""
    istioServiceMeshInternalIngressGatewayEnabled: bool
    """Specifies whether the Internal Istio Ingress Gateway is enabled or not."""
    istioServiceMeshRevisions: List[object]
    """The list of revisions of the Istio control plane. When an upgrade is not in progress, this holds one value. When canary upgrade is in progress, this can only hold two consecutive values."""
    kedaAddon: bool
    """Enables Kubernetes Event-driven Autoscaling (KEDA)."""
    kubeDashboardEnabled: bool
    """Specifies whether the kubeDashboard add-on is enabled or not."""
    kubernetesVersion: str
    """Version of Kubernetes specified when creating the managed cluster."""
    loadBalancerSku: Literal['basic', 'standard']
    """Specifies the sku of the load balancer used by the virtual machine scale sets used by nodepools."""
    location: str
    """Specifies the location of AKS cluster. It picks up Resource Group's location by default."""
    lock: 'Lock'
    """The lock settings of the service."""
    maintenanceConfigurations: List['MaintenanceConfiguration']
    """Whether or not to use AKS Automatic mode."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. Only one type of identity is supported: system-assigned or user-assigned, but not both."""
    managedOutboundIPCount: int
    """Outbound IP Count for the Load balancer."""
    metricAnnotationsAllowList: str
    """A comma-separated list of Kubernetes cluster metrics annotations."""
    metricLabelsAllowlist: str
    """A comma-separated list of kubernetes cluster metrics labels."""
    monitoringWorkspaceResourceId: str
    """Resource ID of the monitoring log analytics workspace."""
    networkDataplane: Literal['azure', 'cilium']
    """Network dataplane used in the Kubernetes cluster. Not compatible with kubenet network plugin."""
    networkPlugin: Literal['azure', 'kubenet']
    """Specifies the network plugin used for building Kubernetes network."""
    networkPluginMode: Literal['overlay']
    """Network plugin mode used for building the Kubernetes network. Not compatible with kubenet network plugin."""
    networkPolicy: Literal['azure', 'calico', 'cilium']
    """Specifies the network policy used for building Kubernetes network. - calico or azure."""
    nodeProvisioningProfile: Dict[str, object]
    """Node provisioning settings that apply to the whole cluster."""
    nodeResourceGroup: str
    """Name of the resource group containing agent pool nodes."""
    nodeResourceGroupProfile: Dict[str, object]
    """The node resource group configuration profile."""
    omsAgentEnabled: bool
    """Specifies whether the OMS agent is enabled."""
    openServiceMeshEnabled: bool
    """Specifies whether the openServiceMesh add-on is enabled or not."""
    outboundType: Literal['loadBalancer', 'managedNATGateway', 'userAssignedNATGateway', 'userDefinedRouting']
    """Specifies outbound (egress) routing method."""
    podCidr: str
    """Specifies the CIDR notation IP range from which to assign pod IPs when kubenet is used."""
    podIdentityProfileAllowNetworkPluginKubenet: bool
    """Running in Kubenet is disabled by default due to the security related nature of AAD Pod Identity and the risks of IP spoofing."""
    podIdentityProfileEnable: bool
    """Whether the pod identity addon is enabled."""
    podIdentityProfileUserAssignedIdentities: List[object]
    """The pod identities to use in the cluster."""
    podIdentityProfileUserAssignedIdentityExceptions: List[object]
    """The pod identity exceptions to allow."""
    privateDNSZone: str
    """Private DNS Zone configuration. Set to 'system' and AKS will create a private DNS zone in the node resource group. Set to '' to disable private DNS Zone creation and use public DNS. Supply the resource ID here of an existing Private DNS zone to use an existing zone."""
    publicNetworkAccess: Literal['Disabled', 'Enabled', 'SecuredByPerimeter']
    """Allow or deny public network access for AKS."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    serviceCidr: str
    """A CIDR notation IP range from which to assign service cluster IPs. It must not overlap with any Subnet IP ranges."""
    skuName: Literal['Automatic', 'Base']
    """Name of a managed cluster SKU."""
    skuTier: Literal['Free', 'Premium', 'Standard']
    """Tier of a managed cluster SKU."""
    sshPublicKey: str
    """Specifies the SSH RSA public key string for the Linux nodes."""
    supportPlan: Literal['AKSLongTermSupport', 'KubernetesOfficial']
    """The support plan for the Managed Cluster."""
    syslogPort: int
    """The syslog host port. If not specified, the default port is 28330."""
    tags: Dict[str, object]
    """Tags of the resource."""
    vpaAddon: bool
    """Whether to enable VPA add-on in cluster. Default value is false."""
    webApplicationRoutingEnabled: bool
    """Specifies whether the webApplicationRoutingEnabled add-on is enabled or not."""


class ContainerServiceManagedClusterOutputs(TypedDict, total=False):
    """Outputs for ContainerServiceManagedCluster"""
    addonProfiles: Output[Literal['object']]
    """The addonProfiles of the Kubernetes cluster."""
    controlPlaneFQDN: Output[Literal['string']]
    """The control plane FQDN of the managed cluster."""
    ingressApplicationGatewayIdentityObjectId: Output[Literal['string']]
    """The Object ID of Application Gateway Ingress Controller (AGIC) identity."""
    keyvaultIdentityClientId: Output[Literal['string']]
    """The Client ID of the Key Vault Secrets Provider identity."""
    keyvaultIdentityObjectId: Output[Literal['string']]
    """The Object ID of the Key Vault Secrets Provider identity."""
    kubeletIdentityClientId: Output[Literal['string']]
    """The Client ID of the AKS identity."""
    kubeletIdentityObjectId: Output[Literal['string']]
    """The Object ID of the AKS identity."""
    kubeletIdentityResourceId: Output[Literal['string']]
    """The Resource ID of the AKS identity."""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the managed cluster."""
    oidcIssuerUrl: Output[Literal['string']]
    """The OIDC token issuer URL."""
    omsagentIdentityObjectId: Output[Literal['string']]
    """The Object ID of the OMS agent identity."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the managed cluster was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the managed cluster."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    webAppRoutingIdentityObjectId: Output[Literal['string']]
    """The Object ID of Web Application Routing."""


class ContainerServiceManagedClusterBicep(Module):
    outputs: ContainerServiceManagedClusterOutputs


def container_service_managed_cluster(
        bicep: IO[str],
        params: ContainerServiceManagedCluster,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ContainerServiceManagedClusterBicep:
    symbol = "container_service_managed_cluster_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/container-service/managed-cluster:{tag}' = {{\n")
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
    output = ContainerServiceManagedClusterBicep(symbol)
    output.outputs = {
            'addonProfiles': Output(symbol, 'addonProfiles', 'object'),
            'controlPlaneFQDN': Output(symbol, 'controlPlaneFQDN', 'string'),
            'ingressApplicationGatewayIdentityObjectId': Output(symbol, 'ingressApplicationGatewayIdentityObjectId', 'string'),
            'keyvaultIdentityClientId': Output(symbol, 'keyvaultIdentityClientId', 'string'),
            'keyvaultIdentityObjectId': Output(symbol, 'keyvaultIdentityObjectId', 'string'),
            'kubeletIdentityClientId': Output(symbol, 'kubeletIdentityClientId', 'string'),
            'kubeletIdentityObjectId': Output(symbol, 'kubeletIdentityObjectId', 'string'),
            'kubeletIdentityResourceId': Output(symbol, 'kubeletIdentityResourceId', 'string'),
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'oidcIssuerUrl': Output(symbol, 'oidcIssuerUrl', 'string'),
            'omsagentIdentityObjectId': Output(symbol, 'omsagentIdentityObjectId', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
            'webAppRoutingIdentityObjectId': Output(symbol, 'webAppRoutingIdentityObjectId', 'string'),
        }

    return output
