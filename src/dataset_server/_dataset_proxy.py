from functools import cache
from typing import Any, cast

import zmq
from torch.utils.data import Dataset

from dataset_server.functional import send_request


class DatasetProxy(Dataset):
    def __init__(
        self,
        server_address: str,
        get_method: str = "__getitem__",
        len_method: str = "__len__",
        **context_kwargs
    ):

        self.server_address = server_address
        self.get_method = get_method
        self.len_method = len_method

        self.context = context_kwargs

    @cache
    def zmq_context(self) -> zmq.Context:
        return zmq.Context()

    @cache
    def socket(self) -> zmq.Socket:
        sock = self.zmq_context().socket(zmq.REQ)
        sock.connect(self.server_address)
        return sock

    def reset_connection(self):
        self.zmq_context.cache_clear()
        self.socket.cache_clear()

    def __getitem__(self, index: int) -> dict[str, Any]:
        message = {
            "command": self.get_method,
            "args": [index],
            "context": self.context,
        }

        reply = send_request(message, self.socket())
        return reply["response"]

    def __len__(self) -> int:
        message = {"command": self.len_method, "context": self.context}
        return cast(int, send_request(message, self.socket())["response"])
