from datetime import datetime, timezone

import pytz


def now() -> datetime:
    """Returns the current datetime in utc.

    Returns:
        Current datetime in utc.

    """
    return datetime.now(timezone.utc)


def now_epoch() -> int:
    """Returns the current datetime in utc epoch format.

    Returns:
        Current datetime in utc epoch format.

    """
    return int(datetime.now(timezone.utc).timestamp())


def now_epoch_ms() -> int:
    """Returns the current datetime in ms utc epoch format.

    Returns:
        Current datetime in ms utc epoch format.

    """
    return int(datetime.now(timezone.utc).timestamp() * 1000)


def make_time_aware(dtime: datetime) -> datetime:
    """Converts given datetime to utc.

    Args:
        dtime: A non-utc datetime that will be converted to utc.

    Returns:
        Datetime in utc.

    """
    return dtime.replace(tzinfo=pytz.utc)
