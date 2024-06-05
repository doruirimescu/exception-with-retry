exception-with-retry
====================
![Pipeline status](https://github.com/doruirimescu/exception-with-retry/actions/workflows/main.yml/badge.svg?branch=master) 


Wraps any method which throws exceptions. Retries calls when exceptions are thrown. Available on [PyPI](https://pypi.org/project/exception-with-retry/) and installable via pip. Don't forget to star the project!


Description
===========

- Check the [unit tests](https://github.com/doruirimescu/exception-with-retry/blob/master/tests/test_1.py) for usage.
- Build and run tests locally: `tox`
- Publish to [test pypi](https://test.pypi.org/): `tox -e clean && tox -e build && tox -e publish`
- Publish to [pypi](https://pypi.org/project/exception-with-retry/): 
  * `git tag MAJOR.MINOR[.PATCH]`
  * `tox -e clean && tox -e build` 
  * `tox -e publish -- --repository pypi`
  
Example usage:
```python3
@exception_with_retry(n_retry=3, sleep_time_s=1.5)
def wrapped_method(number_1: int, number_2: int = 0, calls: List = []):
    calls.append(1)
    if number_1 < 0:
        raise Exception("Not going to happen")
    else:
        return number_1 + number_2
```

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
