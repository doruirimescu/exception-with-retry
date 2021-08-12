exception-with-retry
====================


Wraps any method which throws exceptions. Retries calls when exceptions are thrown.


Description
===========

Check the [unit tests](https://github.com/doruirimescu/exception-with-retry/blob/master/tests/test_1.py) for usage.


Making Changes & Contributing
=============================

This project uses [pre-commit](http://pre-commit.com/), please make sure to install it before making any
changes::

    pip install pre-commit
    cd exception-with-retry
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.


Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
