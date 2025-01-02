from typing import Self, Optional, IO, Literal, List, Dict, Any, Union, overload
import os
import json

from ._utils import serialize
from ._writer import BicepWriter
from .expressions import BicepExpression, Subscription, Module, ResourceGroup
from .modules import ResourceGroup as ResourceGroupParams


class infra(BicepWriter):
    scope: BicepExpression
    bicep: IO[str]

    def __init__(
            self,
            *,
            dir: str = ".",
            infra: str = "infra",
            module: str = "main",
            metadata: Optional[Dict[str, str]] = None,
            scope: Optional[Literal["resourceGroup", "subscription", "tenant", "managementGroup"]] = "subscription",
    ) -> None:
        #self._metadata = metadata or {}
        self._target_scope = scope
        if scope is None or scope == "resourceGroup":
            self.scope = ResourceGroup()
        elif scope == "subscription":
            self.scope = Subscription()
        else:
            raise NotImplementedError("tenant and managementGroup scopes not supported yet.")
        super().__init__(
            module_path=os.path.join(os.path.abspath(os.curdir), infra),
            module_name=module,
            params=True,
            metadata=metadata
        )

    def __enter__(self) -> 'infra':
        super().__enter__()
        if self._target_scope:
            self._bicep.write(f"targetScope = '{self._target_scope}'\n\n")
        return self

    @overload
    def resource_group(
            self,
            *,
            name: Union[str, BicepExpression],
            location: Union[str, BicepExpression],
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None,
            scope: Optional[BicepExpression] = None
    ) -> ResourceGroup:
        ...
    @overload
    def resource_group(
            self,
            *,
            existing: Union[str, BicepExpression],
            scope: Optional[BicepExpression] = None,
            version: Optional[str] = None,
    ) -> ResourceGroup:
        ...
    def resource_group(
            self,
            *,
            name: Optional[Union[str, BicepExpression]] = None,
            location: Optional[Union[str, BicepExpression]] = None,
            existing: Optional[Union[str, BicepExpression]] = None,
            scope: Optional[BicepExpression] = None,
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None
    ) -> ResourceGroup:
        if existing:
            self.resource()
        params: ResourceGroupParams = {
            'name': name,
            'location': location
        }
        if tags:
            params['tags'] = tags
        rg_bicep = self.add('resource_group', params, scope=scope or self.scope)
        return ResourceGroup(rg_bicep.name)