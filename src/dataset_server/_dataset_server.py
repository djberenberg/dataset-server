import json
import logging
import socket
from typing import Optional

import zmq
from torch.utils.data import Dataset

from dataset_server.functional import respond_to_request


class DatasetServer:
    def __init__(
        self, dataset: Dataset, port: int, server_name: Optional[str] = None, _protocol: str = "tcp"
    ):
        self.request_handler = dataset

        self.host = socket.gethostname()
        self.port = port

        self.server_name = server_name or self.__class__.__name__
        self._protocol = _protocol

        self.address = f"{self._protocol}://{self.host}:{self.port}"
        self.logger = logging.getLogger(f"{self.server_name}@{self.address}")
        self.logger.setLevel(logging.DEBUG)

    def serve(self):

        context = zmq.Context()
        frontend = context.socket(zmq.ROUTER)
        frontend.bind(f"{self._protocol}://*:{self.port}")

        poller = zmq.Poller()
        poller.register(frontend, zmq.POLLIN)

        self.logger.info("Starting server")

        while True:

            sockets = dict(poller.poll(1000))
            if frontend in sockets:
                poller.unregister(frontend)

                while True:
                    try:
                        message = frontend.recv_multipart(zmq.NOBLOCK)
                        client, request = message
                        self.logger.debug(f"Responding to client: {client}")
                        respond_to_request(
                            client, json.loads(request.decode()), frontend, self.dataset
                        )
                    except zmq.Again:
                        break

                poller.register(frontend, zmq.POLLIN)
