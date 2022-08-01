import os
import importlib

from .dependencies import list_installed


def get_modules(extensions_prefix: str = None, *, entrypoint_module: str, entrypoint_function: str):
    ret = []

    for installed_name, installed_path in list_installed().items():

        if extensions_prefix and not installed_name.startswith(extensions_prefix):
            continue

        # Find entrypoint module
        try:
            with open(os.path.join(installed_path.egg_info, "RECORD"),
                      "r") as f:
                module_name, _ = f.readline().split("/", maxsplit=1)
        except Exception as e:
            print(e)
            continue

        if not module_name:
            continue

        if entrypoint_module:
            module = importlib.import_module(f"{module_name}.{entrypoint_module}")
        else:
            module = importlib.import_module(module_name)

        if entrypoint_function:

            ret.append(getattr(module, entrypoint_function, None))

        else:
            ret.append(module)

    return ret

__all__ = ("get_modules", )
