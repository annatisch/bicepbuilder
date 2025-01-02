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
    roleDefinitionIdOrName: Required[str]
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


class ComputeVirtualMachineScaleSet(TypedDict, total=False):
    """"""
    adminPassword: Required[str]
    """When specifying a Windows Virtual Machine, this value should be passed."""
    adminUsername: Required[str]
    """Administrator username."""
    imageReference: Required[Dict[str, object]]
    """OS image reference. In case of marketplace images, it's the combination of the publisher, offer, sku, version attributes. In case of custom images it's the resource ID of the custom image."""
    name: Required[str]
    """Name of the VMSS."""
    nicConfigurations: Required[List[object]]
    """Configures NICs and PIPs."""
    osDisk: Required[Dict[str, object]]
    """Specifies the OS disk. For security reasons, it is recommended to specify DiskEncryptionSet into the osDisk object. Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VM Scale sets."""
    osType: Required[Literal['Linux', 'Windows']]
    """The chosen OS type."""
    skuName: Required[str]
    """The SKU size of the VMs."""
    additionalUnattendContent: List[object]
    """Specifies additional base-64 encoded XML formatted information that can be included in the Unattend.xml file, which is used by Windows Setup. - AdditionalUnattendContent object."""
    automaticRepairsPolicyEnabled: bool
    """Specifies whether automatic repairs should be enabled on the virtual machine scale set."""
    availabilityZones: List[object]
    """The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set."""
    bootDiagnosticEnabled: bool
    """Enable boot diagnostics to use default managed or secure storage. Defaults set to false."""
    bootDiagnosticStorageAccountName: str
    """The name of the boot diagnostic storage account. Provide this if you want to use your own storage account for security reasons instead of the recommended Microsoft Managed Storage Account."""
    bootDiagnosticStorageAccountUri: str
    """Storage account boot diagnostic base URI."""
    bypassPlatformSafetyChecksOnUserSchedule: bool
    """Enables customer to schedule patching without accidental upgrades."""
    customData: str
    """Custom data associated to the VM, this value will be automatically converted into base64 to account for the expected VM format."""
    dataDisks: List[object]
    """Specifies the data disks. For security reasons, it is recommended to specify DiskEncryptionSet into the dataDisk object. Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VM Scale sets."""
    diagnosticSettings: List['DiagnosticSetting']
    """The diagnostic settings of the service."""
    disableAutomaticRollback: bool
    """Whether OS image rollback feature should be disabled."""
    disablePasswordAuthentication: bool
    """Specifies whether password authentication should be disabled."""
    doNotRunExtensionsOnOverprovisionedVMs: bool
    """When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs."""
    enableAutomaticOSUpgrade: bool
    """Indicates whether OS upgrades should automatically be applied to scale set instances in a rolling fashion when a newer version of the OS image becomes available. Default value is false. If this is set to true for Windows based scale sets, enableAutomaticUpdates is automatically set to false and cannot be set to true."""
    enableAutomaticUpdates: bool
    """Indicates whether Automatic Updates is enabled for the Windows virtual machine. Default value is true. For virtual machine scale sets, this property can be updated and updates will take effect on OS reprovisioning."""
    enableCrossZoneUpgrade: bool
    """Allow VMSS to ignore AZ boundaries when constructing upgrade batches. Take into consideration the Update Domain and maxBatchInstancePercent to determine the batch size."""
    enableEvictionPolicy: bool
    """Specifies the eviction policy for the low priority virtual machine. Will result in 'Deallocate' eviction policy."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionAtHost: bool
    """This property can be used by user in the request to enable or disable the Host Encryption for the virtual machine. This will enable the encryption for all the disks including Resource/Temp disk at host itself. For security reasons, it is recommended to set encryptionAtHost to True. Restrictions: Cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your virtual machine scale sets."""
    extensionAntiMalwareConfig: Dict[str, object]
    """The configuration for the [Anti Malware] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionAzureDiskEncryptionConfig: Dict[str, object]
    """The configuration for the [Azure Disk Encryption] extension. Must at least contain the ["enabled": true] property to be executed. Restrictions: Cannot be enabled on disks that have encryption at host enabled. Managed disks encrypted using Azure Disk Encryption cannot be encrypted using customer-managed keys."""
    extensionCustomScriptConfig: Dict[str, object]
    """The configuration for the [Custom Script] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionDependencyAgentConfig: Dict[str, object]
    """The configuration for the [Dependency Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionDomainJoinConfig: Dict[str, object]
    """The configuration for the [Domain Join] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionDomainJoinPassword: str
    """Required if name is specified. Password of the user specified in user parameter."""
    extensionDSCConfig: Dict[str, object]
    """The configuration for the [Desired State Configuration] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionHealthConfig: Dict[str, object]
    """Turned on by default. The configuration for the [Application Health Monitoring] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionMonitoringAgentConfig: Dict[str, object]
    """The configuration for the [Monitoring Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionNetworkWatcherAgentConfig: Dict[str, object]
    """The configuration for the [Network Watcher Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    gracePeriod: str
    """The amount of time for which automatic repairs are suspended due to a state change on VM. The grace time starts after the state change has completed. This helps avoid premature or accidental repairs. The time duration should be specified in ISO 8601 format. The minimum allowed grace period is 30 minutes (PT30M). The maximum allowed grace period is 90 minutes (PT90M)."""
    licenseType: Literal['', 'Windows_Client', 'Windows_Server']
    """Specifies that the image or disk that is being used was licensed on-premises. This element is only used for images that contain the Windows Server operating system."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource."""
    maxBatchInstancePercent: int
    """The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability."""
    maxPriceForLowPriorityVm: int
    """Specifies the maximum price you are willing to pay for a low priority VM/VMSS. This price is in US Dollars."""
    maxSurge: bool
    """Create new virtual machines to upgrade the scale set, rather than updating the existing virtual machines. Existing virtual machines will be deleted once the new virtual machines are created for each batch."""
    maxUnhealthyInstancePercent: int
    """The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch."""
    maxUnhealthyUpgradedInstancePercent: int
    """The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch."""
    monitoringWorkspaceResourceId: str
    """Resource ID of the monitoring log analytics workspace."""
    orchestrationMode: Literal['Flexible', 'Uniform']
    """Specifies the orchestration mode for the virtual machine scale set."""
    overprovision: bool
    """Specifies whether the Virtual Machine Scale Set should be overprovisioned."""
    patchAssessmentMode: Literal['AutomaticByPlatform', 'ImageDefault']
    """VM guest patching assessment mode. Set it to 'AutomaticByPlatform' to enable automatically check for updates every 24 hours."""
    patchMode: Literal['', 'AutomaticByOS', 'AutomaticByPlatform', 'ImageDefault', 'Manual']
    """VM guest patching orchestration mode. 'AutomaticByOS' & 'Manual' are for Windows only, 'ImageDefault' for Linux only. Refer to 'https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching'."""
    pauseTimeBetweenBatches: str
    """The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format."""
    plan: Dict[str, object]
    """Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use."""
    prioritizeUnhealthyInstances: bool
    """Upgrade all unhealthy instances in a scale set before any healthy instances."""
    provisionVMAgent: bool
    """Indicates whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified in the request body, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later."""
    proximityPlacementGroupResourceId: str
    """Resource ID of a proximity placement group."""
    publicKeys: List[object]
    """The list of SSH public keys used to authenticate with linux based VMs."""
    rebootSetting: Literal['Always', 'IfRequired', 'Never', 'Unknown']
    """Specifies the reboot setting for all AutomaticByPlatform patch installation operations."""
    roleAssignments: List[Union['RoleAssignment', Literal['Contributor', 'Data Operator for Managed Disks', 'Desktop Virtualization Power On Contributor', 'Desktop Virtualization Power On Off Contributor', 'Desktop Virtualization Virtual Machine Contributor', 'DevTest Labs User', 'Disk Backup Reader', 'Disk Pool Operator', 'Disk Restore Operator', 'Disk Snapshot Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Virtual Machine Administrator Login', 'Virtual Machine Contributor', 'Virtual Machine User Login', 'VM Scanner Operator']]]
    """Array of role assignments to create."""
    rollbackFailedInstancesOnPolicyBreach: bool
    """Rollback failed instances to previous model if the Rolling Upgrade policy is violated."""
    sasTokenValidityLength: str
    """SAS token validity length to use to download files from storage accounts. Usage: 'PT8H' - valid for 8 hours; 'P5D' - valid for 5 days; 'P1Y' - valid for 1 year. When not provided, the SAS token will be valid for 8 hours."""
    scaleInPolicy: Dict[str, object]
    """Specifies the scale-in policy that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled-in."""
    scaleSetFaultDomain: int
    """Fault Domain count for each placement group."""
    scheduledEventsProfile: Dict[str, object]
    """Specifies Scheduled Event related configurations."""
    secrets: List[object]
    """Specifies set of certificates that should be installed onto the virtual machines in the scale set."""
    secureBootEnabled: bool
    """Specifies whether secure boot should be enabled on the virtual machine scale set. This parameter is part of the UefiSettings. SecurityType should be set to TrustedLaunch to enable UefiSettings."""
    securityType: str
    """Specifies the SecurityType of the virtual machine scale set. It is set as TrustedLaunch to enable UefiSettings."""
    singlePlacementGroup: bool
    """When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true."""
    skuCapacity: int
    """The initial instance count of scale set VMs."""
    tags: Dict[str, object]
    """Tags of the resource."""
    timeZone: str
    """Specifies the time zone of the virtual machine. e.g. 'Pacific Standard Time'. Possible values can be """
    ultraSSDEnabled: bool
    """The flag that enables or disables a capability to have one or more managed data disks with UltraSSD_LRS storage account type on the VM or VMSS. Managed disks with storage account type UltraSSD_LRS can be added to a virtual machine or virtual machine scale set only if this property is enabled."""
    upgradePolicyMode: Literal['Automatic', 'Manual', 'Rolling']
    """Specifies the mode of an upgrade to virtual machines in the scale set.' Manual - You control the application of updates to virtual machines in the scale set. You do this by using the manualUpgrade action. ; Automatic - All virtual machines in the scale set are automatically updated at the same time. - Automatic, Manual, Rolling."""
    vmNamePrefix: str
    """Specifies the computer name prefix for all of the virtual machines in the scale set."""
    vmPriority: Literal['Low', 'Regular', 'Spot']
    """Specifies the priority for the virtual machine."""
    vTpmEnabled: bool
    """Specifies whether vTPM should be enabled on the virtual machine scale set. This parameter is part of the UefiSettings.  SecurityType should be set to TrustedLaunch to enable UefiSettings."""
    winRM: Dict[str, object]
    """Specifies the Windows Remote Management listeners. This enables remote Windows PowerShell. - WinRMConfiguration object."""
    zoneBalance: bool
    """Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage."""
    baseTime: str
    """Do not provide a value! This date value is used to generate a registration token."""


class ComputeVirtualMachineScaleSetOutputs(TypedDict, total=False):
    """Outputs for ComputeVirtualMachineScaleSet"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the virtual machine scale set."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the virtual machine scale set."""
    resourceId: Output[Literal['string']]
    """The resource ID of the virtual machine scale set."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class ComputeVirtualMachineScaleSetBicep(Module):
    outputs: ComputeVirtualMachineScaleSetOutputs


def compute_virtual_machine_scale_set(
        bicep: IO[str],
        params: ComputeVirtualMachineScaleSet,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.5.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ComputeVirtualMachineScaleSetBicep:
    symbol = "compute_virtual_machine_scale_set_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/compute/virtual-machine-scale-set:{tag}' = {{\n")
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
    output = ComputeVirtualMachineScaleSetBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
        }

    return output
