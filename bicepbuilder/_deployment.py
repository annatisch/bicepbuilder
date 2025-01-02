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
