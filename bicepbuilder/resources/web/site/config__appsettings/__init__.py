from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)


class ConfigAppsetting(TypedDict, total=False):
    """"""
    kind: Required[Literal['api', 'app', 'app,container,windows', 'app,linux', 'app,linux,container', 'functionapp', 'functionapp,linux', 'functionapp,linux,container', 'functionapp,linux,container,azurecontainerapps', 'functionapp,workflowapp', 'functionapp,workflowapp,linux', 'linux,api']]
    """Type of site to deploy."""
    appInsightResourceId: str
    """Resource ID of the app insight to leverage for this resource."""
    appSettingsKeyValuePairs: Dict[str, object]
    """The app settings key-value pairs except for AzureWebJobsStorage, AzureWebJobsDashboard, APPINSIGHTS_INSTRUMENTATIONKEY and APPLICATIONINSIGHTS_CONNECTION_STRING."""
    currentAppSettings: Dict[str, object]
    """The current app settings."""
    storageAccountResourceId: str
    """Required if app of kind functionapp. Resource ID of the storage account to manage triggers and logging function executions."""
    storageAccountUseIdentityAuthentication: bool
    """If the provided storage account requires Identity based authentication ('allowSharedKeyAccess' is set to false). When set to true, the minimum role assignment required for the App Service Managed Identity to the storage account is 'Storage Blob Data Owner'."""


class ConfigAppsettingOutputs(TypedDict, total=False):
    """Outputs for ConfigAppsetting"""
    name: Output[Literal['string']]
    """The name of the site config."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the site config was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the site config."""


class ConfigAppsettingModule(Module):
    outputs: ConfigAppsettingOutputs

