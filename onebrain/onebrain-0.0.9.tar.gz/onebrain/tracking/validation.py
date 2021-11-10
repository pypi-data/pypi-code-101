import posixpath
import re
import numbers

from onebrain.exceptions import OnebrainException, INVALID_PARAMETER_VALUE

_VALID_PARAM_AND_METRIC_NAMES = re.compile(r"^[/\w.\- ]*$")

_BAD_CHARACTERS_MESSAGE = (
    "Names may only contain alphanumerics, underscores (_), dashes (-), periods (.),"
    " spaces ( ), and slashes (/)."
)
_BAD_PATH_MESSAGE = (
    "Names may be treated as files in certain cases, and must not resolve to other names"
    " when treated as such. This name would resolve to '%s'"
)


def path_not_unique(name):
    norm = posixpath.normpath(name)
    return norm != name or norm == "." or norm.startswith("..") or norm.startswith("/")


def _validate_metric_name(name):
    """Check that `name` is a valid metric name and raise an exception if it isn't."""
    if name is None or not _VALID_PARAM_AND_METRIC_NAMES.match(name):
        raise OnebrainException(
            "Invalid metric name: '%s'. %s" % (name, _BAD_CHARACTERS_MESSAGE),
            INVALID_PARAMETER_VALUE,
        )
    if path_not_unique(name):
        raise OnebrainException(
            "Invalid metric name: '%s'. %s" % (name, _BAD_PATH_MESSAGE % posixpath.normpath(name)),
            INVALID_PARAMETER_VALUE,
        )


def _validate_metric(key, value, timestamp, step):
    _validate_metric_name(key)
    if not isinstance(value, numbers.Number):
        print(
            "Got invalid value %s for metric '%s' (timestamp=%s). Please specify value as a valid "
            "double (64-bit floating point)" % (value, key, timestamp),
            INVALID_PARAMETER_VALUE,
        )
        return False

    if not isinstance(timestamp, numbers.Number) or timestamp < 0:
        print(
            "Got invalid timestamp %s for metric '%s' (value=%s). Timestamp must be a nonnegative "
            "long (64-bit integer) " % (timestamp, key, value),
            INVALID_PARAMETER_VALUE,
        )
        return False

    if not isinstance(step, numbers.Number) or step < 0:
        print(
            "Got invalid step %s for metric '%s' (value=%s). Step must be a valid long "
            "(64-bit integer), not negative" % (step, key, value),
            INVALID_PARAMETER_VALUE,
        )
        return False
    return True
