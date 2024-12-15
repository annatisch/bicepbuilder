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

if TYPE_CHECKING:
    from .api import Api
    from .group import Group


class Product(TypedDict, total=False):
    """"""
    displayName: Required[str]
    """API Management Service Products name. Must be 1 to 300 characters long."""
    name: Required[str]
    """Product Name."""
    apis: List['Api']
    """Array of Product APIs."""
    approvalRequired: bool
    """Whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the products APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the products APIs. Can be present only if subscriptionRequired property is present and has a value of false."""
    description: str
    """Product description. May include HTML formatting tags."""
    groups: List['Group']
    """Array of Product Groups."""
    state: str
    """whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished. - notPublished or published."""
    subscriptionRequired: bool
    """Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true."""
    subscriptionsLimit: int
    """Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false."""
    terms: str
    """Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process."""


class ProductOutputs(TypedDict, total=False):
    """Outputs for Product"""
    apiResourceIds: Output[Literal['array']]
    """The Resources IDs of the API management service product APIs."""
    groupResourceIds: Output[Literal['array']]
    """The Resources IDs of the API management service product groups."""
    name: Output[Literal['string']]
    """The name of the API management service product."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the API management service product was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the API management service product."""


class ProductBicep(Module):
    outputs: ProductOutputs

