from ..events import Event
from ..re_api import log_server_console


connect_event = Event.get("connect")


@connect_event.callback
def example(cn, name, handle, privilege):
    if not handle:
        msg = "%s connected with CN %d" % (name, cn)
    else:
        payload = (name, handle, cn, privilege)
        msg = "%s (account %s) connected with CN %d and privilege %s" % \
              payload

    log_server_console(msg)
