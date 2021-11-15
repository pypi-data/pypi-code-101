_tool_registry = {}


class Tool(object):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        _tool_registry[cls.__name__.lower()] = cls

    def _log(self):
        if not (hasattr(self, "_cached_log") and self._cached_log is not None):
            self._cached_log = self.config.logger(type(self).__name__.lower())
        return self._cached_log
