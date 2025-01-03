from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class SecurityAlertPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the security alert policy."""
    emailAccountAdmins: bool
    """Specifies that the schedule scan notification will be is sent to the subscription administrators."""
    state: Literal['Disabled', 'Enabled']
    """Enables advanced data security features, like recuring vulnerability assesment scans and ATP. If enabled, storage account must be provided."""


class SecurityAlertPolicyOutputs(TypedDict, total=False):
    """Outputs for SecurityAlertPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed security alert policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed security alert policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed security alert policy."""


class SecurityAlertPolicyModule(Module):
    outputs: SecurityAlertPolicyOutputs

