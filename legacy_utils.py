import asyncio
import inspect
from collections import MutableMapping


class LegacyCache(MutableMapping):
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)


def legacy_signature_report(target):
    """Uses inspect.getargspec (removed in Python 3.11)."""
    spec = inspect.getargspec(target)  # noqa: B009
    return f"Legacy argspec: {spec.args}"


def legacy_event_loop():
    """Uses get_event_loop() in the old style."""
    loop = asyncio.get_event_loop()
    return f"Loop running: {loop.is_running()}"
