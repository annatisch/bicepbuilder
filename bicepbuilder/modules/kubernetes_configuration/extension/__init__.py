from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ...._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class KubernetesConfigurationExtension(TypedDict, total=False):
    """"""
    clusterName: Required[str]
    """The name of the AKS cluster that should be configured."""
    extensionType: Required[str]
    """Type of the extension, of which this resource is an instance of. It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the extension publisher."""
    name: Required[str]
    """The name of the Flux Configuration."""
    configurationProtectedSettings: Dict[str, object]
    """Configuration settings that are sensitive, as name-value pairs for configuring this extension."""
    configurationSettings: Dict[str, object]
    """Configuration settings, as name-value pairs for configuring this extension."""
    enableTelemetry: bool
    """Enable/Disable usage telemetry for module."""
    fluxConfigurations: List[object]
    """A list of flux configuraitons."""
    location: str
    """Location for all resources."""
    releaseNamespace: str
    """Namespace where the extension Release must be placed, for a Cluster scoped extension. If this namespace does not exist, it will be created."""
    releaseTrain: str
    """ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is "true"."""
    targetNamespace: str
    """Namespace where the extension will be created for an Namespace scoped extension. If this namespace does not exist, it will be created."""
    version: str
    """Version of the extension for this extension, if it is "pinned" to a specific version."""


class KubernetesConfigurationExtensionOutputs(TypedDict, total=False):
    """Outputs for KubernetesConfigurationExtension"""
    name: Output[Literal['string']]
    """The name of the extension."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the extension was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the extension."""


class KubernetesConfigurationExtensionBicep(Module):
    outputs: KubernetesConfigurationExtensionOutputs


def kubernetes_configuration_extension(
        bicep: IO[str],
        params: KubernetesConfigurationExtension,
        /,
        *,
        scope: Optional[BicepExpression] = None,
        depends_on: Optional[Union[str, BicepExpression]] = None,
        tag: str = '0.3.0',
        batch_size: Optional[int] = None,
        description: Optional[str] = None,
) -> KubernetesConfigurationExtensionBicep:
    symbol = "kubernetes_configuration_extension_" + generate_suffix()
    name = Deployment().name.format(suffix="_" + symbol)
    if description:
        bicep.write(f"@description('{description}')\n")
    if batch_size:
        bicep.write(f"@batchSize({batch_size})\n")
    bicep.write(f"module {symbol} 'br/public:avm/res/kubernetes-configuration/extension:{tag}' = {{\n")
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
    output = KubernetesConfigurationExtensionBicep(symbol)
    output.outputs = {
            'name': Output(symbol, 'name', 'string'),
            'resourceGroupName': Output(symbol, 'resourceGroupName', 'string'),
            'resourceId': Output(symbol, 'resourceId', 'string'),
        }

    return output
