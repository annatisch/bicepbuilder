from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
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


class KubernetesConfigurationExtensionModule(Module):
    outputs: KubernetesConfigurationExtensionOutputs

