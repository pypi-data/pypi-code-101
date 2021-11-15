from logging import Formatter


class MarkdownFormatter(Formatter):
    parse_mode = 'Markdown'
    fmt = "```\n" \
          "%(levelname)s %(asctime)s [%(name)s:%(funcName)s]\n" \
          "%(message)s" \
          "\n```"

    def __init__(self, fmt: str = None, *args, **kwargs):
        super(MarkdownFormatter, self).__init__(fmt or self.fmt, *args, **kwargs)

    def formatException(self, *args, **kwargs):
        string = super(MarkdownFormatter, self).formatException(*args, **kwargs)
        return f"```\n{string}\n```"
