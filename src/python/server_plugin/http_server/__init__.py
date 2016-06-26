from ..re_api import log_server_console

__all__ = tuple()

# Make sure dependencies are installed
# otherwise disallow import of HttpServer
try:
    import aiohttp
except ImportError:
    log_server_console("Error: aiohttp module not available -> HTTP server "
                       "will not be run")
else:
    from .app import HttpServer
    __all__ = (HttpServer,)
