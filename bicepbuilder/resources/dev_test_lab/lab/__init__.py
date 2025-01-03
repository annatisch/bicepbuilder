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


class Notificationchannel(TypedDict, total=False):
    """Notification Channels to create for the lab. Required if the schedules property "notificationSettingsStatus" is set to "Enabled."""
    events: Required[List[object]]
    """The list of event for which this notification is enabled. Can be "AutoShutdown" or "Cost"."""
    name: Required[Literal['autoShutdown', 'costThreshold']]
    """The name of the notification channel."""
    emailRecipient: str
    """The email recipient to send notifications to (can be a list of semi-colon separated email addresses). Required if "webHookUrl" is empty."""
    webHookUrl: str
    """The webhook URL to which the notification will be sent. Required if "emailRecipient" is empty."""
    description: str
    """The description of the notification."""
    notificationLocale: str
    """The locale to use when sending a notification (fallback for unsupported languages is EN)."""
    tags: Dict[str, object]
    """The tags of the notification channel."""


class Artifactsource(TypedDict, total=False):
    """Artifact sources to create for the lab."""
    name: Required[str]
    """The name of the artifact source."""
    uri: Required[str]
    """The artifact source's URI."""
    armTemplateFolderPath: str
    """The folder containing Azure Resource Manager templates. Required if "folderPath" is empty."""
    folderPath: str
    """The folder containing artifacts. At least one folder path is required. Required if "armTemplateFolderPath" is empty."""
    branchRef: str
    """The artifact source's branch reference (e.g. main or master)."""
    displayName: str
    """The display name of the artifact source. Default is the name of the artifact source."""
    securityToken: str
    """The security token to authenticate to the artifact source. Private artifacts use the system-identity of the lab to store the security token for the artifact source in the lab's managed Azure Key Vault. Access to the Azure Key Vault is granted automatically only when the lab is created with a system-assigned identity."""
    sourceType: Literal['GitHub', 'StorageAccount', 'VsoGit']
    """The artifact source's type."""
    status: Literal['Disabled', 'Enabled']
    """Indicates if the artifact source is enabled (values: Enabled, Disabled). Default is "Enabled"."""
    tags: Dict[str, object]
    """The tags of the artifact source."""


class Cost(TypedDict, total=False):
    """Costs to create for the lab."""
    cycleType: Required[Literal['CalendarMonth', 'Custom']]
    """Reporting cycle type."""
    cycleEndDateTime: str
    """Reporting cycle end date in the zulu time format (e.g. 2023-12-01T00:00:00.000Z). Required if cycleType is set to "Custom"."""
    cycleStartDateTime: str
    """Reporting cycle start date in the zulu time format (e.g. 2023-12-01T00:00:00.000Z). Required if cycleType is set to "Custom"."""
    currencyCode: str
    """The currency code of the cost. Default is "USD"."""
    status: Literal['Disabled', 'Enabled']
    """Target cost status."""
    tags: Dict[str, object]
    """The tags of the resource."""
    target: int
    """Lab target cost (e.g. 100). The target cost will appear in the "Cost trend" chart to allow tracking lab spending relative to the target cost for the current reporting cycleSetting the target cost to 0 will disable all thresholds."""
    thresholdValue100DisplayOnChart: Literal['Disabled', 'Enabled']
    """Target Cost threshold at 100% display on chart. Indicates whether this threshold will be displayed on cost charts."""
    thresholdValue100SendNotificationWhenExceeded: Literal['Disabled', 'Enabled']
    """Target cost threshold at 100% send notification when exceeded. Indicates whether notifications will be sent when this threshold is exceeded."""
    thresholdValue125DisplayOnChart: Literal['Disabled', 'Enabled']
    """Target Cost threshold at 125% display on chart. Indicates whether this threshold will be displayed on cost charts."""
    thresholdValue125SendNotificationWhenExceeded: Literal['Disabled', 'Enabled']
    """Target cost threshold at 125% send notification when exceeded. Indicates whether notifications will be sent when this threshold is exceeded."""
    thresholdValue25DisplayOnChart: Literal['Disabled', 'Enabled']
    """Target Cost threshold at 25% display on chart. Indicates whether this threshold will be displayed on cost charts."""
    thresholdValue25SendNotificationWhenExceeded: Literal['Disabled', 'Enabled']
    """Target cost threshold at 25% send notification when exceeded. Indicates whether notifications will be sent when this threshold is exceeded."""
    thresholdValue50DisplayOnChart: Literal['Disabled', 'Enabled']
    """Target Cost threshold at 50% display on chart. Indicates whether this threshold will be displayed on cost charts."""
    thresholdValue50SendNotificationWhenExceeded: Literal['Disabled', 'Enabled']
    """Target cost threshold at 50% send notification when exceeded. Indicates whether notifications will be sent when this threshold is exceeded."""
    thresholdValue75DisplayOnChart: Literal['Disabled', 'Enabled']
    """Target Cost threshold at 75% display on chart. Indicates whether this threshold will be displayed on cost charts."""
    thresholdValue75SendNotificationWhenExceeded: Literal['Disabled', 'Enabled']
    """Target cost threshold at 75% send notification when exceeded. Indicates whether notifications will be sent when this threshold is exceeded."""


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class ManagedIdentity(TypedDict, total=False):
    """The managed identity definition for this resource. For new labs created after 8/10/2020, the lab's system assigned identity is set to On by default and lab owner will not be able to turn this off for the lifecycle of the lab."""
    userAssignedResourceIds: List[object]
    """The resource ID(s) to assign to the resource. Required if a user assigned identity is used for encryption."""


