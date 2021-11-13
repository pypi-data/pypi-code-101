"""Initialize and get global variables."""


def initialize_constants(db_directory):
    """Set global variables.

    Parameters:
    db_directory (string): Path to directory to save db data and logs
    """
    global DATABASE_FILEPATH
    DATABASE_FILEPATH = 'db/data.json'
    global LOG_FILEPATH
    LOG_FILEPATH = 'log/log.txt'
    global DB_DIRECTORY
    DB_DIRECTORY = db_directory


def get_log_file_path():
    """
    Get file path for log.

    :return: log file path
    """
    return LOG_FILEPATH


def get_db_path():
    """
    Get db path.

    :return: db path
    """
    return DATABASE_FILEPATH


def get_db_dir():
    """
    Get db directory.

    :return: db directory
    """
    return DB_DIRECTORY
