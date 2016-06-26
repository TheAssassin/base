import os
import sys

# allow the plugin to import server_plugin
def fix_pythonpath():
    for path in [".", "..", "../python", "../src/python", "src/python"]:
        full_path = os.path.abspath(os.path.join(os.curdir, path))
        sys.path.insert(0, full_path)

fix_pythonpath()

import asyncio
from python_server_plugin import ffi
from server_plugin.re_api import log_server_console
from server_plugin.util import Privileges
from server_plugin.events import Event

try:
    from server_plugin.http_server import HttpServer
except ImportError:
    HttpServer = None


loop = asyncio.get_event_loop()

http_srv = None


@ffi.def_extern()
def pysrvInit():
    global http_srv
    if HttpServer is not None:
        http_srv = HttpServer(loop=loop)

    log_server_console("Python server plugin initialized")

    if http_srv is not None:
        http_srv.setup()


@ffi.def_extern()
def pysrvShutdown():
    global http_srv
    if http_srv is not None:
        http_srv.shutdown()


@ffi.def_extern()
def pysrvRunConnectHooks(cn, name, handle, privilege):
    name = ffi.string(name).decode()
    handle = ffi.string(handle).decode()
    privilege = Privileges(privilege)

    connect_event = Event.get("connect")
    connect_event.run_callbacks(cn, name, handle, privilege)


@ffi.def_extern()
def pysrvRunEventLoopOnce():
    # a trick to run a single iteration of the event loop
    # see https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.
    # BaseEventLoop.run_forever for more information
    loop.stop()
    loop.run_forever()
