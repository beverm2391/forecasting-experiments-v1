# Time Series Model Experiments

## Completed
- [ ] copy polygon data into here, or keep it centralized somewhere

## TODO
- [ ] Replicate tutorial with hourly data for ARCH and GARCH
- [ ] Build out a REST API to serve predictions (model_name, model_id, etc.)

## Resources

### Tips and Tricks
- [Pandas melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) - Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

### Documentation
- [Pandas available frequencies](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)
- [Seasonality by Rob J Hyndman](https://robjhyndman.com/hyndsight/seasonal-periods/) (what's my frequency argument?)

### Datasets
- [Air passengers]('https://datasets-nixtla.s3.amazonaws.com/air-passengers.csv')
- [M4 Hourly](https://datasets-nixtla.s3.amazonaws.com/m4-hourly.parquet')