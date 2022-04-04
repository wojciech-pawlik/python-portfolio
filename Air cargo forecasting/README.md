# Air cargo forecasting

## v1
Data based on [kaggle](https://www.kaggle.com/rajsengo/sfo-air-traffic-passenger-and-cargo-statistics).

1. The optimal way to group the data.
2. Transformation to time series.
3. Analysis of the time series.
4. Building the multivariate LSTM model.
5. Prediction one month into the future by previous year quantities.

## v2
Data based on [transstats](https://www.transtats.bts.gov/freight.asp).

Preparation - crawling the data from the site using [scrapy](https://scrapy.org/):
`!scrapy runspider ac_spider.py -O Data/AirCargoData.json`

1. Importing and preparing the data.
2. Analysis of the time series.
3. Building the SARIMA model, prediction twelve months into the future.
4. Building the LSTM model, prediction twelve months into the future.
