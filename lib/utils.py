import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessHour
from functools import lru_cache
from time import perf_counter
from functools import wraps
import yfinance as yf

# ! Functions =========================================================================================================
def returns(y: pd.Series): return y.pct_change()
def log_returns(y: pd.Series): return np.log(y).diff()
def squared_returns(y: pd.Series): return y.pct_change()**2

def hv(series: pd.Series, annualization_factor: int = 252) -> pd.Series:
    """Historical Volatility"""
    return series.diff().rolling(annualization_factor).std() * np.sqrt(annualization_factor)

def rv(series: pd.Series, window: int) -> pd.Series:
    """
    Realized volatility is defined in [Volatility Forecasting with Machine Learning
    and Intraday Commonality](https://arxiv.org/pdf/2202.08962.pdf) as:

    $$RV_{i,t}(h)=\log(\sum_{s=t-h+1}^{t}r^2_{i,s})$$
    """
    assert window > 0, "Window must be greater than 0"
    fuzz = 1e-10
    log_returns = np.log(series).diff() # log returns
    sum_of_squares = log_returns.rolling(window=window).apply(lambda x: np.sum(x**2), raw=True)
    rv = np.log(sum_of_squares + fuzz)
    assert rv.isna().sum() == window, "RV should have NaNs at the beginning" # ? should have one nan from logret and window - 1 from rolling = window
    return rv

# ! Data Utils ==============================================================================================================
def get_polygon_root() -> str:
    """Returns the root directory of the polygon data."""
    return "/Users/beneverman/Documents/Coding/bp-quant/shared_data/POLYGON/"

def get_polygon_freq() -> pd.offsets.CustomBusinessDay:
    return pd.offsets.CustomBusinessDay(calendar=USFederalHolidayCalendar())

def get_hourly_market_freq() -> pd.offsets.CustomBusinessHour:
    return pd.offsets.CustomBusinessHour(calendar=USFederalHolidayCalendar(), start="9:30", end="16:00")

@lru_cache
def get_AAPL():
    return yf.download("AAPL", start="2019-01-01", end="2020-01-01", interval='1d')

@lru_cache # cache the result of this function to avoid refetching
def get_sp500():
    """Returns a dataframe of the S&P 500 companies."""
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df

# ! Decorators ========================================================================================================
def time_it(message=None): # decorator factory
    """
    Decorator factory that returns a decorator that prints the time it takes to run a function.
    """
    def decorator(func): # decorator
        @wraps(func) # preserves the name and docstring of the decorated function
        def wrapper(*args, **kwargs): # wrapper
            start = perf_counter() 
            result = func(*args, **kwargs)
            end = perf_counter()
            print(f"{message if message else f'Function {func.__name__}'} took {end - start:.02f}s")
            return result
        return wrapper
    return decorator

def try_it(func):
    """
    Decorator that wraps a function in a try-except block.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception: {e}")
    return wrapper