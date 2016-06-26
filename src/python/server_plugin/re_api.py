"""
re_api
======

This file contains wrappers for the server's C API.

This is done to be able to conveniently use this API from Python without
having to deal with types and exact signatures.

This way also allows adding documentation to the functions.
"""

from python_server_plugin import lib as _lib


def log_server_console(msg, prefix="[Python] "):
    """
    Logs a message using Red Eclipse's logging facilities.

    :param str or bytes msg: The message that should be logged
    :param str or bytes prefix: A prefix that will be prepended tothe message
    """
    if hasattr(msg, "encode"):
        msg = msg.encode()

    if hasattr(prefix, "encode"):
        prefix = prefix.encode()

    _lib.reConoutf(prefix + msg)


def get_server_port():
    """
    Returns the main server port.

    You can calculate the server info port by adding 1 to the integer
    returned by this function.

    :return: main server port
    :rtype: int
    """

    return _lib.reGetServerPort()


def shutdown_server():
    return _lib.reShutdownServer()
