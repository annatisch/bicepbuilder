from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from ......expressions import (
    BicepExpression,
    Module,
    Output,
)


class Container(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the container."""
    paths: Required[List[object]]
    """List of paths using which data within the container can be partitioned. For kind=MultiHash it can be up to 3. For anything else it needs to be exactly 1."""
    analyticalStorageTtl: int
    """Default to 0. Indicates how long data should be retained in the analytical store, for a container. Analytical store is enabled when ATTL is set with a value other than 0. If the value is set to -1, the analytical store retains all historical data, irrespective of the retention of the data in the transactional store."""
    autoscaleSettingsMaxThroughput: int
    """Specifies the Autoscale settings and represents maximum throughput, the resource can scale up to. The autoscale throughput should have valid throughput values between 1000 and 1000000 inclusive in increments of 1000. If value is set to null, then autoscale will be disabled."""
    conflictResolutionPolicy: Dict[str, object]
    """The conflict resolution policy for the container. Conflicts and conflict resolution policies are applicable if the Azure Cosmos DB account is configured with multiple write regions."""
    defaultTtl: int
    """Default to -1. Default time to live (in seconds). With Time to Live or TTL, Azure Cosmos DB provides the ability to delete items automatically from a container after a certain time period. If the value is set to "-1", it is equal to infinity, and items don't expire by default."""
    indexingPolicy: Dict[str, object]
    """Indexing policy of the container."""
    kind: Literal['Hash', 'MultiHash']
    """Default to Hash. Indicates the kind of algorithm used for partitioning."""
    tags: Dict[str, object]
    """Tags of the SQL Database resource."""
    throughput: int
    """Default to 400. Request Units per second. Will be ignored if autoscaleSettingsMaxThroughput is used."""
    uniqueKeyPolicyKeys: List[object]
    """The unique key policy configuration containing a list of unique keys that enforces uniqueness constraint on documents in the collection in the Azure Cosmos DB service."""
    version: Literal[1, 2]
    """Default to 1 for Hash and 2 for MultiHash - 1 is not allowed for MultiHash. Version of the partition key definition."""


class ContainerOutputs(TypedDict, total=False):
    """Outputs for Container"""
    name: Output[Literal['string']]
    """The name of the container."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the container was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the container."""


class ContainerModule(Module):
    outputs: ContainerOutputs

