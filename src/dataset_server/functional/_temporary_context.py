import operator
from contextlib import contextmanager
from typing import Any

from ._recursive_set_attr import recursive_set_attr


@contextmanager
def temporary_context(request_handler: Any, kwargs: dict[str, Any]):

    original_context = {kw: operator.attrgetter(kw)(request_handler) for kw in kwargs}

    try:
        for kw, arg in kwargs.items():
            # raises an AttributeError if no such attribute can be set.
            recursive_set_attr(request_handler, kw, arg)

        yield request_handler

    finally:
        for kw, arg in original_context.items():
            recursive_set_attr(request_handler, kw, arg)
