from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    ResourceId,
    ResourceName,
    Deployment,
    Output,
)


class Parameter(TypedDict, total=False):
    """The parameters that this custom action uses."""
    name: Required[str]
    """The name of the parameter."""
    defaultValue: str
    """The default value of the parameter. Only applies to string types."""
    description: str
    """A description to help users understand what this parameter means."""
    required: bool
    """Indicates whether this parameter must be passed when running the custom action."""
    type: Literal['ConfigurationDataBlob', 'LogOutputBlob', 'String']
    """Specifies the type of the custom action parameter."""


class CustomAction(TypedDict, total=False):
    """A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application."""
    name: Required[str]
    """The name of the custom action. Must be unique within the Gallery Application Version."""
    script: Required[str]
    """The script to run when executing this custom action."""
    description: str
    """Description to help the users understand what this custom action does."""
    parameters: List['Parameter']
    """The parameters that this custom action uses."""


class RoleAssignment(TypedDict, total=False):
    """Array of role assignments to create."""
    principalId: Required[str]
    """The principal ID of the principal (user/group/identity) to assign the role to."""
    roleDefinitionIdOrName: Required[Union[str, Literal['Compute Gallery Sharing Admin', 'Contributor', 'Owner', 'Reader', 'Role Based Access Control Administrator', 'User Access Administrator']]]
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


class Application(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the application definition."""
    supportedOSType: Required[Literal['Linux', 'Windows']]
    """This property allows you to specify the supported type of the OS that application is built for."""
    customActions: List['CustomAction']
    """A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application."""
    description: str
    """The description of this gallery Application Definition resource. This property is updatable."""
    endOfLifeDate: str
    """The end of life date of the gallery Image Definition. This property can be used for decommissioning purposes. This property is updatable. Allowed format: 2020-01-10T23:00:00.000Z."""
    eula: str
    """The Eula agreement for the gallery Application Definition. Has to be a valid URL."""
    location: str
    """Location for all resources."""
    privacyStatementUri: str
    """The privacy statement uri. Has to be a valid URL."""
    releaseNoteUri: str
    """The release note uri. Has to be a valid URL."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""
    tags: Dict[str, object]
    """Tags for all resources."""


class ApplicationOutputs(TypedDict, total=False):
    """Outputs for Application"""
    location: Output[Literal['string']]
    """The location the resource was deployed into."""
    name: Output[Literal['string']]
    """The name of the image."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the image was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the image."""


class ApplicationBicep(Module):
    outputs: ApplicationOutputs

