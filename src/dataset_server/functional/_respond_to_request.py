import json
from typing import Any

import zmq

from dataset_server.typing import Request

from ._handle_request import handle_request


def respond_to_request(
    client: bytes, request: Request, server_socket: zmq.Socket[zmq.ROUTER], request_handler: Any
):
    response = handle_request(request, request_handler)
    response_json_msg = json.dumps(response).encode()

    server_socket.send_multipart([client, b"", response_json_msg])
