from typing import TYPE_CHECKING, IO, TypedDict, Literal, List, Dict, Union, Optional
from typing_extensions import Required

from ..._utils import (
    generate_suffix,
    resolve_value,
    resolve_key,
    serialize_dict,
    serialize_list,
)
from ...expressions import (
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


class Key(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the key."""
    attributesEnabled: bool
    """Determines whether the object is enabled."""
    attributesExp: int
    """Expiry date in seconds since 1970-01-01T00:00:00Z. For security reasons, it is recommended to set an expiration date whenever possible."""
    attributesNbf: int
    """Not before date in seconds since 1970-01-01T00:00:00Z."""
    curveName: Literal['P-256', 'P-256K', 'P-384', 'P-521']
    """The elliptic curve name."""
    keyOps: Literal['decrypt', 'encrypt', 'import', 'sign', 'unwrapKey', 'verify', 'wrapKey']
    """Array of JsonWebKeyOperation."""
    keySize: int
    """The key size in bits. For example: 2048, 3072, or 4096 for RSA."""
    kty: Literal['EC', 'EC-HSM', 'RSA', 'RSA-HSM']
    """The type of the key."""
    releasePolicy: Dict[str, object]
    """Key release policy."""
    rotationPolicy: Dict[str, object]
    """Key rotation policy properties object."""
    tags: Dict[str, object]
    """Resource tags."""


class KeyOutputs(TypedDict, total=False):
    """Outputs for Key"""
    keyUri: Output[Literal['string']]
    """The uri of the key."""
    keyUriWithVersion: Output[Literal['string']]
    """The uri with version of the key."""
    name: Output[Literal['string']]
    """The name of the key."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the key was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the key."""


class KeyBicep(Module):
    outputs: KeyOutputs

