#################################################
# Mauna Loa CO2 data scraper
#################################################
# {License_info} TODO
#################################################
# Author: Kyle Pollina
# Copyright: Copyright 2021, https://github.com/kylepollina/ml_co2
# License: TODO
# Version: TODO
# Maintainer: {maintainer}
# Email: kylepollina@pm.me
# Status: In Development
#################################################


from datetime import datetime
from typing import Optional

import requests


def monthly_mean(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None
) -> dict:
    """ Get the monthly mean data
    -----------------------------

    Data from March 1958 through April 1974 have been obtained by C. David Keeling
    of the Scripps Institution of Oceanography (SIO) and were obtained from the
    Scripps website (scrippsco2.ucsd.edu).
    Monthly mean CO2 constructed from daily mean values
    Scripps data downloaded from http://scrippsco2.ucsd.edu/data/atmospheric_co2
    Monthly values are corrected to center of month based on average seasonal
    cycle. Missing days can be asymmetric which would produce a high or low bias.
    Missing months have been interpolated, for NOAA data indicated by negative stdev
    and uncertainty. We have no information for SIO data about Ndays, stdv, unc
    so that they are also indicated by negative numbers
    """

    if start and not isinstance(start, datetime):
        raise TypeError("Start must be a datetime object")
    if end and not isinstance(end, datetime):
        raise TypeError("End must be a datetime object")

    url = "https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
    res = requests.get(url)
    raw = res.content.decode("utf-8")
    lines = raw.splitlines()
    _license = "\n".join(lines[:41])
    description = "\n".join(lines[41:51])
    headers = "\n".join(lines[51:53])

    mean = {
        "url": url,
        "license": _license,
        "description": description,
        "headers": headers,
        "raw": raw,
        "data": {
            "yr": [],
            "mon": [],
            "decimal": [],
            "monthly average (ppm)": [],
            "de-seasonalized (ppm)": [],
            "#days": [],
            "st.dev of days": [],
            "unc. of mon mean": [],
        },
    }

    # Parse data
    for row in lines[53:]:
        yr, mon, decimal, ppm, de_season, days, stdev, unc = row.split()

        date = datetime(year=int(yr), month=int(mon), day=1)

        if start and start > date:
            continue

        if end and end < date:
            break

        mean["data"]["yr"].append(yr)
        mean["data"]["mon"].append(mon)
        mean["data"]["decimal"].append(decimal)
        mean["data"]["monthly average (ppm)"].append(ppm)
        mean["data"]["de-seasonalized (ppm)"].append(de_season)
        mean["data"]["#days"].append(days)
        mean["data"]["st.dev of days"].append(stdev)
        mean["data"]["unc. of mon mean"].append(unc)

    return mean


def annual_mean(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None
) -> dict:
    """Get the annual mean data
    ----------------------------

    Data from March 1958 through April 1974 have been obtained by C. David Keeling
    of the Scripps Institution of Oceanography (SIO) and were obtained from the
    Scripps website (scrippsco2.ucsd.edu).

    The estimated uncertainty in the annual mean is the standard deviation
    of the differences of annual mean values determined independently by
    NOAA/ESRL and the Scripps Institution of Oceanography.

    NOTE: In general, the data presented for the last year are subject to change,
    depending on recalibration of the reference gas mixtures used, and other quality
    control procedures. Occasionally, earlier years may also be changed for the same
    reasons.  Usually these changes are minor.

    CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    """

    if start and not isinstance(start, datetime):
        raise TypeError("Start must be a datetime object")
    if end and not isinstance(end, datetime):
        raise TypeError("End must be a datetime object")

    url = 'https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_annmean_mlo.txt'
    res = requests.get(url)
    raw = res.content.decode("utf-8")
    lines = raw.splitlines()
    _license = "\n".join(lines[:41])
    description = "\n".join(lines[41:56])
    headers = lines[56]

    mean = {
        "url": url,
        "license": _license,
        "description": description,
        "headers": headers,
        "raw": raw,
        "data": {
            "yr": [],
            "mean (ppm)": [],
            "unc": [],
        },
    }

    # Parse data
    for row in lines[57:]:
        yr, ppm, unc = row.split()

        date = datetime(year=int(yr), month=1, day=1)

        if start and start > date:
            continue

        if end and end < date:
            break

        mean["data"]["yr"].append(yr)
        mean["data"]["mean (ppm)"].append(ppm)
        mean["data"]["unc"].append(unc)

    return mean


