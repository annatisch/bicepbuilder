from typing import Self, Optional, IO, Literal, List, Dict, Any, Union, overload
import os
import json

from ._utils import serialize
from .expressions import BicepExpression, ResourceGroup, Subscription
from .modules import AddResourceMixin


class infra(AddResourceMixin):
    scope: BicepExpression
    bicep: Optional[IO[str]]

    def __init__(
            self,
            *,
            dir: str = ".",
            infra: str = "infra",
            module: str = "main",
            metadata: Optional[Dict[str, str]] = None,
            scope: Optional[Literal["resourceGroup", "subscription", "tenant", "managementGroup"]] = "subscription",
    ) -> None:
        self._metadata = metadata or {}
        self._target_scope = scope
        if scope is None or scope == "resourceGroup":
            self.scope = ResourceGroup()
        elif scope == "subscription":
            self.scope = Subscription()
        else:
            raise NotImplementedError("tenant and managementGroup scopes not supported yet.")
        
        self._output_dir = os.path.join(os.path.abspath(os.curdir()), infra)
        self._main_module_file = os.path.join(self._output_dir, module + ".bicep")
        self._main_params_file = os.path.join(self._output_dir, module + ".json")
        self.bicep = None
        self._params : Optional[IO[str]] = None

    def __enter__(self) -> 'infra':
        self._main = open(self._main_module_file, 'w')
        for key, value in self._metadata.items():
            self.bicep.write(f"metadata {key} '{value}'\n")
        if self._target_scope:
            self.bicep.write(f"targetScope = '{self._scope}'\n\n")
        self._params = open(self._main_params_file, 'w')

    @overload
    def param(
            self,
            name: str,
            type: Literal["string"],
            *,
            default: Optional[Union[BicepExpression, str]] = None,
            secure: bool = False,
            description: Optional[str] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
            allowed: Optional[List[str]] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["int"],
            *,
            default: Optional[Union[BicepExpression, int]] = None,
            description: Optional[str] = None,
            allowed: Optional[List[int]] = None,
            max_value: Optional[int] = None,
            min_value: Optional[int] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["bool"],
            *,
            default: Optional[Union[BicepExpression, bool]] = None,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["array"],
            *,
            default: Optional[Union[BicepExpression, List[Any]]] = None,
            description: Optional[str] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["object"],
            *,
            default: Optional[Union[BicepExpression, Dict[str, Any]]] = None,
            secure: bool = False,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    def param(
            self,
            name: str,
            type: str,
            *,
            default: Optional[Any] = None,
            secure: bool = False,
            description: Optional[str] = None,
            allowed: Optional[List[int]] = None,
            max_value: Optional[int] = None,
            min_value: Optional[int] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
    ) -> BicepExpression:
        if secure:
            self.bicep.write("@sys.secure()\n")
        if description:
            self.bicep.write(f"@sys.description('{description}')\n")
        if allowed:
            self.bicep.write("@sys.allowed([\n")
            for value in allowed:
                self.bicep.write(f"  {json.dumps(value)}\n")
            self.bicep.write("])\n")
        if max_value is not None:
            self.bicep.write(f"@sys.maxValue({max_value})\n")
        if min_value is not None:
            self.bicep.write(f"@sys.minValue({min_value})\n")
        if max_length is not None:
            self.bicep.write(f"@sys.maxLength({max_length})\n")
        if min_length is not None:
            self.bicep.write(f"@sys.minLength({max_length})\n")
        self.bicep.write(f"param {name} {type}")
        if default is not None:
            self.bicep.write(" = ")
            serialize(self._main, default)
        else:
            self.bicep.write("\n")
        self.bicep.write("\n")

    def comment(self, comment: str) -> None:
        self.bicep.write(f"// {comment}\n")

    def var(self, name: str, value: Any, *, description: Optional[str] = None) -> BicepExpression:
        if description:
            self.bicep.write(f"@sys.description('{description}')\n")
        self.bicep.write(f"var {name} = ")
        serialize(self._main, value)
        self.bicep.write("\n")

    def module(
            self,
            path: str,
            params: Dict[str, Any],
            /,
            *,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            name: Optional[str] = None,
            tag: Optional[str] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> StorageAccountBicep:
        ...

    def __exit__(self, *args) -> None:
        self.bicep.close()
        self._params.close()
