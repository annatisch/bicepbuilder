from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ......expressions import (
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
    roleDefinitionIdOrName: Required[Union[str, Literal['Azure Resource Notifications System Topics Subscriber', 'Contributor', 'EventGrid Contributor', 'EventGrid Data Contributor', 'EventGrid Data Receiver', 'EventGrid Data Sender', 'EventGrid EventSubscription Contributor', 'EventGrid EventSubscription Reader', 'EventGrid TopicSpaces Publisher', 'EventGrid TopicSpaces Subscriber', 'Owner', 'Reader', 'User Access Administrator']]]
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


class EventSubscription(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the Event Subscription to create."""
    deliveryConfiguration: Dict[str, object]
    """Information about the delivery configuration of the Event Subscription."""
    eventDeliverySchema: str
    """The event delivery schema for the Event Subscription."""
    filtersConfiguration: Dict[str, object]
    """Information about the filter for the Event Subscription."""
    roleAssignments: List['RoleAssignment']
    """Array of role assignments to create."""


class EventSubscriptionOutputs(TypedDict, total=False):
    """Outputs for EventSubscription"""
    name: Output[Literal['string']]
    """The name of the Event Subscription."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the Event Subscription was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the Event Subscription."""


class EventSubscriptionBicep(Module):
    outputs: EventSubscriptionOutputs

