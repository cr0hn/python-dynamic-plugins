# Python Dynamic Plugins

![License](https://img.shields.io/pypi/l/dynamic-plugins)
![Pypi](https://img.shields.io/pypi/v/dynamic-plugins)
![Python Versions](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue)

In a nutshell ``Python Dynamic plugins`` is a small library for manage Python plugins dynamically.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Python Dynamic Plugins](#python-dynamic-plugins)
- [Quickstart](#quickstart)
  - [Pip utils](#pip-utils)
  - [Dynamic library loading](#dynamic-library-loading)
- [Install](#install)
- [Dynamic module load usage](#dynamic-module-load-usage)
  - [Load symbols](#load-symbols)
- [Pip utils](#pip-utils-1)
  - [List installed packages](#list-installed-packages)
  - [Install a package from Pypi](#install-a-package-from-pypi)
  - [Install a package from local folder](#install-a-package-from-local-folder)
- [License](#license)
- [Contributions](#contributions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Quickstart

This library has two main parts:

- Pip utils
- Dynamic library loading 

## Pip utils

This module provides some utilities for pip from Python.

## Dynamic library loading

This library load, following some contrains, Python packages and load specific symbols from them. This is: functions, class definitions, variables, etc 

The main idea of the project is to be able to create a plugin system which is easy to use and easy to maintain. 

# Install

```bash
> pip install dynamic-plugins
```

# Dynamic module load usage

For this example we'll use the demo package ```demo_module``` that you can find in the ```demo_plugins``` folder.

**First you need to install the demo package**

```bash
> cd demo_plugins/demo_module
> pip install . -U
```

## Load symbols 

In this example we'll load the ```hello_world()``` function dynamically from the ```demo_module``` package.

```python

from dynamic_plugins import get_extensions

def main():
    for package_name, package_content in get_extensions("demo-", sub_package="setup",symbols="hello_world").items():
        print(package_name)
        print(package_content["module_object"])
        
        for fn in package_content["symbols"]:
            print(fn())

if __name__ == '__main__':
    main()

```

# Pip utils

## List installed packages

```python
from dynamic_plugins import list_installed_packages

def main():

    for package_name, package_version in list_installed_packages().items():
        print(f"{package_name} {package_version}")

if __name__ == '__main__':
    main()

```

## Install a package from Pypi

```python
from dynamic_plugins import install_library_from_pypi

def main():
    install_library_from_pypi("requests")

if __name__ == '__main__':
    main()

```

## Install a package from local folder

```python
from dynamic_plugins import install_library_from_path

def main():
    install_library_from_path("/path/to/package")

if __name__ == '__main__':
    main()

```

# License

Dictionary Search is Open Source and available under the [MIT](https://github.com/cr0hn/python-dynamic-plugins/blob/main/LICENSE).

# Contributions

Contributions are very welcome. See [CONTRIBUTING.md](https://github.com/cr0hn/python-dynamic-plugins/blob/main/CONTRIBUTING.md) or skim existing tickets to see where you could help out.
