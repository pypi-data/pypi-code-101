import eurec4a_synop

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import datetime


def test_version():
    assert eurec4a_synop.__version__ == "0.1.0"


def test_plot():
    crs = ccrs.PlateCarree()
    fig, ax = plt.subplots(subplot_kw=dict(projection=crs), figsize=(14, 16))
    eurec4a_synop.add_synop(ax=ax, date=datetime.datetime(year=2020, month=2, day=2))
