from python_server_plugin import ffi
from server_plugin.re_api import log_server_console


@ffi.def_extern()
def pysrvInit():
    log_server_console("Python server plugin initialized")
