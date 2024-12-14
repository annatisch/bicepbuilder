from typing import Self, Optional, IO, Literal, List, Dict, Any, overload
import os
import json

from ._utils import BicepExpression, serialize

class infra:
    def __init__(
            self,
            *,
            dir: str = ".",
            infra: str = "infra",
            module: str = "main",
    ) -> None:
        self._output_dir = os.path.join(os.path.abspath(os.curdir()), infra)
        self._main_module_file = os.path.join(self._output_dir, module + ".bicep")
        self._main_params_file = os.path.join(self._output_dir, module + ".json")
        self._main : Optional[IO[str]] = None
        self._params : Optional[IO[str]] = None

    def __enter__(self) -> 'infra':
        self._main = open(self._main_module_file, 'w')
        self._params = open(self._main_params_file, 'w')

    @overload
    def param(
            self,
            name: str,
            type: Literal["string"],
            *,
            default: Optional[str] = None,
            secure: bool = False,
            description: Optional[str] = None,
            max_length: Optional[int] = None,
            allowed: Optional[List[str]] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["int"],
            *,
            default: Optional[int] = None,
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
            default: Optional[bool] = None,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["array"],
            *,
            default: Optional[List[Any]] = None,
            description: Optional[str] = None,
            max_length: Optional[int] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["object"],
            *,
            default: Optional[Dict[str, Any]] = None,
            secure: bool = False,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    def param(
            self,
            name: str,
            type: str,
            *,
            default: Optional[int] = None,
            secure: bool = False,
            description: Optional[str] = None,
            allowed: Optional[List[int]] = None,
            max_value: Optional[int] = None,
            min_value: Optional[int] = None,
            max_length: Optional[int] = None,
    ) -> BicepExpression:
        if secure:
            self._main.write("@sys.secure()\n")
        if description:
            self._main.write(f"@sys.description('{description}')\n")
        if allowed:
            self._main.write("@sys.allowed([\n")
            for value in allowed:
                self._main.write(f"  {json.dumps(value)}\n")
            self._main.write("])\n")
        if max_value is not None:
            self._main.write(f"@sys.maxValue({max_value})\n")
        if min_value is not None:
            self._main.write(f"@sys.minValue({min_value})\n")
        if max_length is not None:
            self._main.write(f"@sys.maxLength({max_length})\n")
        self._main.write(f"param {name} {type}")
        if default is not None:
            self._main.write(" = ")
            serialize(self._main, default)
        else:
            self._main.write("\n")
        self._main.write("\n")

    def comment(self, comment: str) -> None:
        self._main.write(f"// {comment}\n")
    def var()

    def __exit__(self, *args) -> None:
        self._main.close()
        self._params.close()
