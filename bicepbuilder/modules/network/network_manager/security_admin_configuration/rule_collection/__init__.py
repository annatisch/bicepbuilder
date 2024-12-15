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


class AppliesToGroup(TypedDict, total=False):
    """List of network groups for configuration. An admin rule collection must be associated to at least one network group."""
    networkGroupResourceId: Required[str]
    """The resource ID of the network group."""


class Rule(TypedDict, total=False):
    """List of rules for the admin rules collection. Security admin rules allows enforcing security policy criteria that matches the conditions set. Warning: A rule collection without rule will cause a deployment configuration for security admin goal state in network manager to fail."""
    access: Required[Literal['Allow', 'AlwaysAllow', 'Deny']]
    """Indicates the access allowed for this particular rule. "Allow" means traffic matching this rule will be allowed. "Deny" means traffic matching this rule will be blocked. "AlwaysAllow" means that traffic matching this rule will be allowed regardless of other rules with lower priority or user-defined NSGs."""
    direction: Required[Literal['Inbound', 'Outbound']]
    """Indicates if the traffic matched against the rule in inbound or outbound."""
    name: Required[str]
    """The name of the rule."""
    priority: Required[int]
    """The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule."""
    protocol: Required[Literal['Ah', 'Any', 'Esp', 'Icmp', 'Tcp', 'Udp']]
    """Network protocol this rule applies to."""
    description: str
    """A description of the rule."""
    destinationPortRanges: List[object]
    """List of destination port ranges. This specifies on which ports traffic will be allowed or denied by this rule. Provide an (*) to allow traffic on any port. Port ranges are between 1-65535."""
    sourcePortRanges: List[object]
    """List of destination port ranges. This specifies on which ports traffic will be allowed or denied by this rule. Provide an (*) to allow traffic on any port. Port ranges are between 1-65535."""


class Destination(TypedDict, total=False):
    """The destnations filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""
    addressPrefix: Required[str]
    """Address prefix."""
    addressPrefixType: Required[Literal['IPPrefix', 'ServiceTag']]
    """Address prefix type."""


class Source(TypedDict, total=False):
    """The source filter can be an IP Address or a service tag. Each filter contains the properties AddressPrefixType (IPPrefix or ServiceTag) and AddressPrefix (using CIDR notation (e.g. 192.168.99.0/24 or 2001:1234::/64) or a service tag (e.g. AppService.WestEurope)). Combining CIDR and Service tags in one rule filter is not permitted."""
    addressPrefix: Required[str]
    """Address prefix."""
    addressPrefixType: Required[Literal['IPPrefix', 'ServiceTag']]
    """Address prefix type."""


class RuleCollection(TypedDict, total=False):
    """"""
    name: Required[str]
    """The name of the admin rule collection."""
    description: str
    """A description of the admin rule collection."""


class RuleCollectionOutputs(TypedDict, total=False):
    """Outputs for RuleCollection"""
    name: Output[Literal['string']]
    """The name of the deployed admin rule collection."""
    resourceGroupName: Output[Literal['string']]
    """The resource group the admin rule collection was deployed into."""
    resourceId: Output[Literal['string']]
    """The resource ID of the deployed admin rule collection."""


class RuleCollectionBicep(Module):
    outputs: RuleCollectionOutputs

