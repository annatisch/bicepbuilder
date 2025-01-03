from typing import TYPE_CHECKING, TypedDict, Literal, List, Dict, Union
from typing_extensions import Required

from .....expressions import (
    BicepExpression,
    Module,
    Output,
)

if TYPE_CHECKING:
    from .container import Container


class SqlDatabase(TypedDict, total=False):
    """"""
    name: Required[str]
    """Name of the SQL database ."""
    autoscaleSettingsMaxThroughput: int
    """Specifies the Autoscale settings and represents maximum throughput, the resource can scale up to.  The autoscale throughput should have valid throughput values between 1000 and 1000000 inclusive in increments of 1000. If value is set to null, then autoscale will be disabled."""
    containers: List['Container']
    """Array of containers to deploy in the SQL database."""
    tags: Dict[str, object]
    """Tags of the SQL database resource."""
    throughput: int
    """Request units per second. Will be ignored if autoscaleSettingsMaxThroughput is used."""


class SqlDatabaseOutputs(TypedDict, total=False):
    """Outputs for SqlDatabase"""
    name: Output[Literal['string']]
    """The name of the SQL database."""
    resourceGroupName: Output[Literal['string']]
    """The name of the resource group the SQL database was created in."""
    resourceId: Output[Literal['string']]
    """The resource ID of the SQL database."""


class SqlDatabaseModule(Module):
    outputs: SqlDatabaseOutputs

