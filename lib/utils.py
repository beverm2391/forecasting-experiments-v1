import numpy as np
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessHour

def log_returns(series):
    return np.log(series).diff()

def get_polygon_root() -> str:
    """Returns the root directory of the polygon data."""
    return "/Users/beneverman/Documents/Coding/bp-quant/shared_data/POLYGON/"

def get_polygon_freq() -> pd.offsets.CustomBusinessDay:
    return pd.offsets.CustomBusinessDay(calendar=USFederalHolidayCalendar())

def get_hourly_market_freq() -> pd.offsets.CustomBusinessHour:
    return pd.offsets.CustomBusinessHour(calendar=USFederalHolidayCalendar(), start="9:30", end="16:00")