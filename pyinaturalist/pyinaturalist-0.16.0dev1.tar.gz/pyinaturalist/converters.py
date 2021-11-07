"""Type conversion utilities"""
from datetime import date, datetime, timedelta
from logging import getLogger
from typing import Any, Dict, List, MutableSequence, Optional, Union
from warnings import catch_warnings, simplefilter

from dateutil.parser import UnknownTimezoneWarning  # type: ignore  # (missing from type stubs)
from dateutil.parser import parse as parse_date
from dateutil.tz import tzlocal, tzoffset

from pyinaturalist.constants import (
    Coordinates,
    Dimensions,
    HistogramResponse,
    JsonResponse,
    ResponseResult,
)

GENERIC_TIME_FIELDS = ('created_at', 'last_post_at', 'updated_at')
OBSERVATION_TIME_FIELDS = (
    'created_at_details',
    'created_time_zone',
    'observed_on',
    'observed_on_details',
    'observed_on_string',
    'observed_time_zone',
    'time_zone_offset',
)

logger = getLogger(__name__)


# Wrapper functions to apply conversions to all results in a response
# --------------------


def convert_all_coordinates(results: List[ResponseResult]) -> List[ResponseResult]:
    """Convert coordinate pairs in response items from strings to floats, if valid

    Args:
        results: Results from API response; expects coordinates in either 'location' key or
            'latitude' and 'longitude' keys
    """
    results = [convert_lat_long_dict(result) for result in results]
    results = [convert_lat_long_list(result) for result in results]
    return results


def convert_all_place_coordinates(response: JsonResponse) -> JsonResponse:
    """Convert locations for both standard and community-contributed places to floats"""
    response['results'] = {
        'standard': convert_all_coordinates(response['results'].get('standard')),
        'community': convert_all_coordinates(response['results'].get('community')),
    }
    return response


def convert_all_timestamps(results: List[ResponseResult]) -> List[ResponseResult]:
    """Replace all date/time info with datetime objects, where possible"""
    results = [convert_generic_timestamps(result) for result in results]
    results = [convert_observation_timestamps(result) for result in results]
    return results


def convert_histogram(response: JsonResponse) -> HistogramResponse:
    """Convert a response containing time series data into a single ``{date: value}`` dict"""
    # The inner result object's key will be the name of the interval requested
    interval = next(iter(response['results'].keys()))
    histogram = response['results'][interval]

    # Convert keys to appropriate type depending on interval
    if interval in ['month_of_year', 'week_of_year']:
        return {int(k): v for k, v in histogram.items()}
    else:
        return {parse_date(k): v for k, v in histogram.items()}


# Type conversion functions for individual results or values
# --------------------


def convert_csv_list(obj: Any) -> str:
    """Convert list parameters into an API-compatible (comma-delimited) string"""
    if isinstance(obj, list):
        return ','.join(map(str, obj))
    else:
        return obj


def convert_isoformat(value: Union[date, datetime, str]) -> str:
    """Convert a date, datetime, or timestamps to a string in ISO 8601 format.
    If it's a datetime and doesn't already have tzinfo, set it to the system's local timezone.

    Raises:
        :py:exc:`dateutil.parser._parser.ParserError` if a date/datetime format is invalid
    """
    if isinstance(value, str):
        value = parse_date(value)
    if isinstance(value, datetime) and not value.tzinfo:
        value = value.replace(tzinfo=tzlocal())
    return value.isoformat()


def convert_lat_long(obj: Union[Dict, List, None, str]) -> Optional[Coordinates]:
    """Convert a coordinate pair as a dict, list, or string into a pair of floats, if valid"""
    if not obj:
        return None
    if isinstance(obj, str):
        return try_float_pair(*str(obj).split(','))
    elif isinstance(obj, list):
        return try_float_pair(*obj)
    elif isinstance(obj, dict):
        return try_float_pair(obj.get('latitude'), obj.get('longitude'))


def convert_lat_long_dict(result: ResponseResult) -> ResponseResult:
    """Convert a coordinate pair dict within a response to floats, if valid"""
    if 'latitude' in result and 'longitude' in result:
        result['latitude'] = try_float(result['latitude'])
        result['longitude'] = try_float(result['longitude'])
    return result


