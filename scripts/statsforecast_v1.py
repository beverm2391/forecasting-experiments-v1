import pandas as pd
import numpy as np
from statsforecast import StatsForecast
from statsforecast.models import ARCH, GARCH, Naive
import yfinance as yf
from typing import List, Union
import random
from time import perf_counter

from lib.statsforecast import preprocess_yf
from lib.utils import log_returns

def fetch_data(tickers: Union[str, List[str]], start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Fetches data from Yahoo Finance API
    """
    df = yf.download(tickers, start=start, end=end, interval=interval)
    return df

def main():
    # ! YOUR PARAMETERS HERE ================================================================
    
    # data
    tickers = ["AAPL", "MSFT"]
    start = "2018-01-01"
    end = "2022-12-13"
    interval = "1d"

    # models
    models = [
        Naive(),
        ARCH(),
        GARCH()
    ]

    # forecasts
    horizon = 3
    levels = [80, 95]
    path = "/Users/beneverman/Documents/Coding/bp-quant/forecasting-experiments-v1/data/forecasts"

    # ! ====================================================================================

    # Fetch data
    print(f"Fetching data for {tickers} from {start} to {end} with interval {interval}...")
    s = perf_counter()

    df = fetch_data(tickers, start, end, interval)

    el = perf_counter() - s
    print(f"Data fetched in {el:.02f}s")

    # Preprocess data
    print("Preprocessing data...")
    df = preprocess_yf(df, log_returns)

    # Forecast
    print("Generating forecasts...")
    s = perf_counter()

    sf = StatsForecast(
        df = df, 
        models = models, 
        freq = "D",
        n_jobs = -1
    )

    forecasts = sf.forecast(h=horizon, level=levels)
    forecasts.reset_index(inplace=True)

    el = perf_counter() - s
    print(f"Forecasts generated in {el:.02f}s")

    # Save forecasts
    print(f"Saving forecasts to {path}...")
    forecasts.to_csv(f"{path}_forecast_{random.randint(0, 9999)}.csv")

    print("Complete")

if __name__ == "__main__":
    main()