class Policy(TypedDict, total=False):
    """Policies to create for the lab."""
    evaluatorType: Required[Literal['AllowedValuesPolicy', 'MaxValuePolicy']]
    """The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy)."""
    factName: Required[Literal['EnvironmentTemplate', 'GalleryImage', 'LabPremiumVmCount', 'LabTargetCost', 'LabVmCount', 'LabVmSize', 'ScheduleEditPermission', 'UserOwnedLabPremiumVmCount', 'UserOwnedLabVmCount', 'UserOwnedLabVmCountInSubnet']]
    """The fact name of the policy."""
    name: Required[str]
    """The name of the policy."""
    threshold: Required[str]
    """The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy)."""
    description: str
    """The description of the policy."""
    factData: str
    """The fact data of the policy."""
    status: Literal['Disabled', 'Enabled']
    """The status of the policy. Default is "Enabled"."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'DevTest Labs User', 'Owner', 'Reader', 'Resource Policy Contributor', 'Role Based Access Control Administrator', 'User Access Administrator', 'Virtual Machine Contributor']]]
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


class DailyRecurrence(TypedDict, total=False):
    """The daily recurrence of the schedule."""
    time: Required[str]
    """The time of day the schedule will occur."""


class HourlyRecurrence(TypedDict, total=False):
    """If the schedule will occur multiple times a day, specify the hourly recurrence."""
    minute: Required[int]
    """Minutes of the hour the schedule will run."""


class NotificationSetting(TypedDict, total=False):
    """The notification settings for the schedule."""
    emailRecipient: str
    """The email recipient to send notifications to (can be a list of semi-colon separated email addresses). Required if "webHookUrl" is empty."""
    webHookUrl: str
    """The webhook URL to which the notification will be sent. Required if "emailRecipient" is empty."""
    notificationLocale: str
    """The locale to use when sending a notification (fallback for unsupported languages is EN)."""
    status: Literal['Disabled', 'Enabled']
    """If notifications are enabled for this schedule (i.e. Enabled, Disabled). Default is Disabled."""
    timeInMinutes: int
    """Time in minutes before event at which notification will be sent. Default is 30 minutes if status is Enabled and not specified."""


class WeeklyRecurrence(TypedDict, total=False):
    """If the schedule will occur only some days of the week, specify the weekly recurrence."""
    time: Required[str]
    """The time of day the schedule will occur."""
    weekdays: Required[List[object]]
    """The days of the week for which the schedule is set (e.g. Sunday, Monday, Tuesday, etc.)."""


class Schedule(TypedDict, total=False):
    """Schedules to create for the lab."""
    name: Required[Literal['LabVmAutoStart', 'LabVmsShutdown']]
    """The name of the schedule."""
    taskType: Required[Literal['LabVmsShutdownTask', 'LabVmsStartupTask']]
    """The task type of the schedule (e.g. LabVmsShutdownTask, LabVmsStartupTask)."""
    dailyRecurrence: 'DailyRecurrence'
    """The daily recurrence of the schedule."""
    hourlyRecurrence: 'HourlyRecurrence'
    """If the schedule will occur multiple times a day, specify the hourly recurrence."""
    notificationSettings: 'NotificationSetting'
    """The notification settings for the schedule."""
    status: Literal['Disabled', 'Enabled']
    """The status of the schedule (i.e. Enabled, Disabled). Default is "Enabled"."""
    tags: Dict[str, object]
    """The tags of the schedule."""
    targetResourceId: str
    """The resource ID to which the schedule belongs."""
    timeZoneId: str
    """The time zone ID of the schedule. Defaults to "Pacific Standard time"."""
    weeklyRecurrence: 'WeeklyRecurrence'
    """If the schedule will occur only some days of the week, specify the weekly recurrence."""


class AllowedSubnet(TypedDict, total=False):
    """The allowed subnets of the virtual network."""
    labSubnetName: Required[str]
    """The name of the subnet as seen in the lab."""
    resourceId: Required[str]
    """The resource ID of the allowed subnet."""
    allowPublicIp: Literal['Allow', 'Default', 'Deny']
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""


class AllowedPort(TypedDict, total=False):
    """Backend ports that virtual machines on this subnet are allowed to expose."""
    backendPort: Required[int]
    """Backend port of the target virtual machine."""
    transportProtocol: Required[Literal['Tcp', 'Udp']]
    """Protocol type of the port."""


class SharedPublicIpAddressConfiguration(TypedDict, total=False):
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""
    allowedPorts: Required[List['AllowedPort']]
    """Backend ports that virtual machines on this subnet are allowed to expose."""


class SubnetOverride(TypedDict, total=False):
    """The subnet overrides of the virtual network."""
    labSubnetName: Required[str]
    """The name given to the subnet within the lab."""
    resourceId: Required[str]
    """The resource ID of the subnet."""
    sharedPublicIpAddressConfiguration: 'SharedPublicIpAddressConfiguration'
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""
    useInVmCreationPermission: Literal['Allow', 'Default', 'Deny']
    """Indicates whether this subnet can be used during virtual machine creation (i.e. Allow, Deny)."""
    usePublicIpAddressPermission: Literal['Allow', 'Default', 'Deny']
    """Indicates whether public IP addresses can be assigned to virtual machines on this subnet (i.e. Allow, Deny)."""
    virtualNetworkPoolName: str
    """The virtual network pool associated with this subnet."""


class Virtualnetwork(TypedDict, total=False):
    """Virtual networks to create for the lab."""
    externalProviderResourceId: Required[str]
    """The external provider resource ID of the virtual network."""
    name: Required[str]
    """The name of the virtual network."""
    allowedSubnets: List['AllowedSubnet']
    """The allowed subnets of the virtual network."""
    description: str
    """The description of the virtual network."""
    subnetOverrides: List['SubnetOverride']
    """The subnet overrides of the virtual network."""
    tags: Dict[str, object]
    """The tags of the virtual network."""


class DevTestLab(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the lab."""
    encryptionDiskEncryptionSetId: str
    """The Disk Encryption Set Resource ID used to encrypt OS and data disks created as part of the the lab. Required if encryptionType is set to "EncryptionAtRestWithCustomerKey"."""
    notificationchannels: List['Notificationchannel']
    """Notification Channels to create for the lab. Required if the schedules property "notificationSettingsStatus" is set to "Enabled."""
    announcement: Dict[str, object]
    """The properties of any lab announcement associated with this lab."""
    artifactsources: List['Artifactsource']
    """Artifact sources to create for the lab."""
    artifactsStorageAccount: str
    """The resource ID of the storage account used to store artifacts and images by the lab. Also used for defaultStorageAccount, defaultPremiumStorageAccount and premiumDataDiskStorageAccount properties. If left empty, a default storage account will be created by the lab and used."""
    browserConnect: Literal['Disabled', 'Enabled']
    """Enable browser connect on virtual machines if the lab's VNETs have configured Azure Bastion."""
    costs: 'Cost'
    """Costs to create for the lab."""
    disableAutoUpgradeCseMinorVersion: bool
    """Disable auto upgrade custom script extension minor version."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    encryptionType: Literal['EncryptionAtRestWithCustomerKey', 'EncryptionAtRestWithPlatformKey']
    """Specify how OS and data disks created as part of the lab are encrypted."""
    environmentPermission: Literal['Contributor', 'Reader']
    """The access rights to be granted to the user when provisioning an environment."""
    extendedProperties: Dict[str, object]
    """Extended properties of the lab used for experimental features."""
    isolateLabResources: Literal['Disabled', 'Enabled']
    """Enable lab resources isolation from the public internet."""
    labStorageType: Literal['Premium', 'Standard', 'StandardSSD']
    """Type of storage used by the lab. It can be either Premium or Standard."""
    location: str
    """Location for all Resources."""
    lock: 'Lock'
    """The lock settings of the service."""
    managedIdentities: 'ManagedIdentity'
    """The managed identity definition for this resource. For new labs created after 8/10/2020, the lab's system assigned identity is set to On by default and lab owner will not be able to turn this off for the lifecycle of the lab."""
    managementIdentitiesResourceIds: List[object]
    """The resource ID(s) to assign to the virtual machines associated with this lab."""
    mandatoryArtifactsResourceIdsLinux: List[object]
    """The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user."""
    mandatoryArtifactsResourceIdsWindows: List[object]
    """The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user."""
    policies: List['Policy']
    """Policies to create for the lab."""
    premiumDataDisks: Literal['Disabled', 'Enabled']
    """The setting to enable usage of premium data disks. When its value is "Enabled", creation of standard or premium data disks is allowed. When its value is "Disabled", only creation of standard data disks is allowed. Default is "Disabled"."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    schedules: List['Schedule']
    """Schedules to create for the lab."""
    support: Dict[str, object]
    """The properties of any lab support message associated with this lab."""
    tags: Dict[str, object]
    """Tags of the resource."""
    virtualnetworks: List['Virtualnetwork']
    """Virtual networks to create for the lab."""
    vmCreationResourceGroupId: str
    """Resource Group allocation for virtual machines. If left empty, virtual machines will be deployed in their own Resource Groups. Default is the same Resource Group for DevTest Lab."""


class DevTestLabOutputs(TypedDict, total=False):
    """Outputs for DevTestLab"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the lab."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the lab was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the lab."""
    systemAssignedMIPrincipalId: Output[Literal['string']]
    """The principal ID of the system assigned identity."""
    uniqueIdentifier: Output[Literal['string']]
    """The unique identifier for the lab. Used to track tags that the lab applies to each resource that it creates."""


class DevTestLabModule(Module):
    outputs: DevTestLabOutputs


def _dev_test_lab(
        bicep: IO[str],
        params: DevTestLab,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.4.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> DevTestLabModule:
    symbol = "dev_test_lab_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/dev-test-lab/lab:{tag}' = {{\n")
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
    output = DevTestLabModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
            'systemAssignedMIPrincipalId': Output(symbol, 'systemAssignedMIPrincipalId', 'string'),
            'uniqueIdentifier': Output(symbol, 'uniqueIdentifier', 'string'),
        }

    return output
