import logging
from time import gmtime

LEVELS = {1: "ERROR", 2: "WARN", 3: "INFO"}


def LOGGER(message: str, level: int = 3):
    """
    logging package's root logger whose level is set to info.

    :param message: log statement
    :param level: level of the log
    :return:
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.Formatter.converter = gmtime

    if level == 1:
        logging.error(msg=f"{message}")
    elif level == 2:
        logging.warning(msg=f"{message}")
    else:
        logging.info(msg=f"{message}")
