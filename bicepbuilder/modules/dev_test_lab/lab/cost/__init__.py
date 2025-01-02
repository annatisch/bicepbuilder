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


class Cost(TypedDict, total=False):
    """"""
    cycleType: Required[Literal['CalendarMonth', 'Custom']]
    """Reporting cycle type."""
    cycleEndDateTime: str
    """Reporting cycle end date in the zulu time format (e.g. 2023-12-01T00:00:00.000Z). Required if cycleType is set to "Custom"."""
    cycleStartDateTime: str
    """Reporting cycle start date in the zulu time format (e.g. 2023-12-01T00:00:00.000Z). Required if cycleType is set to "Custom"."""
    currencyCode: str
    """The currency code of the cost."""
    status: Literal['Disabled', 'Enabled']
    """Target cost status."""
    tags: Dict[str, object]
    """Tags of the resource."""
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


class CostOutputs(TypedDict, total=False):
    """Outputs for Cost"""
    name: Output[Literal['string']]
    """The name of the cost."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the cost was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the cost."""


class CostBicep(Module):
    outputs: CostOutputs

