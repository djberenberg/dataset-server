import json

import zmq

from dataset_server.typing import Request, Response


def send_request(request: Request, socket: zmq.Socket[zmq.REQ]) -> Response:
    # logger.debug(f"Sending a request: {request} to {self.server_address}")
    socket.send(json.dumps(request).encode())
    _, reply = socket.recv_multipart()
    response: Response = json.loads(reply.decode())
    # logger.debug(f"Got a response {reply_obj}")
    return response
