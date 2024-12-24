from typing import Union

JSONSerializeable = Union[
    None, bool, int, float, str, list["JSONSerializeable"], dict[str, "JSONSerializeable"]
]
