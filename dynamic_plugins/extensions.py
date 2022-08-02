import os
import importlib
import sysconfig

from types import ModuleType
from typing import Tuple, List, Iterable, Callable

from .dependencies import list_installed_packages

def get_extensions(extensions_prefix: str = None, *, sub_package: str = None, symbols: List[str] | str = None) -> Iterable[Callable]:
    """
    This function dynamically loads all installed extensions and returns the functions and variables listed in symbols.

    :return: list of functions and variables
    """

    symbols = symbols or []

    if type(symbols) is str:
        symbols = [symbols]

    for module_name, module in get_packages(extensions_prefix):

        if sub_package:
            new_module = importlib.import_module(f"{module_name}.{sub_package}")
        else:
            new_module = module

        for symbol in symbols:
            if hasattr(new_module, symbol):
                yield getattr(new_module, symbol)

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

        for path in emtry_module_paths:

            try:
                with open(os.path.join(path, "RECORD"), "r") as f:
                    for line in f.readlines():
                        if "info/RECORD" in line:
                            # format: package_name-1.0.1.dist-info/RECORD,,
                            module_name = line[:line.find(package_version) - 1]
                            break

            except FileNotFoundError as e:
                print(e)

        else:
            print(f"Can't loat module: {installed_name}")

        # Checks if version is in name:
        # if package_version in module_name:
        #     module_name = module_name.replace(f"-{package_version}", "")

        if not module_name:
            continue

        ret.append((module_name, importlib.import_module(module_name)))

    return ret

__all__ = ("get_packages", "get_extensions")
