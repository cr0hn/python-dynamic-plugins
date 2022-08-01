import os

import pip
import shutil
import tempfile

import pkg_resources


def install_from_path(path: str):
    """Install a Python library from directory."""
    module_name = path.split(os.sep)[-1]

    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(path, f"{t}/{module_name}")

        ret = pip.main(['install', f"{t}/{module_name}"])

    return ret

def install_from_pypi(name: str):
    """Install a Python library from PyPI."""
    pip.main(['install', name])


def list_installed() -> dict:
    """List all installed Python libraries."""
    return {
        x: v
        for x, v in pkg_resources.working_set.by_key.items()
    }
