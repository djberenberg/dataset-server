from typing import TypedDict

from ._json_serializeable import JSONSerializeable


class Request(TypedDict):
    command: str

    context: dict[str, JSONSerializeable]
    args: list[JSONSerializeable]
    kwargs: dict[str, JSONSerializeable]
