from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class AgentPool(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the agent pool."""
    availabilityZones: List[object]
    """The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is "VirtualMachineScaleSets"."""
    count: int
    """Desired Number of agents (VMs) specified to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default value is 1."""
    enableAutoScaling: bool
    """Whether to enable auto-scaler."""
    enableEncryptionAtHost: bool
    """This is only supported on certain VM sizes and in certain Azure regions. For more information, see: /azure/aks/enable-host-encryption. For security reasons, this setting should be enabled."""
    enableFIPS: bool
    """See Add a FIPS-enabled node pool (https://learn.microsoft.com/en-us/azure/aks/use-multiple-node-pools#add-a-fips-enabled-node-pool-preview) for more details."""
    enableNodePublicIP: bool
    """Some scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. For more information see assigning a public IP per node (https://learn.microsoft.com/en-us/azure/aks/use-multiple-node-pools#assign-a-public-ip-per-node-for-your-node-pools)."""
    enableUltraSSD: bool
    """Whether to enable UltraSSD."""
    gpuInstanceProfile: Literal['MIG1g', 'MIG2g', 'MIG3g', 'MIG4g', 'MIG7g']
    """GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU."""
    kubeletDiskType: str
    """Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage."""
    maxCount: int
    """The maximum number of nodes for auto-scaling."""
    maxPods: int
    """The maximum number of pods that can run on a node."""
    maxSurge: str
    """This can either be set to an integer (e.g. "5") or a percentage (e.g. "50%"). If a percentage is specified, it is the percentage of the total agent pool size at the time of the upgrade. For percentages, fractional nodes are rounded up. If not specified, the default is 1. For more information, including best practices, see: /azure/aks/upgrade-cluster#customize-node-surge-upgrade."""
    minCount: int
    """The minimum number of nodes for auto-scaling."""
    mode: str
    """A cluster must have at least one "System" Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: /azure/aks/use-system-pools."""
    nodeLabels: Dict[str, object]
    """The node labels to be persisted across all nodes in agent pool."""
    nodePublicIpPrefixResourceId: str
    """ResourceId of the node PublicIPPrefix."""
    nodeTaints: List[object]
    """The taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule."""
    orchestratorVersion: str
    """As a best practice, you should upgrade all node pools in an AKS cluster to the same Kubernetes version. The node pool version must have the same major version as the control plane. The node pool minor version must be within two minor versions of the control plane version. The node pool version cannot be greater than the control plane version. For more information see upgrading a node pool (https://learn.microsoft.com/en-us/azure/aks/use-multiple-node-pools#upgrade-a-node-pool)."""
    osDiskSizeGB: int
    """OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified."""
    osDiskType: Literal['Ephemeral', 'Managed']
    """The default is "Ephemeral" if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to "Managed". May not be changed after creation. For more information see Ephemeral OS (https://learn.microsoft.com/en-us/azure/aks/cluster-configuration#ephemeral-os)."""
    osSku: Literal['AzureLinux', 'CBLMariner', 'Ubuntu', 'Windows2019', 'Windows2022']
    """Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes <= 1.24 or Windows2022 when Kubernetes >= 1.25 if OSType is Windows."""
    osType: Literal['Linux', 'Windows']
    """The operating system type. The default is Linux."""
    podSubnetResourceId: str
    """Subnet resource ID for the pod IPs. If omitted, pod IPs are statically assigned on the node subnet (see vnetSubnetID for more details). This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}."""
    proximityPlacementGroupResourceId: str
    """The ID for the Proximity Placement Group."""
    scaleDownMode: Literal['Deallocate', 'Delete']
    """Describes how VMs are added to or removed from Agent Pools. See """
    scaleSetEvictionPolicy: Literal['Deallocate', 'Delete']
    """The eviction policy specifies what to do with the VM when it is evicted. The default is Delete. For more information about eviction see spot VMs."""
    scaleSetPriority: Literal['Regular', 'Spot']
    """The Virtual Machine Scale Set priority."""
    sourceResourceId: str
    """This is the ARM ID of the source object to be used to create the target object."""
    spotMaxPrice: int
    """Possible values are any decimal value greater than zero or -1 which indicates the willingness to pay any on-demand price. For more details on spot pricing, see spot VMs pricing (https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms#pricing)."""
    tags: Dict[str, object]
    """Tags of the resource."""
    type: str
    """The type of Agent Pool."""
    vmSize: str
    """VM size. VM size availability varies by region. If a node contains insufficient compute resources (memory, cpu, etc) pods might fail to run correctly. For more details on restricted VM sizes, see: /azure/aks/quotas-skus-regions."""
    vnetSubnetResourceId: str
    """Node Subnet ID. If this is not specified, a VNET and subnet will be generated and used. If no podSubnetID is specified, this applies to nodes and pods, otherwise it applies to just nodes. This is of the form: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/subnets/{subnetName}."""
    workloadRuntime: str
    """Determines the type of workload a node can run."""


class AgentPoolOutputs(TypedDict, total=False):
    """Outputs for AgentPool"""
    name: Output[Literal['string']]
    """The name of the agent pool."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the agent pool was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the agent pool."""


class AgentPoolModule(Module):
    outputs: AgentPoolOutputs

