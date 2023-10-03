import pandas as pd
import numpy as np
from statsforecast import StatsForecast
from statsforecast.models import ARCH, GARCH, Naive
import yfinance as yf
from functools import lru_cache
from typing import List, Union
import random

from lib.statsforecast import preprocess_yf
from lib.utils import log_returns, try_it, time_it

data_path = "../data/tests/AAPL_MSFT_2018-01-01_2022-12-13_1d.pkl"
df = pd.read_pickle(data_path)

@try_it
@time_it("Data fetched in")
@lru_cache
def fetch_data(tickers: Union[str, List[str]], start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Fetches data from Yahoo Finance API
    """
    return yf.download(tickers, start=start, end=end, interval=interval)

@try_it
@time_it("Data preprocessed in")
def preprocess_data(*args, **kwargs): return preprocess_yf(*args, **kwargs)

@try_it
def model(df, models, freq, n_jobs=-1):
    sf = StatsForecast(
        df = df, 
        models = models, 
        freq = freq,
        n_jobs = n_jobs
    )
    return sf

@try_it
@time_it("Forecasts generated in")
def forecast(sf: StatsForecast, h: int, levels: List[int]):
    levels = [80, 95] # confidence levels for the prediction intervals 
    forecasts = sf.forecast(h=h, level=levels)
    forecasts.reset_index(inplace=True)
    return forecasts

@try_it
@time_it("Forecasts saved in")
def save_forecasts(forecasts, path):
    forecasts.to_pickle(path)

def main():
    # ! YOUR PARAMETERS HERE ================================================================
    
    # data
    tickers = ["AAPL", "MSFT"]
    start = "2018-01-01"
    end = "2022-12-13"
    interval = "1d"

    # models
    models = [Naive, ARCH, GARCH]

    # forecasts
    horizon = 3
    levels = [80, 95]
    path = "/Users/beneverman/Documents/Coding/bp-quant/forecasting-experiments-v1/data/forecasts"

    # ! ====================================================================================


    df = fetch_data(tickers, start, end, interval)
    df = preprocess_data(df)
    sf = model(df, models, freq="MS")
    forecasts = forecast(sf, h=horizon, levels=levels if levels else None)
    save_forecasts(forecasts, f"{path}_{random.randint(0, 999)}")

if __name__ == "__main__":
    main()