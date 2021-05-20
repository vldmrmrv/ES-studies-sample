## ES(E-mini S&P 500 Futures)/SPX Studies
* [General info](#general-info)
* [Methodology](#methodology)
* [SW & libraries](#sw-&-libraries)
* [Data](#data)
* [Seasonality Example](#seasonality-example)
* [Mid term study Example](#mid-term-study-example)
* [Short term study Example](#short-term-study-example)

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
* Python libraries: matplotlib, pandas,  mplfinance, seaborn, numpy 

## Data
* Daily OHLC 1928-2020 SPX
* Intraday 1 minute ES-futures continuous contract OHLCV 2010-2020
* Intraday tick data ES-futures continuous contract 2017-2020
* CME Daily E-mini S&P 500 Futures continuous contract OHLCV 1997-2020

## Seasonality Example
* Seasonality is well calendar effect in markets worth investigating in case of planning trading/investing for longer period of time. Seasonal patterns are constructed by plotting daily data against calendar/trading days rather than simply averaging daily/weekly/monthly data. Such daily data has proven to be far more valuable when looking for consistent and precise entry and exit dates.
* The following chart reflect seasonal patterns for SPX index over the period of a calendar year. Long term studies tend to survive for decades and as we can see very little changes of long term seasonal patterns occured during last 60 years.
![SPX year](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/Y%20seasonality.png)
* Closer look on individual months will help with timeing entries and exists. For example: second half of October is usually good time to initiate long term LONG possition in SPX/ES/SPDR with a potential of holding till the end of the calendar year and catching historically strongest period of the year.
![SPX October](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/10_October.png)

## Mid term study Example
*  Study of weekly volatility during the year. Data for last 20 years indicates October is the most volatile month of the year.
![Weekly RNG](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/004_heatmap_W_pR_HL_mean.png) 

## Short term study Example
*  Releationship between RTH range and IB range for different opening types and days of the week. Useing Seaborn-Implot to fit regression models across conditional subsets of a dataset.
'''python
sns.lmplot(data=df, x='IB_RNG', y='RTH_RNG', col='DoW', hue="OOR", height=5)
plt.show()
'''
![Implot RNG](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/002_lmplot_of_IB_rng_and_RTH_rng_SAMPLE.png)

## ---
Past performance is not indicative of future results. Data and information provided may be delayed. Data and information is provided for informational purposes only, and is not intended for trading purposes.
