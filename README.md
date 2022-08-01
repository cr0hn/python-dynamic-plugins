# Python Dynamic Plugins

![License](https://img.shields.io/badge/License-Apache2-SUCCESS)
![Pypi](https://img.shields.io/pypi/v/dynamic-plugins)
![Python Versions](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-blue)

In a nutshell ``Python Dynamic plugins`` is a small library for manage Python plugins dynamically.

# Quickstart

This library load and execute plugins dynamically. 

It allows to load installed Python libraries with some constraints:

- Module names starts with some word.
- Load specific module on each Python library.
- Loas specific function on a module.

This main idea of the project is to be able to create a plugin system which is easy to use and easy to maintain. 

# Install

```bash
> pip install dynamic-plugins
```

# Usage

For this example we'll use the demo package ```demo_module``` that you can find in the ```demo_plugins``` folder.

**Installing the demo plugin**

```bash
> cd demo_plugins/demo_module
> pip install . -U
```

**Load the function ```hello_world``` from the plugin**:

```python

from dynamic_plugins import get_modules

def main():
    functions = get_modules("demo-", entrypoint_module="setup", entrypoint_function="hello_world")

    for fn in functions:
        fn()

if __name__ == '__main__':
    main()
```

# License

Dictionary Search is Open Source and available under the [MIT](https://github.com/cr0hn/python-dynamic-plugins/blob/main/LICENSE).

# Contributions

Contributions are very welcome. See [CONTRIBUTING.md](https://github.com/cr0hn/python-dynamic-plugins/blob/main/CONTRIBUTING.md) or skim existing tickets to see where you could help out.


