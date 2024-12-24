import gzip
import json

from dataset_server.typing import JSONSerializeable


def read_jsonl(filename: str, gzip_compressed: bool = False) -> list[JSONSerializeable]:

    with (gzip.open if gzip_compressed else open)(filename, "rt") as f:
        return [json.loads(ln) for ln in f]
