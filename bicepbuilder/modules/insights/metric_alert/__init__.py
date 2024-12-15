from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ..expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


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


class MetricAlert(TypedDict, total=False):
    """"""
    criteria: Required[Dict[str, object]]
    """Maps to the 'odata.type' field. Specifies the type of the alert criteria."""
    name: Required[str]
    """The name of the alert."""
    targetResourceRegion: str
    """The region of the target resource(s) on which the alert is created/updated. Required if alertCriteriaType is MultipleResourceMultipleMetricCriteria."""
    targetResourceType: str
    """The resource type of the target resource(s) on which the alert is created/updated. Required if alertCriteriaType is MultipleResourceMultipleMetricCriteria."""
    actions: List[object]
    """The list of actions to take when alert triggers."""
    alertDescription: str
    """Description of the alert."""
    autoMitigate: bool
    """The flag that indicates whether the alert should be auto resolved or not."""
    enabled: bool
    """Indicates whether this alert is enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    evaluationFrequency: Literal['PT15M', 'PT1H', 'PT1M', 'PT30M', 'PT5M']
    """how often the metric alert is evaluated represented in ISO 8601 duration format."""
    location: str
    """Location for all resources."""
    scopes: List[object]
    """the list of resource IDs that this metric alert is scoped to."""
    severity: Literal[0, 1, 2, 3, 4]
    """The severity of the alert."""
    tags: Dict[str, object]
    """Tags of the resource."""
    windowSize: Literal['P1D', 'PT12H', 'PT15M', 'PT1H', 'PT1M', 'PT30M', 'PT5M', 'PT6H']
    """the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold."""


class MetricAlertOutputs(TypedDict, total=False):
    """Outputs for MetricAlert"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the metric alert."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the metric alert was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the metric alert."""


class MetricAlertBicep(Module):
    outputs: MetricAlertOutputs


def metric_alert(
        bicep: IO[str],
        /,
        *,
        params: MetricAlert,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'insights/metric-alert',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> MetricAlertBicep:
    symbol = "metric_alert_" + generate_suffix()
    name = name or Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} '{registry_prefix}/{path}:{tag}' = {{\n")
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
    output = MetricAlertBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
