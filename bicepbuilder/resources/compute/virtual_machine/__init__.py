from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ManagedDisk(TypedDict, total=False):
    """The managed disk parameters."""
    diskEncryptionSetResourceId: str
    """Specifies the customer managed disk encryption set resource id for the managed disk."""
    storageAccountType: Literal['Premium_LRS', 'Premium_ZRS', 'PremiumV2_LRS', 'Standard_LRS', 'StandardSSD_LRS', 'StandardSSD_ZRS', 'UltraSSD_LRS']
    """Specifies the storage account type for the managed disk."""


class OsDisk(TypedDict, total=False):
    """Specifies the OS disk. For security reasons, it is recommended to specify DiskEncryptionSet into the osDisk object.  Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VMs."""
    managedDisk: Required['ManagedDisk']
    """The managed disk parameters."""
    caching: Literal['None', 'ReadOnly', 'ReadWrite']
    """Specifies the caching requirements."""
    createOption: Literal['Attach', 'Empty', 'FromImage']
    """Specifies how the virtual machine should be created."""
    deleteOption: Literal['Delete', 'Detach']
    """Specifies whether data disk should be deleted or detached upon VM deletion."""
    diskSizeGB: int
    """Specifies the size of an empty data disk in gigabytes."""
    name: str
    """The disk name."""


class ManagedDisk(TypedDict, total=False):
    """The managed disk parameters."""
    storageAccountType: Required[Literal['Premium_LRS', 'Premium_ZRS', 'PremiumV2_LRS', 'Standard_LRS', 'StandardSSD_LRS', 'StandardSSD_ZRS', 'UltraSSD_LRS']]
    """Specifies the storage account type for the managed disk."""
    diskEncryptionSetResourceId: str
    """Specifies the customer managed disk encryption set resource id for the managed disk."""
    id: str
    """Specifies the customer managed disk id for the managed disk."""


