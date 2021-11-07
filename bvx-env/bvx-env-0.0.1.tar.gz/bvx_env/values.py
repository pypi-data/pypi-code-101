import os

from box import Box
from dotenv import dotenv_values


def values(
        key: str = None,
        verbose: bool = False,
        interpolate: bool = True,
) -> Box:
    """
    load environment settings.

    These file's value priorities, low to high.

    - .env.default
    - .env.shared
    - .env.development
    - .env.dev
    - .env.debug
    - .env.secret
    - .env.test
    - .env.production
    - .env.env
    - posix environment variables

    :param key:
    :param verbose:
    :param interpolate:
    :type key: str
    :type verbose: bool
    :type interpolate: bool
    :return:
    """

    # init _config
    _config = {}

    if key is None:

        _config = {
            # load shared development variables
            **dotenv_values(".env.default", verbose=verbose,
                            interpolate=interpolate),

            # load shared development variables
            **dotenv_values(".env.shared", verbose=verbose,
                            interpolate=interpolate),

            # load shared development variables
            **dotenv_values(".env.development", verbose=verbose,
                            interpolate=interpolate),

            # load shared development variables
            **dotenv_values(".env.dev", verbose=verbose,
                            interpolate=interpolate),

            # load shared debug variables
            **dotenv_values(".env.debug", verbose=verbose,
                            interpolate=interpolate),

            # load sensitive variables, this file will set in .gitignore.
            **dotenv_values(".env.secret", verbose=verbose,
                            interpolate=interpolate),

            # load sensitive variables, this file will set in .gitignore.
            **dotenv_values(".env.test", verbose=verbose,
                            interpolate=interpolate),

            # load sensitive variables, this file will set in .gitignore.
            **dotenv_values(".env.production", verbose=verbose,
                            interpolate=interpolate),

            # load sensitive variables, this file will set in .gitignore.
            **dotenv_values(".env", verbose=verbose,
                            interpolate=interpolate),

            # override loaded values with environment variables
            **os.environ,
        }

    else:

        _config = {
            **dotenv_values(key, verbose=verbose,
                            interpolate=interpolate),
        }

    return Box(_config)

# EOF
