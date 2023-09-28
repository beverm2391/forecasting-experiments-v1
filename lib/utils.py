import numpy as np

def log_returns(series):
    return np.log(series).diff()