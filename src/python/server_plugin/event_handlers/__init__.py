"""
server_plugin.event_handlers
============================

This package contains handlers for different events that can occur within
Red Eclipse's servers, for example "player connect" or "chat message".
"""

import pkgutil


__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    __import__(modname)