class DataDisk(TypedDict, total=False):
    """Specifies the data disks. For security reasons, it is recommended to specify DiskEncryptionSet into the dataDisk object. Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VMs."""
    diskSizeGB: Required[int]
    """Specifies the size of an empty data disk in gigabytes."""
    managedDisk: Required['ManagedDisk']
    """The managed disk parameters."""
    caching: Literal['None', 'ReadOnly', 'ReadWrite']
    """Specifies the caching requirements."""
    createOption: Literal['Attach', 'Empty', 'FromImage']
    """Specifies how the virtual machine should be created."""
    deleteOption: Literal['Delete', 'Detach']
    """Specifies whether data disk should be deleted or detached upon VM deletion."""
    diskIOPSReadWrite: int
    """The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes."""
    diskMBpsReadWrite: int
    """The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10."""
    lun: int
    """Specifies the logical unit number of the data disk."""
    name: str
    """The disk name."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. The system-assigned managed identity will automatically be enabled if extensionAadJoinConfig.enabled = "True"."""
    systemAssigned: bool
    """Enables system assigned managed identity on the resource."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Data Operator for Managed Disks', 'Desktop Virtualization Power On Contributor', 'Desktop Virtualization Power On Off Contributor', 'Desktop Virtualization Virtual Machine Contributor', 'DevTest Labs User', 'Disk Backup Reader', 'Disk Pool Operator', 'Disk Restore Operator', 'Disk Snapshot Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator', 'Virtual Machine Administrator Login', 'Virtual Machine Contributor', 'Virtual Machine User Login', 'VM Scanner Operator']]]
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


class ComputeVirtualMachine(TypedDict, total=False):
    """"""
    adminUsername: Required[str]
    """Administrator username."""
    imageReference: Required[Dict[str, object]]
    """OS image reference. In case of marketplace images, it's the combination of the publisher, offer, sku, version attributes. In case of custom images it's the resource ID of the custom image."""
    name: Required[str]
    """The name of the virtual machine to be created. You should use a unique prefix to reduce name collisions in Active Directory."""
    nicConfigurations: Required[List[object]]
    """Configures NICs and PIPs."""
    osDisk: Required['OsDisk']
    """Specifies the OS disk. For security reasons, it is recommended to specify DiskEncryptionSet into the osDisk object.  Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VMs."""
    osType: Required[Literal['Linux', 'Windows']]
    """The chosen OS type."""
    vmSize: Required[str]
    """Specifies the size for the VMs."""
    zone: Required[Literal[0, 1, 2, 3]]
    """If set to 1, 2 or 3, the availability zone for all VMs is hardcoded to that value. If zero, then availability zones is not used. Cannot be used in combination with availability set nor scale set."""
    additionalUnattendContent: List[object]
    """Specifies additional XML formatted information that can be included in the Unattend.xml file, which is used by Windows Setup. Contents are defined by setting name, component name, and the pass in which the content is applied."""
    adminPassword: str
    """When specifying a Windows Virtual Machine, this value should be passed."""
    allowExtensionOperations: bool
    """Specifies whether extension operations should be allowed on the virtual machine. This may only be set to False when no extensions are present on the virtual machine."""
    autoShutdownConfig: Dict[str, object]
    """The configuration for auto-shutdown."""
    availabilitySetResourceId: str
    """Resource ID of an availability set. Cannot be used in combination with availability zone nor scale set."""
    backupPolicyName: str
    """Backup policy the VMs should be using for backup. If not provided, it will use the DefaultPolicy from the backup recovery service vault."""
    backupVaultName: str
    """Recovery service vault name to add VMs to backup."""
    backupVaultResourceGroup: str
    """Resource group of the backup recovery service vault. If not provided the current resource group name is considered by default."""
    bootDiagnostics: bool
    """Whether boot diagnostics should be enabled on the Virtual Machine. Boot diagnostics will be enabled with a managed storage account if no bootDiagnosticsStorageAccountName value is provided. If bootDiagnostics and bootDiagnosticsStorageAccountName values are not provided, boot diagnostics will be disabled."""
    bootDiagnosticStorageAccountName: str
    """Custom storage account used to store boot diagnostic information. Boot diagnostics will be enabled with a custom storage account if a value is provided."""
    bootDiagnosticStorageAccountUri: str
    """Storage account boot diagnostic base URI."""
    bypassPlatformSafetyChecksOnUserSchedule: bool
    """Enables customer to schedule patching without accidental upgrades."""
    certificatesToBeInstalled: List[object]
    """Specifies set of certificates that should be installed onto the virtual machine."""
    computerName: str
    """Can be used if the computer name needs to be different from the Azure VM resource name. If not used, the resource name will be used as computer name."""
    configurationProfile: str
    """The configuration profile of automanage. Either '/providers/Microsoft.Automanage/bestPractices/AzureBestPracticesProduction', 'providers/Microsoft.Automanage/bestPractices/AzureBestPracticesDevTest' or the resource Id of custom profile."""
    customData: str
    """Custom data associated to the VM, this value will be automatically converted into base64 to account for the expected VM format."""
    dataDisks: List['DataDisk']
    """Specifies the data disks. For security reasons, it is recommended to specify DiskEncryptionSet into the dataDisk object. Restrictions: DiskEncryptionSet cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VMs."""
    dedicatedHostId: str
    """Specifies resource ID about the dedicated host that the virtual machine resides in."""
    disablePasswordAuthentication: bool
    """Specifies whether password authentication should be disabled."""
    enableAutomaticUpdates: bool
    """Indicates whether Automatic Updates is enabled for the Windows virtual machine. Default value is true. When patchMode is set to Manual, this parameter must be set to false. For virtual machine scale sets, this property can be updated and updates will take effect on OS reprovisioning."""
    enableEvictionPolicy: bool
    """Specifies the eviction policy for the low priority virtual machine. Will result in 'Deallocate' eviction policy."""
    enableHotpatching: bool
    """Enables customers to patch their Azure VMs without requiring a reboot. For enableHotpatching, the 'provisionVMAgent' must be set to true and 'patchMode' must be set to 'AutomaticByPlatform'."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionAtHost: bool
    """This property can be used by user in the request to enable or disable the Host Encryption for the virtual machine. This will enable the encryption for all the disks including Resource/Temp disk at host itself. For security reasons, it is recommended to set encryptionAtHost to True. Restrictions: Cannot be enabled if Azure Disk Encryption (guest-VM encryption using bitlocker/DM-Crypt) is enabled on your VMs."""
    extensionAadJoinConfig: Dict[str, object]
    """The configuration for the [AAD Join] extension. Must at least contain the ["enabled": true] property to be executed. To enroll in Intune, add the setting mdmId: "0000000a-0000-0000-c000-000000000000"."""
    extensionAntiMalwareConfig: Dict[str, object]
    """The configuration for the [Anti Malware] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionAzureDiskEncryptionConfig: Dict[str, object]
    """The configuration for the [Azure Disk Encryption] extension. Must at least contain the ["enabled": true] property to be executed. Restrictions: Cannot be enabled on disks that have encryption at host enabled. Managed disks encrypted using Azure Disk Encryption cannot be encrypted using customer-managed keys."""
    extensionCustomScriptConfig: Dict[str, object]
    """The configuration for the [Custom Script] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionCustomScriptProtectedSetting: Dict[str, object]
    """An object that contains the extension specific protected settings."""
    extensionDependencyAgentConfig: Dict[str, object]
    """The configuration for the [Dependency Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionDomainJoinConfig: Dict[str, object]
    """The configuration for the [Domain Join] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionDomainJoinPassword: str
    """Required if name is specified. Password of the user specified in user parameter."""
    extensionDSCConfig: Dict[str, object]
    """The configuration for the [Desired State Configuration] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionGuestConfigurationExtension: Dict[str, object]
    """The configuration for the [Guest Configuration] extension. Must at least contain the ["enabled": true] property to be executed. Needs a managed identy."""
    extensionGuestConfigurationExtensionProtectedSettings: Dict[str, object]
    """An object that contains the extension specific protected settings."""
    extensionHostPoolRegistration: Dict[str, object]
    """The configuration for the [Host Pool Registration] extension. Must at least contain the ["enabled": true] property to be executed. Needs a managed identy."""
    extensionMonitoringAgentConfig: Dict[str, object]
    """The configuration for the [Monitoring Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionNetworkWatcherAgentConfig: Dict[str, object]
    """The configuration for the [Network Watcher Agent] extension. Must at least contain the ["enabled": true] property to be executed."""
    extensionNvidiaGpuDriverWindows: Dict[str, object]
    """The configuration for the [Nvidia Gpu Driver Windows] extension. Must at least contain the ["enabled": true] property to be executed."""
    galleryApplications: List[object]
    """Specifies the gallery applications that should be made available to the VM/VMSS."""
    guestConfiguration: Dict[str, object]
    """The guest configuration for the virtual machine. Needs the Guest Configuration extension to be enabled."""
    licenseType: Literal['', 'RHEL_BYOS', 'SLES_BYOS', 'Windows_Client', 'Windows_Server']
    """Specifies that the image or disk that is being used was licensed on-premises."""
    location: str
    """Location for all resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    maintenanceConfigurationResourceId: str
    """The resource Id of a maintenance configuration for this VM."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. The system-assigned managed identity will automatically be enabled if extensionAadJoinConfig.enabled = "True"."""
    maxPriceForLowPriorityVm: str
    """Specifies the maximum price you are willing to pay for a low priority VM/VMSS. This price is in US Dollars."""
    patchAssessmentMode: Literal['AutomaticByPlatform', 'ImageDefault']
    """VM guest patching assessment mode. Set it to 'AutomaticByPlatform' to enable automatically check for updates every 24 hours."""
    patchMode: Literal['', 'AutomaticByOS', 'AutomaticByPlatform', 'ImageDefault', 'Manual']
    """VM guest patching orchestration mode. 'AutomaticByOS' & 'Manual' are for Windows only, 'ImageDefault' for Linux only. Refer to 'https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching'."""
    plan: Dict[str, object]
    """Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use."""
    priority: Literal['Low', 'Regular', 'Spot']
    """Specifies the priority for the virtual machine."""
    provisionVMAgent: bool
    """Indicates whether virtual machine agent should be provisioned on the virtual machine. When this property is not specified in the request body, default behavior is to set it to true. This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later."""
    proximityPlacementGroupResourceId: str
    """Resource ID of a proximity placement group."""
    publicKeys: List[object]
    """The list of SSH public keys used to authenticate with linux based VMs."""
    rebootSetting: Literal['Always', 'IfRequired', 'Never', 'Unknown']
    """Specifies the reboot setting for all AutomaticByPlatform patch installation operations."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    sasTokenValidityLength: str
    """SAS token validity length to use to download files from storage accounts. Usage: 'PT8H' - valid for 8 hours; 'P5D' - valid for 5 days; 'P1Y' - valid for 1 year. When not provided, the SAS token will be valid for 8 hours."""
    secureBootEnabled: bool
    """Specifies whether secure boot should be enabled on the virtual machine. This parameter is part of the UefiSettings. SecurityType should be set to TrustedLaunch to enable UefiSettings."""
    securityType: Literal['', 'ConfidentialVM', 'TrustedLaunch']
    """Specifies the SecurityType of the virtual machine. It has to be set to any specified value to enable UefiSettings. The default behavior is: UefiSettings will not be enabled unless this property is set."""
    tags: Dict[str, object]
    """Tags of the resource."""
    timeZone: str
    """Specifies the time zone of the virtual machine. e.g. 'Pacific Standard Time'. Possible values can be """
    ultraSSDEnabled: bool
    """The flag that enables or disables a capability to have one or more managed data disks with UltraSSD_LRS storage account type on the VM or VMSS. Managed disks with storage account type UltraSSD_LRS can be added to a virtual machine or virtual machine scale set only if this property is enabled."""
    userData: str
    """UserData for the VM, which must be base-64 encoded. Customer should not pass any secrets in here."""
    virtualMachineScaleSetResourceId: str
    """Resource ID of a virtual machine scale set, where the VM should be added."""
    vTpmEnabled: bool
    """Specifies whether vTPM should be enabled on the virtual machine. This parameter is part of the UefiSettings.  SecurityType should be set to TrustedLaunch to enable UefiSettings."""
    winRM: List[object]
    """Specifies the Windows Remote Management listeners. This enables remote Windows PowerShell. - WinRMConfiguration object."""
    baseTime: str
    """Do not provide a value! This date value is used to generate a registration token."""


class ComputeVirtualMachineOutputs(TypedDict, total=False):
    """Outputs for ComputeVirtualMachine"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the VM."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the VM was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the VM."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""


class ComputeVirtualMachineModule(Module):
    outputs: ComputeVirtualMachineOutputs

