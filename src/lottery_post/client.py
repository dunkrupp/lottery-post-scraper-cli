from http import HTTPStatus

class Request:
    def __init__(self, path: str, body: str):
        self.path = path
        self.body = body


class Response:
    def __init__(self, uri: str, status: int, body: str):
        self.uri = uri
        self.status = status
        self.body = body

    def ok(self) -> bool:
        return self.status == HTTPStatus.OK


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request(self, request: Request) -> Response:
        pass # @todo: request
