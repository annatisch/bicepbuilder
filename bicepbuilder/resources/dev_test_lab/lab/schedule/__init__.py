from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class DailyRecurrence(TypedDict, total=False):
    """If the schedule will occur once each day of the week, specify the daily recurrence."""
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
    """"""
    name: Required[Literal['LabVmAutoStart', 'LabVmsShutdown']]
    """The name of the schedule."""
    taskType: Required[Literal['LabVmsShutdownTask', 'LabVmsStartupTask']]
    """The task type of the schedule (e.g. LabVmsShutdownTask, LabVmsStartupTask)."""
    dailyRecurrence: 'DailyRecurrence'
    """If the schedule will occur once each day of the week, specify the daily recurrence."""
    hourlyRecurrence: 'HourlyRecurrence'
    """If the schedule will occur multiple times a day, specify the hourly recurrence."""
    notificationSettings: 'NotificationSetting'
    """The notification settings for the schedule."""
    status: Literal['Disabled', 'Enabled']
    """The status of the schedule (i.e. Enabled, Disabled)."""
    tags: Dict[str, object]
    """Tags of the resource."""
    targetResourceId: str
    """The resource ID to which the schedule belongs."""
    timeZoneId: str
    """The time zone ID (e.g. Pacific Standard time)."""
    weeklyRecurrence: 'WeeklyRecurrence'
    """If the schedule will occur only some days of the week, specify the weekly recurrence."""


class ScheduleOutputs(TypedDict, total=False):
    """Outputs for Schedule"""
    name: Output[Literal['string']]
    """The name of the schedule."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the schedule was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the schedule."""


class ScheduleModule(Module):
    outputs: ScheduleOutputs

