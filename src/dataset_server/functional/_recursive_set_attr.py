from typing import Any


def recursive_set_attr(obj: Any, kw: str, arg: Any):
    if "." in kw:
        attr, attrpath = kw.split(".", maxsplit=1)
        nested_obj = getattr(obj, attr)

        return recursive_set_attr(nested_obj, attrpath, arg)
    else:
        setattr(obj, kw, arg)
