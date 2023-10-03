import pandas as pd
import yfinance as yf
from functools import lru_cache

from lib.statsforecast import preprocess_yf
from lib.utils import log_returns


@lru_cache
def _cache_data_1():
    df = yf.download(tickers='AAPL', start = '2018-01-01', end = '2022-12-31', interval='1d')
    return df

@lru_cache
def _cache_data_2():
    df = yf.download(['AAPL', 'MSFT'], start = '2018-01-01', end = '2022-12-31', interval='1d')
    return df

def test_preprocess_yf():
    data_1 = _cache_data_1()
    ppd_1 = preprocess_yf(data_1, log_returns)

    data_2 = _cache_data_2()
    ppd_2 = preprocess_yf(data_2, log_returns)
