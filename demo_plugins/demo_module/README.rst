# OpenAPI Generator Python SDK

# Install

## Development environment

.. code-block:: console

    $ cd sdk/
    $ pip install -e .

## Production environment

.. code-block:: console

    $ cd sdk/
    $ pip install oag-python-sdk

# Reference

## Read JSON from stdin

Python code:

.. code-block:: python
   :caption: read_json_example1.py

    from oag_sdk import *

    # Read JSON data from stdin. Read line by line
    for json_data in read_json_from_stdin():
        key_one = json_data["key1"]
        key_two = json_data["key2"]

Usage example:

.. code-block:: console

    $ echo '{"key1": 1, "key2": 2}' | read_json_example1.py


## Write JSON to stdout

The Python code:

.. code-block:: python
   :caption: write_json_example1.py

    from oag_sdk import *

    for index in range(5):
        d = {
            "value": index
        }

        # Convert
        write_json_to_stdout(d)

Usage example:

.. code-block:: console

    $ write_json_example1.py
    {"value": 0}
    {"value": 1}
    {"value": 0}
    {"value": 3}
    {"value": 4}
