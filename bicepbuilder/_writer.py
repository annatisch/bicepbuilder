from typing import Self, Optional, IO, Literal, List, Dict, Any, Union, overload
import os
import json

from ._utils import serialize
from .expressions import BicepExpression, Module
from .modules import AddResourceMixin


class BicepWriter(AddResourceMixin):
    bicep: IO[str]

    def __init__(
            self,
            module_path: str,
            params_path: Optional[str] = None,
            *,
            metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        self._module_file = module_path
        self._params_file = params_path
        self._metadata = metadata
        self._bicep: Optional[IO[str]] = None
        self._bicep_params: Optional[IO[str]] = None

    @property
    def bicep(self) -> IO[str]:
        if not self._bicep:
            raise ValueError("No bicep currently in progress.")
        return self._bicep


    def __enter__(self) -> 'BicepWriter':
        self.bicep = open(self._module_file, 'w')
        for key, value in self._metadata.items():
            self.bicep.write(f"metadata {key} '{value}'\n")
        self._params = open(self._params_file, 'w')

    @overload
    def param(
            self,
            name: str,
            type: Literal["string"],
            *,
            default: Optional[Union[BicepExpression, str]] = None,
            secure: bool = False,
            description: Optional[str] = None,
            envvar: Optional[str] = None,
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
            envvar: Optional[str] = None,
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
            envvar: Optional[str] = None,
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
            envvar: Optional[str] = None,
            allowed: Optional[List[int]] = None,
            max_value: Optional[int] = None,
            min_value: Optional[int] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
    ) -> BicepExpression:
        if secure:
            self._bicep.write("@sys.secure()\n")
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        if allowed:
            self._bicep.write("@sys.allowed([\n")
            for value in allowed:
                self._bicep.write(f"  {json.dumps(value)}\n")
            self._bicep.write("])\n")
        if max_value is not None:
            self._bicep.write(f"@sys.maxValue({max_value})\n")
        if min_value is not None:
            self._bicep.write(f"@sys.minValue({min_value})\n")
        if max_length is not None:
            self._bicep.write(f"@sys.maxLength({max_length})\n")
        if min_length is not None:
            self._bicep.write(f"@sys.minLength({max_length})\n")
        self._bicep.write(f"param {name} {type}")
        if default is not None:
            self._bicep.write(" = ")
            serialize(self._bicep, default)
        else:
            self.bicep.write("\n")
        self.bicep.write("\n")
        #if self._bicep_params:

    def comment(self, comment: str) -> None:
        self._bicep.write(f"// {comment}\n")

    def var(self, name: str, value: Any, *, description: Optional[str] = None) -> BicepExpression:
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        self._bicep.write(f"var {name} = ")
        serialize(self._bicep, value)
        self._bicep.write("\n")

    @overload
    def module(
            self,
            path: str,
            params: Dict[str, Any],
            /,
            *,
            format: Literal["file"] = "file",
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> 'LocalModule':
        ...
    @overload
    def module(
            self,
            path: str,
            params: Dict[str, Any],
            /,
            *,
            format: Literal["registry"],
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            name: Optional[str] = None,
            tag: Optional[str] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> Module:
        ...
    @overload
    def module(
            self,
            params: Dict[str, Any],
            /,
            *,
            format: Literal["templatespec"],
            alias: Optional[str] = None,
            path: Optional[str] = None,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            name: Optional[str] = None,
            tag: Optional[str] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> Module:
        ...

    def module(
            self,
            path: str,
            params: Dict[str, Any],
            /,
            *,
            format: Literal["file", "registry", "templatespec"] = "file",
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[Union[str, BicepExpression]] = None,
            name: Optional[str] = None,
            tag: Optional[str] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> BicepExpression:
        ...

    def __exit__(self, *args) -> None:
        if self._bicep:
            self._bicep.close()
        if self._bicep_params:
            self._bicep_params.close()
