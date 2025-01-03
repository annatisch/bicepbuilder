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


class Lock(TypedDict, total=False):
    """The lock settings of the service."""
    kind: Literal['CanNotDelete', 'None', 'ReadOnly']
    """Specify the type of lock."""
    name: str
    """Specify the name of lock."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class InsightsWebtest(TypedDict, total=False):
    """"""
    appInsightResourceId: Required[str]
    """Resource ID of the App Insights resource to link with this webtest."""
    name: Required[str]
    """Name of the webtest."""
    request: Required[Dict[str, object]]
    """The collection of request properties."""
    webTestName: Required[str]
    """User defined name if this WebTest."""
    configuration: Dict[str, object]
    """An XML configuration specification for a WebTest."""
    description: str
    """User defined description for this WebTest."""
    enabled: bool
    """Is the test actively being monitored."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    frequency: int
    """Interval in seconds between test runs for this WebTest."""
    kind: Literal['multistep', 'ping', 'standard']
    """The kind of WebTest that this web test watches."""
    location: str
    """Location for all Resources."""
    locations: List[object]
    """List of where to physically run the tests from to give global coverage for accessibility of your application."""
    lock: 'Lock'
    """The lock settings of the service."""
    retryEnabled: bool
    """Allow for retries should this WebTest fail."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    syntheticMonitorId: str
    """Unique ID of this WebTest."""
    tags: Dict[str, object]
    """Resource tags. Note: a mandatory tag 'hidden-link' based on the 'appInsightResourceId' parameter will be automatically added to the tags defined here."""
    timeout: int
    """Seconds until this WebTest will timeout and fail."""
    validationRules: Dict[str, object]
    """The collection of validation rule properties."""


class InsightsWebtestOutputs(TypedDict, total=False):
    """Outputs for InsightsWebtest"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the webtest."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the resource was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the webtest."""


class InsightsWebtestModule(Module):
    outputs: InsightsWebtestOutputs


def _insights_webtest(
        bicep: IO[str],
        params: InsightsWebtest,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> InsightsWebtestModule:
    symbol = "insights_webtest_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/insights/webtest:{tag}' = {{\n")
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
    output = InsightsWebtestModule(symbol)
    output.outputs = {
            'location': Output(symbol, 'location', 'string'),
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
