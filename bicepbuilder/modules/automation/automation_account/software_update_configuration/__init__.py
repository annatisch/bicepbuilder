from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class SoftwareUpdateConfiguration(TypedDict, total=False):
    """"""
    frequency: Required[Literal['Day', 'Hour', 'Month', 'OneTime', 'Week']]
    """The frequency of the deployment schedule. When using 'Hour', 'Day', 'Week' or 'Month', an interval needs to be provided."""
    name: Required[str]
    """The name of the Deployment schedule."""
    operatingSystem: Required[Literal['Linux', 'Windows']]
    """The operating system to be configured by the deployment schedule."""
    rebootSetting: Required[Literal['Always', 'IfRequired', 'Never', 'RebootOnly']]
    """Reboot setting for the deployment schedule."""
    azureVirtualMachines: List[object]
    """List of azure resource IDs for azure virtual machines in scope for the deployment schedule."""
    excludeUpdates: List[object]
    """KB numbers or Linux packages excluded in the deployment schedule."""
    expiryTime: str
    """The end time of the deployment schedule in ISO 8601 format. YYYY-MM-DDTHH:MM:SS, 2021-12-31T23:00:00."""
    expiryTimeOffsetMinutes: int
    """The expiry time's offset in minutes."""
    includeUpdates: List[object]
    """KB numbers or Linux packages included in the deployment schedule."""
    interval: int
    """The interval of the frequency for the deployment schedule. 1 Hour is every hour, 2 Day is every second day, etc."""
    isEnabled: bool
    """Enables the deployment schedule."""
    maintenanceWindow: str
    """Maximum time allowed for the deployment schedule to run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601."""
    monthDays: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    """Can be used with frequency 'Month'. Provides the specific days of the month to run the deployment schedule."""
    monthlyOccurrences: List[object]
    """Can be used with frequency 'Month'. Provides the pattern/cadence for running the deployment schedule in a month. Takes objects formed like this {occurance(int),day(string)}. Day is the name of the day to run the deployment schedule, the occurance specifies which occurance of that day to run the deployment schedule."""
    nextRun: str
    """The next time the deployment schedule runs in ISO 8601 format. YYYY-MM-DDTHH:MM:SS, 2021-12-31T23:00:00."""
    nextRunOffsetMinutes: int
    """The next run's offset in minutes."""
    nonAzureComputerNames: List[object]
    """List of names of non-azure machines in scope for the deployment schedule."""
    nonAzureQueries: List[object]
    """Array of functions from a Log Analytics workspace, used to scope the deployment schedule."""
    postTaskParameters: Dict[str, object]
    """Parameters provided to the task running after the deployment schedule."""
    postTaskSource: str
    """The source of the task running after the deployment schedule."""
    preTaskParameters: Dict[str, object]
    """Parameters provided to the task running before the deployment schedule."""
    preTaskSource: str
    """The source of the task running before the deployment schedule."""
    scheduleDescription: str
    """The schedules description."""
    scopeByLocations: List[object]
    """Specify locations to which to scope the deployment schedule to."""
    scopeByResources: List[object]
    """Specify the resources to scope the deployment schedule to."""
    scopeByTags: Dict[str, object]
    """Specify tags to which to scope the deployment schedule to."""
    scopeByTagsOperation: Literal['All', 'Any']
    """Enables the scopeByTags to require All (Tag A and Tag B) or Any (Tag A or Tag B)."""
    startTime: str
    """The start time of the deployment schedule in ISO 8601 format. To specify a specific time use YYYY-MM-DDTHH:MM:SS, 2021-12-31T23:00:00. For schedules where we want to start the deployment as soon as possible, specify the time segment only in 24 hour format, HH:MM, 22:00."""
    timeZone: str
    """Time zone for the deployment schedule. IANA ID or a Windows Time Zone ID."""
    updateClassifications: Literal['Critical', 'Definition', 'FeaturePack', 'Other', 'Security', 'ServicePack', 'Tools', 'UpdateRollup', 'Updates']
    """Update classification included in the deployment schedule."""
    weekDays: Literal['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    """Required when used with frequency 'Week'. Specified the day of the week to run the deployment schedule."""
    baseTime: str
    """Do not touch. Is used to provide the base time for time comparison for startTime. If startTime is specified in HH:MM format, baseTime is used to check if the provided startTime has passed, adding one day before setting the deployment schedule."""


class SoftwareUpdateConfigurationOutputs(TypedDict, total=False):
    """Outputs for SoftwareUpdateConfiguration"""
    name: Output[Literal['string']]
    """The name of the deployed softwareUpdateConfiguration."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed softwareUpdateConfiguration."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed softwareUpdateConfiguration."""


class SoftwareUpdateConfigurationBicep(Module):
    outputs: SoftwareUpdateConfigurationOutputs