def annual_mean_increase(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None
) -> dict:
    """
    Data from March 1958 through April 1974 have been obtained by C. David Keeling
    of the Scripps Institution of Oceanography (SIO) and were obtained from the
    Scripps website (scrippsco2.ucsd.edu).

    Annual CO2 mole fraction increase (ppm) from Jan 1 through Dec 31.

    The uncertainty in the Mauna Loa annual mean growth rate is estimated
    from the standard deviation of the differences between monthly mean
    values determined independently by the Scripps Institution of Oceanography
    and by NOAA/ESRL.

    NOTE: In general, the data presented for the last year are subject to change,
    depending on recalibration of the reference gas mixtures used, and other quality
    control procedures. Occasionally, earlier years may also be changed for the same
    reasons.  Usually these changes are minor.

    CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    """

    if start and not isinstance(start, datetime):
        raise TypeError("Start must be a datetime object")
    if end and not isinstance(end, datetime):
        raise TypeError("End must be a datetime object")

    url = "https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_gr_mlo.txt"
    res = requests.get(url)
    raw = res.content.decode("utf-8")
    lines = raw.splitlines()
    _license = "\n".join(lines[:41])
    description = "\n".join(lines[41:59])
    headers = lines[59]

    mean = {
        "url": url,
        "license": _license,
        "description": description,
        "headers": headers,
        "raw": raw,
        "data": {
            "yr": [],
            "ann inc": [],
            "unc": [],
        },
    }

    # Parse data
    for row in lines[60:]:
        yr, ann_inc, unc = row.split()

        date = datetime(year=int(yr), month=1, day=1)

        if start and start > date:
            continue

        if end and end < date:
            break

        mean["data"]["yr"].append(yr)
        mean["data"]["ann inc"].append(ann_inc)
        mean["data"]["unc"].append(unc)

    return mean


def weekly_mean(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None
) -> dict:
    """
    NOTE: DATA FOR THE LAST SEVERAL MONTHS ARE PRELIMINARY, ARE STILL SUBJECT
    TO QUALITY CONTROL PROCEDURES.
    NOTE: The week "1 yr ago" is exactly 365 days ago, and thus does not run from
    Sunday through Saturday. 365 also ignores the possibility of a leap year.
    The week "10 yr ago" is exactly 10*365 days +3 days (for leap years) ago.
    """
    if start and not isinstance(start, datetime):
        raise TypeError("Start must be a datetime object")
    if end and not isinstance(end, datetime):
        raise TypeError("End must be a datetime object")

    url = "https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2/co2_weekly_mlo.txt"
    res = requests.get(url)
    raw = res.content.decode("utf-8")
    lines = raw.splitlines()
    _license = "\n".join(lines[:41])
    description = "\n".join(lines[41:47])
    headers = "\n".join(lines[47: 49])

    mean = {
        "url": url,
        "license": _license,
        "description": description,
        "headers": headers,
        "raw": raw,
        "data": {
            "yr": [],
            "mon": [],
            "day": [],
            "decimal": [],
            "ppm": [],
            "#days": [],
            "1 yr ago": [],
            "10 yr ago": [],
            "since 1800": []
        },
    }

    # Parse data
    for row in lines[49:]:
        yr, mon, day, decimal, ppm, days, _1yr, _10yr, _1800 = row.split()

        date = datetime(year=int(yr), month=int(mon), day=int(day))

        if start and start > date:
            continue

        if end and end < date:
            break

        mean["data"]["yr"].append(yr)
        mean["data"]["mon"].append(mon)
        mean["data"]["day"].append(day)
        mean["data"]["decimal"].append(decimal)
        mean["data"]["ppm"].append(ppm)
        mean["data"]["#days"].append(days)
        mean["data"]["1 yr ago"].append(_1yr)
        mean["data"]["10 yr ago"].append(_10yr)
        mean["data"]["since 1800"].append(_1800)

    return mean
