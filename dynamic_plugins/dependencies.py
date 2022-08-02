import os
import pip
import shutil
import tempfile
import pkg_resources

from typing import Dict, Tuple


def install_library_from_path(path: str):
    """Install a Python library from directory."""
    module_name = path.split(os.sep)[-1]

    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(path, f"{t}/{module_name}")

        ret = pip.main(['install', f"{t}/{module_name}"])

    return ret

def install_library_from_pypi(name: str):
    """Install a Python library from PyPI."""
    pip.main(['install', name])


def list_installed_packages() -> Dict[str, Tuple[str, pkg_resources.DistInfoDistribution]]:
    """
    List all installed Python libraries.

    >>> list_installed_packages()
    {'setuptools': '60.2.0', 'pip': '22.2.1', 'demo-modules': '1.0.0', 'dynamic-plugins': '1.0.0', 'wheel': '0.37.1'}

    :return: A dictionary of installed libraries and their versions
    :rtype: dict[package_name, tuple[package_version, pkg_resources.DistInfoDistribution]]
    """
    return {
        x: (str(v).split(" ")[-1], v)
        for x, v in pkg_resources.working_set.by_key.items()
    }

__all__ = ("install_library_from_path", "install_library_from_pypi",
           "list_installed_packages")
