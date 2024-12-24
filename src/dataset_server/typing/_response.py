from typing import Optional, TypedDict

from ._error import Error
from ._json_serializeable import JSONSerializeable
from ._request import Request


class Response(TypedDict):
    request: Request
    response: JSONSerializeable
    error: Optional[Error]
