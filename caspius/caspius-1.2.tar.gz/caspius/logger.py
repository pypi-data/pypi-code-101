from datetime import datetime

from caspius.colors import Colors


class Logger:
    def __init__(self, handler=None, use_time=True):
        self._handler = handler
        self.use_time = use_time

    _logs_colors = {
        "info": Colors.CYAN,
        "log": Colors.BOLD,
        "warning": Colors.RED
    }

    def change_colors(self, logs_colors: dict) -> None:
        """
        just give me dict as self._logs_colors to change colors
        """
        if isinstance(logs_colors, dict):
            self._logs_colors = logs_colors

    @property
    def time_now(self) -> str:
        return str(datetime.now().replace(microsecond=0)) + " " \
            if self.use_time else ""

    def set_handler(self, handler) -> None:
        """
        use your own functions to handle logs
        for example add log line by line to file
        """
        self._handler = handler

    def info(self, message: str) -> None:
        message = f"{self.time_now}INFO: {message}"
        self._handler(message) if self._handler else None
        color = self._logs_colors.get("info", Colors.DEFAULT)
        print(f"{color}{message}{color}")

    def warning(self, message: str) -> None:
        message = f"{self.time_now}WARNING: {message}"
        self._handler(message) if self._handler else None
        color = self._logs_colors.get("warning", Colors.DEFAULT)
        print(f"{color}{message}{color}")

    def log(self, message: str) -> None:
        message = f"{self.time_now}LOG: {message}"
        self._handler(message) if self._handler else None
        color = self._logs_colors.get("log", Colors.DEFAULT)
        print(f"{color}{message}{color}")

    def custom_log(self, message: str, name=None, color=None, use_time=None) -> None:
        name = f"{name}: " if name else ""
        if use_time is None:
            use_time = self.use_time
        message = f"{self.custom_time(use_time)}{name}{message}"
        self._handler(message) if self._handler else None

        if color not in Colors.color_list:
            color = Colors.get_color(color)
        print(f"{color}{message}{color}")

    @staticmethod
    def custom_time(use_time: bool) -> str:
        return str(datetime.now().replace(microsecond=0)) + " " \
            if use_time else ""
