from python_server_plugin import ffi
from server_plugin.re_api import log_server_console
from server_plugin.util import Privileges
from server_plugin.events import Event


@ffi.def_extern()
def pysrvInit():
    log_server_console("Python server plugin initialized")


@ffi.def_extern()
def pysrvRunConnectHooks(cn, name, handle, privilege):
    name = ffi.string(name).decode()
    handle = ffi.string(handle).decode()
    privilege = Privileges(privilege)

    connect_event = Event.get("connect")
    connect_event.run_callbacks(cn, name, handle, privilege)
