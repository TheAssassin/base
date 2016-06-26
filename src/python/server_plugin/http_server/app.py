from aiohttp import web
from asyncio import coroutine
from ..re_api import log_server_console as log, get_server_port


class HttpServer:
    _routes = []

    def __init__(self, host="0.0.0.0", port=get_server_port()+2, loop=None):
        self.host = host
        self.port = port

        self._app = web.Application(loop=loop)
        for route in self.__class__._routes:
            self._app.router.add_route(*route)

        self._loop = self._app.loop
        self._srv = None
        self._handler = None

    def setup(self):
        self._handler = self._app.make_handler()
        self._srv = self._loop.run_until_complete(
            self._loop.create_server(self._handler, self.host, self.port))

        log("======== Running on http://{}:{}/ ========\n".format(
            self.host, self.port))

    def shutdown(self, shutdown_timeout=60.0):
        self._srv.close()
        self._loop.run_until_complete(self._srv.wait_closed())
        self._loop.run_until_complete(self._app.shutdown())
        self._loop.run_until_complete(
            self._handler.finish_connections(shutdown_timeout))
        self._loop.run_until_complete(self._app.cleanup())

    @classmethod
    def route(cls, path, method="GET"):
        def decorator(func):
            cls._routes.append((method, path, func))
            return func

        return decorator


@HttpServer.route("/")
@coroutine
def handle_request(request):
    return web.Response(body=b"woo")
