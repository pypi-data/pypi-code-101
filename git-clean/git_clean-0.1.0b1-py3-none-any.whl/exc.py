

class GitCleanerError(Exception):
    pass


class GitCleanerInitError(GitCleanerError, ValueError):
    pass


class GitCleanerInvalidPathError(GitCleanerError, OSError):
    pass


class GitCleanerInvalidUrlError(GitCleanerError, OSError):
    pass
