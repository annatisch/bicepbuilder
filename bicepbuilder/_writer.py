from typing import Self, Optional, IO, Literal, List, Dict, Any, Union, overload
import os
import json

from ._utils import generate_suffix, resolve_value, serialize, serialize_dict, serialize_list
from .expressions import BicepExpression, BicepParam, Deployment, Identity, Module, Output, PrincipalId, Resource, ResourceGroup, ResourceId, ResourceName
from .resources import _AddResourceMixin


class BicepWriter(_AddResourceMixin):
    bicep: IO[str]

    def __init__(
            self,
            module_path: str,
            *,
            module_name: str,
            params: bool = False,
            metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        self._module_dir = module_path
        self._module_file = os.path.join(self._module_dir, module_name + ".bicep")
        self._params_file = os.path.join(self._module_dir, module_name + ".json") if params else None
        self._metadata = metadata or {}
        self._bicep: Optional[IO[str]] = None
        self._bicep_params: Optional[IO[str]] = None

    @property
    def bicep(self) -> IO[str]:
        if not self._bicep:
            raise ValueError("No bicep currently in progress.")
        return self._bicep

    def __enter__(self) -> 'BicepWriter':
        if not os.path.isdir(self._module_dir):
            os.makedirs(self._module_dir)
        self._bicep = open(self._module_file, 'w')
        for key, value in self._metadata.items():
            self._bicep.write(f"metadata {key} '{value}'\n")
        self._params = open(self._params_file, 'w') if self._params_file else None
        return self

    @overload
    def param(
            self,
            name: str,
            type: Literal["string"],
            /,
            *,
            default: Optional[Union[BicepExpression, str]] = None,
            secure: bool = False,
            description: Optional[str] = None,
            envvar: Optional[str] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
            allowed: Optional[List[str]] = None,
    ) -> BicepParam:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["int"],
            /,
            *,
            default: Optional[Union[BicepExpression, int]] = None,
            description: Optional[str] = None,
            envvar: Optional[str] = None,
            allowed: Optional[List[int]] = None,
            max_value: Optional[int] = None,
            min_value: Optional[int] = None,
    ) -> BicepParam:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["bool"],
            /,
            *,
            default: Optional[Union[BicepExpression, bool]] = None,
            description: Optional[str] = None,
            envvar: Optional[str] = None,
    ) -> BicepParam:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["array"],
            /,
            *,
            default: Optional[Union[BicepExpression, List[Any]]] = None,
            description: Optional[str] = None,
            max_length: Optional[int] = None,
            min_length: Optional[int] = None,
    ) -> BicepParam:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["object"],
            /,
            *,
            default: Optional[Union[BicepExpression, Dict[str, Any]]] = None,
            secure: bool = False,
            description: Optional[str] = None,
    ) -> BicepParam:
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
    ) -> BicepParam:
        if secure:
            self._bicep.write("@sys.secure()\n")
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        if allowed:
            self._bicep.write("@sys.allowed([\n")
            for value in allowed:
                if isinstance(value, str):
                    clean_value = "'" + json.dumps(value).strip('"') + "'"
                else:
                    clean_value = json.dumps(value)
                self._bicep.write(f"  {clean_value}\n")
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
        #else:
        #    self._bicep.write("\n")
        self._bicep.write("\n\n")
        return BicepParam(name, type)
        #if self._bicep_params:

    def comment(self, comment: str) -> None:
        self._bicep.write(f"// {comment}\n")

    def var(self, name: str, type: str, value: Any, *, description: Optional[str] = None) -> BicepExpression:
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        self._bicep.write(f"var {name} = ")
        serialize(self._bicep, value)
        self._bicep.write("\n\n")
        return BicepParam(name, type)

    @overload
    def resource(
            self,
            resource: str,
            version: str,
            *,
            name: Union[str, BicepExpression],
            location: Union[str, BicepExpression],
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
            depends_on: Optional[List[Union[str, BicepExpression]]] = None,
            scope: Optional[BicepExpression] = None,
            **kwargs
    ) -> Resource:
        ...
    @overload
    def resource(
            self,
            resource: str,
            version: str,
            *,
            existing: Union[str, BicepExpression],
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
            scope: Optional[BicepExpression] = None,
            **kwargs
    ) -> Resource:
            ...
    def resource(
            self,
            resource: str,
            version: str,
            *,
            name: Optional[Union[str, BicepExpression]] = None,
            existing: Optional[Union[str, BicepExpression]] = None,
            location: Optional[Union[str, BicepExpression]] = None,
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None,
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[List[Union[str, BicepExpression]]] = None,
            **kwargs
    ) -> Resource:
        symbol = "resource_" + generate_suffix()
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        if batch_size:
            self._bicep.write(f"@sys.batchSize({batch_size})\n")
        self._bicep.write(f"resource {symbol} '{resource}@{version}'")
        if existing:
            self._bicep.write("existing")
            params = {'name': existing}
        else:
            params = {
                'name': name,
                'location': location,
                'tags': tags,
            }
        self._bicep.write(" = {\n")
        params.update(kwargs)
        serialize_dict(self._bicep, params, indent="  ")
        if scope:
            self._bicep.write(f"  scope: {resolve_value(scope)}\n")
        if depends_on:
            self._bicep.write(f"  dependsOn: [\n")
            serialize_list(self._bicep, depends_on, indent="    ")
            self._bicep.write("  ]")
        self._bicep.write("}\n\n")
        return Resource(symbol)

    @overload
    def module(
            self,
            name: str,
            /,
            *,
            format: Literal["file"] = "file",
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[List[Union[str, BicepExpression]]] = None,
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
            *args,
            format: Literal["file", "registry", "templatespec"] = "file",
            scope: Optional[BicepExpression] = None,
            depends_on: Optional[List[Union[str, BicepExpression]]] = None,
            name: Optional[str] = None,
            tag: Optional[str] = None,
            batch_size: Optional[int] = None,
            description: Optional[str] = None
    ) -> BicepExpression:
        symbol = "module_" + generate_suffix()
        name = Deployment().name.format(suffix="_" + symbol)
        if description:
            self._bicep.write(f"@sys.description('{description}')\n")
        if batch_size:
            self._bicep.write(f"@sys.batchSize({batch_size})\n")
        if format == "file":
            self._bicep.write(f"module {symbol} '{args[0]}.bicep' = {{\n")
            self._bicep.write(f"  name: '{name}'\n")
            if scope:
                self._bicep.write(f"  scope: {resolve_value(scope)}\n")
            if depends_on:
                self._bicep.write(f"  dependsOn: [\n")
                serialize_list(self._bicep, depends_on, indent="    ")
                self._bicep.write("  ]")
            return LocalModule(
                self._bicep,
                symbol,
                module_path=self._module_dir,
                module_name=args[0]
            )
    
    @overload
    def managed_identity(
            self,
            *,
            name: Union[str, BicepExpression],
            location: Union[str, BicepExpression],
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None,
    ) -> Identity:
        ...
    @overload
    def managed_identity(self, *, existing: Union[str, BicepExpression]) -> Identity:
        ...
    def managed_identity(
            self,
            *,
            name: Optional[Union[str, BicepExpression]] = None,
            existing: Optional[Union[str, BicepExpression]] = None,
            location: Optional[Union[str, BicepExpression]] = None,
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None,
    ) -> Identity:
        managed_identity = self.resource(
            "Microsoft.ManagedIdentity/userAssignedIdentities",
            "2023-01-31",
            name=name,
            existing=existing,
            tags=tags,
            location=location
        )
        return Identity(managed_identity._value)

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
            version: Optional[str] = None,
    ) -> ResourceGroup:
        ...
    def resource_group(
            self,
            *,
            name: Optional[Union[str, BicepExpression]] = None,
            location: Optional[Union[str, BicepExpression]] = None,
            existing: Optional[Union[str, BicepExpression]] = None,
            tags: Optional[Union[Dict[str, str], BicepExpression]] = None
    ) -> ResourceGroup:
        if existing:
            rg = self.resource(
                "Microsoft.Resources/resourceGroups",
                "2021-04-01",
                existing=existing,
            )
        else:
            rg = self.resource(
                "Microsoft.Resources/resourceGroups",
                "2021-04-01",
                name=name,
                location=location,
                tags=tags
            )
        return ResourceGroup(rg.name)

    def output(self, name: str, value) -> None:
        if isinstance(value, Output):
            self._bicep.write(f"output {name} {value.type} = {value.resolve()}\n")
        elif isinstance(value, (ResourceId, ResourceName)):
            self._bicep.write(f"output {name} string = {value.resolve()}\n")
        elif isinstance(value, BicepExpression):
            raise ValueError(f"Unexpected BicepExpression: {value}")
        elif isinstance(value, str):
            self._bicep.write(f"output {name} string = '{value}'\n")
        elif isinstance(value, int):
            self._bicep.write(f"output {name} int = {value}\n")
        else:
            raise TypeError(f"Unexpected output type: {value}")

    def __exit__(self, *args) -> None:
        if self._bicep:
            self._bicep.close()
        if self._bicep_params:
            self._bicep_params.close()


