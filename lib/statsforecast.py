import pandas as pd
from typing import Callable, Optional, List, Dict
import warnings

def preprocess_yf(df: pd.DataFrame, y_func: Callable[[pd.Series], pd.Series], \
                  yfunc_args: Optional[List] = [], yfunc_kwargs: Optional[Dict] = {}) -> pd.DataFrame:
    """
    Takes a yfinance price dataframe and returns a dataframe with columns: ds, unique_id (optional), y
    """
    def _is_multi_index(df): return type(df.columns) == pd.core.indexes.multi.MultiIndex

    def _process_single_index(df):
        df.reset_index(inplace=True)
        ds_colname = df.columns[0]
        df.rename(columns={ds_colname: 'ds'}, inplace=True) # rename ds column
        df.loc[:, 'y'] = df.loc[:, 'Adj Close'].agg(y_func, *yfunc_args, **yfunc_kwargs) # add log returns column
        df = df.loc[:, ['ds', 'y']] # keep only ds and y columns
        return df
    
    def _process_multi_index(df):
        warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)  #? ignore SettingWithCopyWarning

        tickers = df.columns.get_level_values(1).unique().tolist()
        df = df.loc[:, (['Adj Close'], tickers)] # just get adj close
        df.columns = df.columns.droplevel() # drop MultiIndex
        df = df.reset_index() # reset index
        ds_colname = df.columns[0] # get ds column name
        df.rename(columns={ds_colname: 'ds'}, inplace=True) # rename ds column
        prices = df.melt(id_vars='ds') # melt by ds index
        prices['y_func'] = prices.groupby('variable')['value'].transform(y_func, *yfunc_args, **yfunc_kwargs) # apply y_func to value (Adj Close)
        prices.rename(columns={'variable': 'unique_id', 'y_func' : 'y'}, inplace=True)
        prices.drop(columns='value', inplace=True) # rename columns
        return prices

    if _is_multi_index(df):
        return _process_multi_index(df)
    else:
        return _process_single_index(df)