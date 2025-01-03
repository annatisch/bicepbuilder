from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConsumptionBudget(TypedDict, total=False):
    """"""
    amount: Required[int]
    """The total amount of cost or usage to track with the budget."""
    name: Required[str]
    """The name of the budget."""
    actionGroups: List[object]
    """List of action group resource IDs that will receive the alert. Required if neither """
    contactEmails: List[object]
    """The list of email addresses to send the budget notification to when the thresholds are exceeded. Required if neither """
    contactRoles: List[object]
    """The list of contact roles to send the budget notification to when the thresholds are exceeded. Required if neither """
    category: Literal['Cost', 'Usage']
    """The category of the budget, whether the budget tracks cost or usage."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    endDate: str
    """The end date for the budget. If not provided, it will default to 10 years from the start date."""
    filter: Dict[str, object]
    """The filter to use for restricting which resources are considered within the budget."""
    location: str
    """Location deployment metadata."""
    operator: Literal['EqualTo', 'GreaterThan', 'GreaterThanOrEqualTo']
    """The comparison operator. The operator can be either """
    resetPeriod: Literal['Annually', 'BillingAnnual', 'BillingMonth', 'BillingQuarter', 'Monthly', 'Quarterly']
    """The time covered by a budget. Tracking of the amount will be reset based on the time grain. BillingMonth, BillingQuarter, and BillingAnnual are only supported by WD customers."""
    resourceGroupFilter: List[object]
    """The list of resource groups that contain the resources that are to be considered within the budget."""
    startDate: str
    """The start date for the budget. Start date should be the first day of the month and cannot be in the past (except for the current month)."""
    thresholds: List[object]
    """Percent thresholds of budget for when to get a notification. Can be up to 5 thresholds, where each must be between 1 and 1000."""
    thresholdType: Literal['Actual', 'Forecasted']
    """The type of threshold to use for the budget. The threshold type can be either """


class ConsumptionBudgetOutputs(TypedDict, total=False):
    """Outputs for ConsumptionBudget"""
    name: Output[Literal['string']]
    """The name of the budget."""
    resourceId: Output[Literal['string']]
    """The resource ID of the budget."""
    subscriptionName: Output[Literal['string']]
    """The subscription the budget was deployed into."""


class ConsumptionBudgetModule(Module):
    outputs: ConsumptionBudgetOutputs

