class APIError(Exception):
    """Raised when the api or aiohttp raised an error. Accessible attributes are the `code` and `msg`. These attributes are basically what the api has returned."""

    def __init__(self, code: int, msg: str) -> None:
        self.code = code
        self.msg = msg
        super().__init__(self, code, msg)


class RateLimitError(Exception):
    """Raised when the rate limit is exceeded."""


class MediaNotFound(Exception):
    """Raised when you're trying to get a specific media from a GIF object but it is not in the list of medias."""
