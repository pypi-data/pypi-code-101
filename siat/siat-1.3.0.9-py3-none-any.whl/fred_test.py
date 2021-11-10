# -*- coding: utf-8 -*-

import pandas as pd
#if you get an error after executing the code, try adding below:
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2021, 1, 1)
end = datetime.datetime(2021, 10, 30)

sp500 = web.DataReader(['sp500'], 'fred', start, end)
djia = web.DataReader(['djia'], 'fred', start, end)

hk50 = web.DataReader(['hk50'], 'fred', start, end)