def convert_lat_long_list(result: ResponseResult):
    """Convert a coordinate pairs in a response item from strings to floats, if valid"""
    # Format inner record if present, e.g. for search results
    if 'record' in result:
        result['record'] = convert_lat_long_list(result['record'])
        return result

    if ',' in (result.get('location') or ''):
        result['location'] = [try_float(coord) for coord in result['location'].split(',')]
    return result


def convert_generic_timestamps(result: ResponseResult) -> ResponseResult:
    """Replace generic created/updated info that's returned by multiple endpoints.
    **Note:** Compared to observation timestamps, these are generally more reliable. These seem to
    be consistently in ISO 8601 format.
    """
    if not result:
        return result

    # Format inner record if present, e.g. for search results
    if 'record' in result:
        result['record'] = convert_generic_timestamps(result['record'])
        return result

    for field in GENERIC_TIME_FIELDS:
        datetime_obj = try_datetime(result.get(field, ''))
        if datetime_obj:
            result[field] = datetime_obj
    return result


# TODO: Replace this with attrs version
def convert_observation_timestamps(result: ResponseResult) -> ResponseResult:
    """Replace observation date/time info with datetime objects"""
    if 'created_at_details' not in result and 'observed_on_string' not in result:
        return result

    observation = result.copy()
    tz_offset = observation.get('time_zone_offset', '')
    tz_name = observation.get('observed_time_zone')

    created_datetime = observation.get('created_at')
    if not isinstance(created_datetime, datetime):
        created_datetime = try_datetime(observation.get('created_at_details', {}).get('date'))
        created_datetime = convert_offset(created_datetime, tz_offset, tz_name)

    # Ignore any timezone info in observed_on timestamp; offset field is more reliable
    observed_datetime = try_datetime(observation.get('observed_on_string', ''), ignoretz=True)
    observed_datetime = convert_offset(observed_datetime, tz_offset, tz_name)

    # If valid, add the datetime objects and remove all other redundant date/time fields
    if created_datetime and observed_datetime:
        for field in OBSERVATION_TIME_FIELDS:
            observation.pop(field, None)
    observation['created_at'] = created_datetime
    observation['observed_on'] = observed_datetime

    return observation


def convert_observation_timestamp(
    timestamp: str, tz_offset: str = None, tz_name: str = None, ignoretz: bool = False
) -> Optional[datetime]:
    """Convert an observation timestamp + timezone info to a datetime. This is needed because
    observed_on and created_at can be in in inconsistent (user-submitted?) formats.
    """
    dt = try_datetime(timestamp, ignoretz=ignoretz)
    return convert_offset(dt, tz_offset, tz_name)


def convert_offset(
    datetime_obj: Optional[datetime], tz_offset: str = None, tz_name: str = None
) -> Optional[datetime]:
    """Use timezone offset info to replace a datetime's tzinfo"""
    if not datetime_obj or not tz_offset:
        return datetime_obj

    try:
        offset = parse_offset(tz_offset, tz_name)
        return datetime_obj.replace(tzinfo=offset)
    except (AttributeError, TypeError, ValueError) as e:
        logger.debug(f'Could not parse offset: {tz_offset}: {str(e)}')
        return None


def parse_offset(tz_offset: str, tz_name: str = None) -> tzoffset:
    """Convert a timezone offset string to a tzoffset object, accounting for some common variations
    in format

    Examples:

        >>> parse_offset('GMT-08:00', 'PST')
        tzoffset('PST', -28800)
        >>> parse_offset('-06:00')
        tzoffset(None, -21600)
        >>> parse_offset('+05:30')
        tzoffset(None, 19800)
        >>> parse_offset('0530')
        tzoffset(None, 19800)

    """

    def remove_prefixes(text, prefixes):
        for prefix in prefixes:
            if text.startswith(prefix):
                text = text[len(prefix) :]  # noqa  # black and flake8 fight over this one
        return text

    # Parse hours, minutes, and sign from offset string; account for either `hh:mm` or `hhmm` format
    tz_offset = remove_prefixes(tz_offset, ['GMT', 'UTC']).strip()
    multiplier = -1 if tz_offset.startswith('-') else 1
    tz_offset = tz_offset.lstrip('+-')
    if ':' in tz_offset:
        hours, minutes = tz_offset.split(':')
    else:
        hours, minutes = tz_offset[:2], tz_offset[2:]

    # Convert to a timezone offset in +/- seconds
    delta = timedelta(hours=int(hours), minutes=int(minutes))
    return tzoffset(tz_name, delta.total_seconds() * multiplier)