class LocalModule(BicepWriter, Module):
    def __init__(
            self,
            parent_bicep: IO[str],
            symbol: str,
            module_path: str,
            *,
            module_name: str,
            params: bool = False,
            metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(
            module_name=module_name,
            module_path=module_path,
            params=params,
            metadata=metadata
        )
        self._value = symbol
        self.outputs = {}
        self._parent_bicep = parent_bicep
        self._module_params = {}

    def __enter__(self) -> 'LocalModule':
        super().__enter__()
        self._parent_bicep.write("  params: {\n")
        return self
    
    def __exit__(self, *args) -> None:
        super().__exit__(*args)
        serialize_dict(self._parent_bicep, self._module_params, indent="    ")
        self._parent_bicep.write("  }\n")
        self._parent_bicep.write("}\n\n")

    @overload
    def param(
            self,
            param: BicepParam,
            /,
            *,
            default: Optional[Union[BicepExpression, str]] = None,
            secure: bool = False,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    @overload
    def param(
            self,
            name: str,
            type: Literal["string"],
            /,
            *,
            value: Optional[Union[BicepExpression, str]] = None,
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
            /,
            *,
            value: Optional[Union[BicepExpression, int]] = None,
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
            /,
            *,
            value: Optional[Union[BicepExpression, bool]] = None,
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
            /,
            *,
            value: Optional[Union[BicepExpression, List[Any]]] = None,
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
            /,
            *,
            value: Optional[Union[BicepExpression, Dict[str, Any]]] = None,
            default: Optional[Union[BicepExpression, Dict[str, Any]]] = None,
            secure: bool = False,
            description: Optional[str] = None,
    ) -> BicepExpression:
        ...
    def param(
            self,
            *args,
            **kwargs
    ) -> BicepExpression:
        if isinstance(args[0], BicepParam):
            value = args[0]
            self._module_params[value.name] = value
            return super().param(value.name, value.type, **kwargs)
        else:
            try:
                value = kwargs.pop('value')
                self._module_params[args[0]] = value
            except IndexError:
                if 'default' not in kwargs:
                    raise ValueError("Module param must pass in value or specify default.")
        return super().param(*args, **kwargs)

    def output(self, name: str, value) -> None:
        super().output(name, value)
        if isinstance(value, Output):
            self.outputs[name] = Output(symbol=self._value, name=name, type=value.type)
        elif isinstance(value, (ResourceId, ResourceName)):
            self.outputs[name] = Output(symbol=self._value, name=name, type="string")
        elif isinstance(value, BicepExpression):
            raise ValueError(f"Unexpected BicepExpression: {value}")
        elif isinstance(value, str):
            self.outputs[name] = Output(symbol=self._value, name=name, type="string")
        elif isinstance(value, int):
            self.outputs[name] = Output(symbol=self._value, name=name, type="int")
        else:
            raise TypeError(f"Unexpected output type: {value}")
