import logging

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging(logfilename: str, rotation: str, retention: str) -> None:
    """Sets up logging using loguru. Includes logging of uvicorn and fastapi if it \
    exists in the project. Logs are stored in /python/logs directory.

    Args:
        logfilename: Filename of the log file.
        rotation: Specifies how long a file's rotation should happen.
        retention: Specifies how long before a file is cleaned up.

    Returns:
        Returns None.

    """
    logging.getLogger('uvicorn.access').handlers = [InterceptHandler()]
    logging.getLogger('fastapi').handlers = [InterceptHandler()]
    logging.getLogger().handlers = [InterceptHandler()]

    logger.add(f'/python/logs/{logfilename}.log', rotation=rotation, retention=retention)
