## ES(E-mini S&P 500 Futures)/SPX Studies
* [General info](#general-info)
* [Methodology](#methodology)
* [SW & libraries](#sw-&-libraries)
* [Data](#data)
* [Seasonality Example](#seasonality-example)

## General info
This project is simple group of statistical studies with an intention to understand general behaviour of the market. Ideas and observations are tested on past data to give us an quantifiable results for possible future probabilities.

## Methodology
Usually a three steps process is:
* CSV data are cleaned, transformed, aggregated, grouped based on current requirements. 
* Studies are programmed and run in Python.
* Output is generated in visually easy to interpret chart/heatmap/table to give us clear picture/probability of study.

## SW & libraries
Project is created with:
* PyCharm 2021 (Community Edition)
* Python version: 3.8.5
* Python libraries: matplotlib, pandas,  mplfinance, matplotlib, seaborn, numpy 

## Data
* Daily OHLC 1962-2020 SPX
* Daily OHLC 1928-2020 SPX
* Intraday 1 minute ES-futures continuous contract OHLCV 2010-2020
* CME Daily E-mini S&P 500 Futures continuous contract OHLCV 1997-2020

## Seasonality Example
* Seasonality is well calendar effect in markets worth investigating in case of planning trading/investing for longer period of time. Seasonal patterns are constructed by plotting daily data against calendar/trading days rather than simply averaging daily/weekly/monthly data. Such daily data has proven to be far more valuable when looking for consistent and precise entry and exit dates.
* The following chart reflect seasonal patterns for SPX index over the period of a calendar year. Long term studies tend to survive for decades and as we can see very little changes of long term seasonal patterns occured during last 60 years.
![SPX year](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/Y%20seasonality.png)
* Closer look on individual months will help with timeing entries and exists. For example: second half of October is usually good time to initiate long term LONG possition in SPX/ES/SPDR with a potential of holding till the end of the calendar year and catching historically strongest period of the year.
![SPX October](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/10_October.png)

## ---
Past performance is not indicative of future results. Data and information provided may be delayed. Data and information is provided for informational purposes only, and is not intended for trading purposes.
