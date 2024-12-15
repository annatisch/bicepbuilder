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


class AccessPolicy(TypedDict, total=False):
    """An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID."""


class Permission(TypedDict, total=False):
    """Permissions the identity has for keys, secrets and certificates."""
    certificates: Literal['all', 'backup', 'create', 'delete', 'deleteissuers', 'get', 'getissuers', 'import', 'list', 'listissuers', 'managecontacts', 'manageissuers', 'purge', 'recover', 'restore', 'setissuers', 'update']
    """Permissions to certificates."""
    keys: Literal['all', 'backup', 'create', 'decrypt', 'delete', 'encrypt', 'get', 'getrotationpolicy', 'import', 'list', 'purge', 'recover', 'release', 'restore', 'rotate', 'setrotationpolicy', 'sign', 'unwrapKey', 'update', 'verify', 'wrapKey']
    """Permissions to keys."""
    secrets: Literal['all', 'backup', 'delete', 'get', 'list', 'purge', 'recover', 'restore', 'set']
    """Permissions to secrets."""
    storage: Literal['all', 'backup', 'delete', 'deletesas', 'get', 'getsas', 'list', 'listsas', 'purge', 'recover', 'regeneratekey', 'restore', 'set', 'setsas', 'update']
    """Permissions to storage accounts."""


class AccessPolicy(TypedDict, total=False):
    """"""
    objectId: Required[str]
    """The object ID of a user, service principal or security group in the tenant for the vault."""
    applicationId: str
    """Application ID of the client making request on behalf of a principal."""
    tenantId: str
    """The tenant ID that is used for authenticating requests to the key vault."""


class AccessPolicyOutputs(TypedDict, total=False):
    """Outputs for AccessPolicy"""
    name: Output[Literal['string']]
    """The name of the access policies assignment."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the access policies assignment was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the access policies assignment."""


class AccessPolicyBicep(Module):
    outputs: AccessPolicyOutputs

