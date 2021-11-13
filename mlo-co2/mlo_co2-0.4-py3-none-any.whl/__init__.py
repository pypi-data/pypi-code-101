"""
mlo_co2
-------

Mauna Loa Observatory Carbon Dioxide Data Scraper

This Python package includes a script to scrape the NOAA Earth Science Research Lab for Carbon Dioxide (CO2) readings from the Mauna Loa Observatory in Hawai'i.
You can access this data here: [https://www.esrl.noaa.gov/gmd/ccgg/trends/mlo.html](https://www.esrl.noaa.gov/gmd/ccgg/trends/mlo.html)
"""

from .mlo_co2 import monthly_mean, annual_mean, annual_mean_increase, weekly_mean

__all__ = [
    'monthly_mean', 'annual_mean', 'annual_mean_increase', 'weekly_mean'
]
