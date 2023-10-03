import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessHour
from functools import lru_cache
from time import perf_counter
from functools import wraps

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