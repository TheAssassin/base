class Event:
    _known_events = {}

    def __init__(self, name):
        if name in self.__class__._known_events:
            raise ValueError("hook with name '%s' exists already!" % name)

        self.name = name
        self._callbacks = []

    def callback(self, func):
        """
        Decorator that can be used to register callbacks for events.

        The callable needs to be able to accept the right amount of arguments.
        If in doubt, use *args (or similar) and print the arguments.

        :param callable func: Any kind of callable
        :return: the given callable (required for being a decorator)
        :rtype: callabke
        """
        self._callbacks.append(func)
        return func

    def run_callbacks(self, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)

    @classmethod
    def get(cls, name):
        """
        Factory function that checks if a hook instance named `name` is known
        to the hook system and returns this instance, otherwise creates and
        returns a new hook.

        :param str name: name of the hook you want an instance for
        :return: the hook you want
        :rtype: :class:`Hook`
        """

        try:
            hook = cls._known_events[name]
        except KeyError:
            hook = Event(name)
            cls._known_events[name] = hook

        return hook