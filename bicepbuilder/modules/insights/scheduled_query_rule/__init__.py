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


class ScheduledQueryRule(TypedDict, total=False):
    """"""
    criterias: Required[Dict[str, object]]
    """The rule criteria that defines the conditions of the scheduled query rule."""
    name: Required[str]
    """The name of the Alert."""
    scopes: Required[List[object]]
    """The list of resource IDs that this scheduled query rule is scoped to."""
    windowSize: str
    """The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Required if the kind is set to 'LogAlert', otherwise not relevant."""
    actions: List[object]
    """Actions to invoke when the alert fires."""
    alertDescription: str
    """The description of the scheduled query rule."""
    alertDisplayName: str
    """The display name of the scheduled query rule."""
    autoMitigate: bool
    """The flag that indicates whether the alert should be automatically resolved or not. Relevant only for rules of the kind LogAlert."""
    enabled: bool
    """The flag which indicates whether this scheduled query rule is enabled."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    evaluationFrequency: str
    """How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert."""
    kind: Literal['LogAlert', 'LogToMetric']
    """Indicates the type of scheduled query rule."""
    location: str
    """Location for all resources."""
    queryTimeRange: str
    """If specified (in ISO 8601 duration format) then overrides the query time range. Relevant only for rules of the kind LogAlert."""
    ruleResolveConfiguration: Dict[str, object]
    """Defines the configuration for resolving fired alerts. Relevant only for rules of the kind LogAlert."""
    severity: Literal[0, 1, 2, 3, 4]
    """Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert."""
    skipQueryValidation: bool
    """The flag which indicates whether the provided query should be validated or not. Relevant only for rules of the kind LogAlert."""
    suppressForMinutes: str
    """Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. If set, autoMitigate must be disabled.Relevant only for rules of the kind LogAlert."""
    tags: Dict[str, object]
    """Tags of the resource."""
    targetResourceTypes: List[object]
    """List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert."""


class ScheduledQueryRuleOutputs(TypedDict, total=False):
    """Outputs for ScheduledQueryRule"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The Name of the created scheduled query rule."""
    resourceGroupName: Output[Literal['string']]
    """The Resource Group of the created scheduled query rule."""
    resourceId: Output[Literal['string']]
    """The resource ID of the created scheduled query rule."""


class ScheduledQueryRuleBicep(Module):
    outputs: ScheduledQueryRuleOutputs


def scheduled_query_rule(
        bicep: IO[str],
        /,
        *,
        params: ScheduledQueryRule,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'insights/scheduled-query-rule',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> ScheduledQueryRuleBicep:
    symbol = "scheduled_query_rule_" + generate_suffix()
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
    output = ScheduledQueryRuleBicep(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
