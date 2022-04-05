# Air cargo forecasting

Data based on [transstats](https://www.transtats.bts.gov/freight.asp).

Preparation - crawling the data from the site using [scrapy](https://scrapy.org/):
```[shell]
$ scrapy runspider ac_spider.py -O Data/AirCargoData.json
```

1. Importing and preparing the data.
2. Analysis of the time series.
3. Building the SARIMA model, prediction twelve months into the future.
4. Building the LSTM model, prediction twelve months into the future.