def safe_split(value: Any, delimiter: str = '|') -> List[str]:
    """Split a pipe-(or other token)-delimited string"""
    return list(ensure_list(value, convert_csv=True, delimiter=delimiter))


def strip_empty_values(values: Dict) -> Dict:
    """Remove any dict items with empty or ``None`` values."""
    return {k: v for k, v in values.items() if v or v in [False, 0, 0.0]}


# Type conversion functions for collections
# -------------------


def ensure_list(
    value: Any, convert_csv: bool = False, delimiter: str = ','
) -> MutableSequence[Any]:
    """Convert an object, response, or (optionally) comma-separated string into a list"""
    if not value:
        return []
    elif isinstance(value, dict) and 'results' in value:
        value = value['results']
    elif convert_csv and isinstance(value, str) and delimiter in value:
        return [s.strip() for s in value.split(delimiter)]

    if isinstance(value, MutableSequence):
        return value
    elif isinstance(value, (tuple, set)):
        return list(value)
    else:
        return [value]


# Formatting functions
# --------------------


def format_dimensions(dimensions: Union[Dict[str, int], Dimensions, None]) -> Dimensions:
    """Simplify a 'dimensions' dict into a ``(width, height)`` tuple"""
    if not dimensions:
        return (0, 0)
    if isinstance(dimensions, tuple):
        return dimensions
    return dimensions.get("width", 0), dimensions.get("height", 0)


def format_file_size(n_bytes: int) -> str:
    """Convert a file size in bytes into a human-readable format"""
    filesize = float(n_bytes or 0)

    def _format(unit):
        return f'{int(filesize)} {unit}' if unit == 'bytes' else f'{filesize:.2f} {unit}'

    for unit in ['bytes', 'KB', 'MB', 'GB']:
        if filesize < 1024 or unit == 'GB':
            return _format(unit)
        filesize /= 1024

    return _format(unit)


def format_license(value: str) -> Optional[str]:
    """Format a Creative Commons license code"""
    return str(value).upper().replace('_', '-') if value else None


# 'Safe' conversion functions that return invalid values as None instead of raising an error
# --------------------


def try_datetime(timestamp: Any, **kwargs) -> Optional[datetime]:
    """Parse a timestamp string into a datetime, if valid; return ``None`` otherwise"""
    if isinstance(timestamp, datetime):
        return timestamp
    if not timestamp or not str(timestamp).strip():
        return None

    try:
        # Suppress UnknownTimezoneWarning
        with catch_warnings():
            simplefilter('ignore', category=UnknownTimezoneWarning)
            return parse_date(timestamp, **kwargs)
    except (AttributeError, TypeError, ValueError) as e:
        logger.debug(f'Could not parse timestamp: {timestamp}: "{str(e)}"')
        return None


def try_float(value: Any) -> Optional[float]:
    """Convert a value to a float, if valid; return ``None`` otherwise"""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def try_float_pair(*values: Any) -> Optional[Coordinates]:
    """Convert a pair of coordinat values to floats, if both are valid; return ``None`` otherwise"""
    if len(values) != 2:
        return None
    try:
        return float(values[0]), float(values[1])
    except (TypeError, ValueError):
        return None


def try_int(value: Any) -> Optional[float]:
    """Convert a value to a int, if valid; return ``None`` otherwise"""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def try_int_or_float(value: Any) -> Union[int, float, None]:
    """Convert a value to either an int or a float, if valid; return ``None`` otherwise"""
    return try_int(str(value)) or try_float(str(value))
