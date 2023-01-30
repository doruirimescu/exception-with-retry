import functools
import time
from typing import Any, Callable

__author__ = "Doru Irimescu"
__copyright__ = "Doru Irimescu"
__license__ = "MIT"


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from exception_with_retry.source import ExceptionWithRetry`,
# when using this Python module as a library.


class ExceptionWithRetry:
    def __init__(self, method, n_retry=5, sleep_time_s=0.5):
        """Construct ExceptionWithRetry

        Args:
            method(function): Method which throws exception to call.
            n_retry (int, optional): Number of retries. Defaults to 5.
            sleep_time_s (float, optional): Sleep time between consecutive
            retries in seconds. Defaults to 0.5.
        """
        self._method = method
        self._retries = 0
        self._max_retries = n_retry
        self._sleep_time_s = sleep_time_s

    def run(self, *args, **kwargs):
        """Execute the wrapped method, and retry for _max_retries.

        Args:
            args (list): list of arguments for the wrapped method.

        Returns:
            [method return type]: value which the wrapped method returns.
        """
        exception = None
        for i in range(self._max_retries):
            try:
                result = self._method(*args, **kwargs)
                return result
            except Exception as e:
                exception = e
                print(e)
                time.sleep(self._sleep_time_s)
        raise exception


def exception_with_retry(n_retry: int, sleep_time_s: float):
    """Use this decorator to retry calling your function n_retry times,
    with sleep_time_s in between unsuccessful calls.
    Will finally throw the original error if the last retry fails.

    Args:
        n_retry (int): number of retries
        sleep_time_s (float): time to sleep between unsuccessful retries, in seconds

    Returns:
        Callable[..., Any]: decorated function
    """

    def dec(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            ewr = ExceptionWithRetry(func, n_retry, sleep_time_s)
            return ewr.run(*args, **kwargs)

        return wrapper

    return dec
