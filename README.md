# Time Series Model Experiments

## Completed
- [X] copy polygon data into here, or keep it centralized somewhere
- [X] Fix preprocess multi-index
- [X] Create a script for generating forecasts from statsforecasting models
  
## TODO
- [ ] Figure out the best ARCH and GARCH models for a group of stocks
  - [ ] Create a script for training and evaluating statsforecasting models

## Resources

### Tips and Tricks
- [Pandas melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) - Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

### Documentation
- [Pandas available frequencies](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)
- [Seasonality by Rob J Hyndman](https://robjhyndman.com/hyndsight/seasonal-periods/) (what's my frequency argument?)

### Datasets
- [Air passengers]('https://datasets-nixtla.s3.amazonaws.com/air-passengers.csv')
- [M4 Hourly](https://datasets-nixtla.s3.amazonaws.com/m4-hourly.parquet')