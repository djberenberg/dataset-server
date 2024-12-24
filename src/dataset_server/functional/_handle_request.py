import operator
from typing import Any

from dataset_server.functional import temporary_context
from dataset_server.typing import Error, JSONSerializeable, Request, Response


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
