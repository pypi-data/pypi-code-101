import warnings
import datetime as dt
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pathlib import Path

IMAGE_PATH = Path(__file__).parent / "images"

MIN_DATE = dt.datetime(year=2020, month=1, day=1)
MAX_DATE = dt.datetime(year=2020, month=2, day=29)


def add_synop(ax, date):
    if isinstance(date, dt.datetime):
        warnings.warn(
            "You provided a `datetime` to `add_synop`, but because synoptic"
            " charts are only available at 00:00UTC the nearest time to midnight"
            " will be used"
        )
        date = _nearest_midnight(date)

    if date < MIN_DATE or date > MAX_DATE:
        raise NotImplementedError(
            f"You requested a synoptic chart for {date}, but the charts are only"
            f" available between {MIN_DATE} and {MAX_DATE}"
        )
    fn = IMAGE_PATH / f"{date:%Y%m%d000000}.png"
    im = plt.imread(fn)

    ax.imshow(im, extent=[-100, -10, 0, 35], transform=ccrs.PlateCarree())


def _nearest_midnight(t):
    current_td = dt.timedelta(
        hours=t.hour,
        minutes=t.minute,
        seconds=t.second,
        microseconds=t.microsecond,
    )

    to_midnight = dt.timedelta(hours=round(current_td.total_seconds() / (60 * 60 * 24)))
    return dt.datetime.combine(t, dt.time(0)) + to_midnight
