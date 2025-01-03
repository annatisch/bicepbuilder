from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ....expressions import (
    BicepExpression,
    Module,
    Output,
)


class KubernetesConfigurationFluxConfiguration(TypedDict, total=False):
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


class KubernetesConfigurationFluxConfigurationOutputs(TypedDict, total=False):
    """Outputs for KubernetesConfigurationFluxConfiguration"""
    name: Output[Literal['string']]
    """The name of the flux configuration."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the flux configuration was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the flux configuration."""


class KubernetesConfigurationFluxConfigurationModule(Module):
    outputs: KubernetesConfigurationFluxConfigurationOutputs

