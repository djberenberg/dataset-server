import json

from dataset_server.typing import JSONSerializeable


def read_jsonl(filename: str) -> list[JSONSerializeable]:

    with open(filename, "r") as f:
        return [json.loads(ln) for ln in f]
