"""Utility functions module."""


import pandas as pd


def convert_fx(timeseries, currency_pair, reverse, data_type='price'):
    """Convert a data frame of quotes or returns in one currency to a given currency

        Parameters
        ----------
        timeseries : pandas.core.series.Series
        pandas dataframe indexed by dates

        currency_pair: str
        Currency pair to convert.  Eg. BRL/USD , from price currency Brazilian Reais to base currency US Dolar

        data_type: str,optional
        price for monetary, or return for percentual changes

        reverse : bool
        when True, convert from base currency to price currency. Eg. BRL/USD , from US Dolar to Brazilian Reais 
            (Default value = False)

        Returns
        -------
        pandas.core.series.Series

        """
    if currency_pair == "BRL/USD":

        # Getting BRL/USD conversion rate from Brazilian Central Bank(BCB)

        url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json'
        df = pd.read_json(url)
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df.set_index('data', inplace=True)

        # returning results

        if reverse == False:
            return (1/df).mul(timeseries, axis=0).dropna()

        else:
            return df.mul(timeseries, axis=0).dropna()


def bcb_data(code, from_date="1800-01-01", to_date="2300-01-01", data_type="quote"):
    """Retrieve data from Brazilian Central Bank (BCB)

        Parameters
        ----------
        code : int
        data code for a given time series (consult https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries)

        from_date: str
        Initial date of desired time series YYYY-MM-DD

        to_date: str
        End date of desired time series YYYY-MM-DD

        data_type: str
        Enter "quote" for values, or 

        Returns
        -------
        pandas.core.series.Series

        """
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(
        code)

    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)
    data = df[(df.index >= from_date) & (df.index <= to_date)]

    if data_type == "quote":
        return data
