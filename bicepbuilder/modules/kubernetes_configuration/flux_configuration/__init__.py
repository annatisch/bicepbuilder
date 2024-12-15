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


class FluxConfiguration(TypedDict, total=False):
    """"""
    clusterName: Required[str]
    """The name of the AKS cluster that should be configured."""
    kustomizations: Required[Dict[str, object]]
    """Array of kustomizations used to reconcile the artifact pulled by the source type on the cluster."""
    name: Required[str]
    """The name of the Flux Configuration."""
    namespace: Required[str]
    """The namespace to which this configuration is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only."""
    scope: Required[Literal['cluster', 'namespace']]
    """Scope at which the configuration will be installed."""
    sourceKind: Required[Literal['Bucket', 'GitRepository']]
    """Source Kind to pull the configuration data from."""
    bucket: Dict[str, object]
    """Parameters to reconcile to the GitRepository source kind type. Required if """
    gitRepository: Dict[str, object]
    """Parameters to reconcile to the GitRepository source kind type. Required if """
    configurationProtectedSettings: Dict[str, object]
    """Key-value pairs of protected configuration settings for the configuration."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    location: str
    """Location for all resources."""
    suspend: bool
    """Whether this configuration should suspend its reconciliation of its kustomizations and sources."""


class FluxConfigurationOutputs(TypedDict, total=False):
    """Outputs for FluxConfiguration"""
    name: Output[Literal['string']]
    """The name of the flux configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the flux configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the flux configuration."""


class FluxConfigurationBicep(Module):
    outputs: FluxConfigurationOutputs


def flux_configuration(
        bicep: IO[str],
        /,
        *,
        params: FluxConfiguration,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        name: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        registry_prefix: str = 'br/public:avm/res',
        path: str = 'kubernetes-configuration/flux-configuration',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> FluxConfigurationBicep:
    symbol = "flux_configuration_" + generate_suffix()
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
    output = FluxConfigurationBicep(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
