import os
import importlib
import sysconfig

from types import ModuleType
from typing import Tuple, List, Dict

from .exceptions import DynamicPluginException
from .dependencies import list_installed_packages

def get_symbols_from_package(package: str, symbols: List[str] | str = None) -> Tuple[object, Dict[str, dict]] | DynamicPluginException:
    """
    This function dynamically loads all installed extensions and returns the functions and variables listed in symbols.

    :return: list of functions and variables
    """

    symbols = symbols or []

    if type(symbols) is str:
        symbols = [symbols]

    if type(package) is str:
        try:
            new_module = importlib.import_module(package)
        except ModuleNotFoundError as e:
            raise DynamicPluginException(f"Can't load module: {package}") from e
    else:
        new_module = package

    ret_symbols = {}

    for symbol in symbols:
        ret_symbols[symbol] = getattr(new_module, symbol, None)

    return new_module, ret_symbols


def get_extensions(extensions_prefix: str = None, *, sub_package: str = None, symbols: List[str] | str = None) -> Dict[str, dict]:
    """
    This function dynamically loads all installed extensions and returns the functions and variables listed in symbols.

    :return: list of functions and variables
    """

    symbols_list = symbols or []

    if type(symbols_list) is str:
        symbols_list = [symbols_list]


    ret = {}

    for module_name, module in get_packages(extensions_prefix):

        if sub_package:
            new_module = f"{module_name}.{sub_package}"
        else:
            new_module = module

        got_module, got_symbols = get_symbols_from_package(new_module, symbols_list)

        ret[module_name] = dict(
            module_object=got_module,
            symbols=got_symbols
        )

    return ret


def get_packages(module_prefix: str = None) -> List[Tuple[str, ModuleType]]:
    """
    dynamically list installed Python libraries and load them with matches
    with module_prefix.

    :return: list of modules and their names
    :rtype: list((str: [MODULE NAME], ModuleType: [MODULE]))
    """
    ret = []

    for installed_name, (package_version, dist_info) in list_installed_packages().items():

        if module_prefix and not installed_name.startswith(module_prefix):
            continue

        # Find entrypoint module
        emtry_module_paths = (
            dist_info.egg_info,
            os.path.join(
                sysconfig.get_paths()["platlib"],
                f"{installed_name.replace('-', '_')}-{package_version}.dist-info"
            )
        )

        module_name = None

        for path in emtry_module_paths:

            if module_name is not None:
                break

            try:
                with open(os.path.join(path, "RECORD"), "r") as f:
                    for line in f.readlines():
                        if line.count("/") == 1 and "/__init__.py" in line:
                            module_name = line.split("/")[0]
                            break

            except FileNotFoundError:
                ...


        if not module_name:
            continue

        try:
            ret.append((module_name, importlib.import_module(module_name)))
        except ModuleNotFoundError as e:
            raise DynamicPluginException(f"Can't load module: {module_name}") from e

    return ret

__all__ = ("get_packages", "get_extensions", "get_symbols_from_package")
