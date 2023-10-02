import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessHour
from functools import lru_cache

def returns(y: pd.Series): return y.pct_change()
def log_returns(y: pd.Series): return np.log(y).diff()

def get_polygon_root() -> str:
    """Returns the root directory of the polygon data."""
    return "/Users/beneverman/Documents/Coding/bp-quant/shared_data/POLYGON/"

def get_polygon_freq() -> pd.offsets.CustomBusinessDay:
    return pd.offsets.CustomBusinessDay(calendar=USFederalHolidayCalendar())

def get_hourly_market_freq() -> pd.offsets.CustomBusinessHour:
    return pd.offsets.CustomBusinessHour(calendar=USFederalHolidayCalendar(), start="9:30", end="16:00")

@lru_cache # cache the result of this function to avoid refetching
def get_sp500():
    """Returns a dataframe of the S&P 500 companies."""
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df