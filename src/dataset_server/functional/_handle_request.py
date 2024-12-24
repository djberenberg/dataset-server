import operator
from contextlib import contextmanager
from typing import Any

from dataset_server.typing import Error, JSONSerializeable, Request, Response


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


def recursive_set_attr(obj: Any, kw: str, arg: Any):
    if "." in kw:
        attr, attrpath = kw.split(".", maxsplit=1)
        nested_obj = getattr(obj, attr)

        return recursive_set_attr(nested_obj, attrpath, arg)
    else:
        setattr(obj, kw, arg)


def handle_request(request: Request, request_handler: Any) -> Response:

    method = request["command"]
    args = request["args"]
    kwargs = request["kwargs"]
    context = request["context"]

    error = None
    return_value = None

    with temporary_context(request_handler, context) as handler:
        try:
            method_to_call = operator.attrgetter(method)(handler)
            return_value: JSONSerializeable = method_to_call(*args, **kwargs)
        except Exception as e:
            error = Error(exception=e.__class__.__name__, message=str(e))

    response = Response(request=request, response=return_value, error=error)
    return response
