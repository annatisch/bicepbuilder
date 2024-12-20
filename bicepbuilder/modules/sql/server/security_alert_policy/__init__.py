from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class SecurityAlertPolicy(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the Security Alert Policy."""
    disabledAlerts: Literal['Access_Anomaly', 'Brute_Force', 'Data_Exfiltration', 'Sql_Injection', 'Sql_Injection_Vulnerability', 'Unsafe_Action']
    """Alerts to disable."""
    emailAccountAdmins: bool
    """Specifies that the alert is sent to the account administrators."""
    emailAddresses: List[object]
    """Specifies an array of email addresses to which the alert is sent."""
    retentionDays: int
    """Specifies the number of days to keep in the Threat Detection audit logs."""
    state: Literal['Disabled', 'Enabled']
    """Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database."""
    storageAccountAccessKey: str
    """Specifies the identifier key of the Threat Detection audit storage account."""
    storageEndpoint: str
    """Specifies the blob storage endpoint. This blob storage will hold all Threat Detection audit logs."""


class SecurityAlertPolicyOutputs(TypedDict, total=False):
    """Outputs for SecurityAlertPolicy"""
    name: Output[Literal['string']]
    """The name of the deployed security alert policy."""
    resourceGroupName: Output[Literal['string']]
    """The resource group of the deployed security alert policy."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed security alert policy."""


class SecurityAlertPolicyBicep(Module):
    outputs: SecurityAlertPolicyOutputs

