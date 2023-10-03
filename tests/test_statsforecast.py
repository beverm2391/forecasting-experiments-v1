import pandas as pd
import yfinance as yf
from functools import lru_cache
import os

from lib.statsforecast import preprocess_yf
from lib.utils import log_returns

base_path = "/Users/beneverman/Documents/Coding/bp-quant/forecasting-experiments-v1/data/tests"

def get_data_1():
    """
    1 stock daily
    """
    fname = "AAPL_2018-01-01_2022-12-13_1d.csv"
    fpath = f"{base_path}/{fname}"
    if not os.path.exists(fpath):
        df = yf.download('AAPL', start = '2018-01-01', end = '2022-12-31', interval='1d')
        df.to_csv(fpath)
    return pd.read_csv(fpath)


def get_data_2():
    """
    2 stocks daily
    """
    fname = "AAPL_MSFT_2018-01-01_2022-12-13_1d.csv"
    fpath = f"{base_path}/{fname}"
    if not os.path.exists(fpath):
        df = yf.download(['AAPL', 'MSFT'], start = '2018-01-01', end = '2022-12-31', interval='1d')
        df.to_csv(fpath)
    return pd.read_csv(fpath)

def test_preprocess_yf():
    data_1 = get_data_1()
    ppd_1 = preprocess_yf(data_1, log_returns)
    data_2 = get_data_1()
    ppd_2 = preprocess_yf(data_2, log_returns)