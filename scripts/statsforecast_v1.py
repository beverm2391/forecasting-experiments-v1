import pandas as pd
import numpy as np
from statsforecast import StatsForecast
from statsforecast.models import ARCH, GARCH, Naive
import yfinance as yf
from functools import lru_cache
from typing import List, Union

from lib.statsforecast import preprocess_yf
from lib.utils import log_returns

data_path = "../data/tests/AAPL_MSFT_2018-01-01_2022-12-13_1d.pkl"
df = pd.read_pickle(data_path)

@lru_cache
def fetch_data(tickers: Union[str, List[str]], start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Fetches data from Yahoo Finance API
    """
    return yf.download(tickers, start=start, end=end, interval=interval)

def main():
    tickers = ["AAPL", "MSFT"]
    start = "2018-01-01"
    end = "2022-12-13"
    interval = "1d"




if __name__ == "__main__":
    main()