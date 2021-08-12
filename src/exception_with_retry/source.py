import time

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

    def run(self, args):
        """Execute the wrapped method, and retry for _max_retries.

        Args:
            args (list): list of arguments for the wrapped method.

        Returns:
            [method return type]: value which the wrapped method returns.
        """
        if self._retries < self._max_retries:
            self._retries = self._retries + 1
            try:
                return self._method(*args)
            except Exception as e:
                print(e)
                time.sleep(self._sleep_time_s)
                return self.run(args)
