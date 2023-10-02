import pandas as pd
from typing import Callable

def preprocess_yf(df: pd.DataFrame, y_func: Callable[[pd.Series], pd.Series]):
    """
    Takes a yfinance price dataframe and returns a dataframe with columns:
    """
    def _is_multi_index(df): return type(df.columns) == pd.core.indexes.multi.MultiIndex

    if _is_multi_index(df):
        tickers = df.columns.get_level_values(1).unique().tolist()
        df = df.loc[:, (['Adj Close'], tickers)] # just get adj close
        df.columns = df.columns.droplevel() # drop MultiIndex
        df = df.reset_index() # reset index
        ds_colname = df.columns[0] # get ds column name
        df.rename(columns={ds_colname: 'ds'}, inplace=True) # rename ds column
        prices = df.melt(id_vars='ds') # melt by ds index
        prices['y_func'] = prices.groupby('variable')['value'].transform(y_func) # apply y_func to value (Adj Close)
        prices.rename(columns={'variable': 'unique_id', 'y_func' : 'y'}, inplace=True)
        prices.drop(columns='value', inplace=True) # rename columns
        return prices
    else:
        df.reset_index(inplace=True)
        ds_colname = df.columns[0]
        df.rename(columns={ds_colname: 'ds'}, inplace=True) # rename ds column
        df.loc[:, 'y'] = df.loc[:, 'Adj Close'].agg(y_func) # add log returns column
        df = df.loc[:, ['ds', 'y']] # keep only ds and y columns
        return df