from datetime import datetime, timezone

import pytz

from toolip.utils.time import make_time_aware, now, now_epoch, now_epoch_ms


def test_now():
    assert now().tzinfo == timezone.utc


def test_now_epoch():
    now = datetime.now(timezone.utc).timestamp()
    assert now_epoch() == int(now)


def test_now_epoch_ms():
    now = datetime.now(timezone.utc).timestamp() * 1000
    assert now_epoch_ms() == int(now)


def test_make_time_aware():
    dtime = datetime.now()
    assert dtime.tzinfo != pytz.utc
    assert make_time_aware(dtime).tzinfo == pytz.utc
