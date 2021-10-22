## ES(E-mini S&P 500 Futures)/SPX Studies
* [General info](#general-info)
* [Methodology](#methodology)
* [SW & libraries](#sw-&-libraries)
* [Data](#data)
* [Seasonality Example](#seasonality-example)
* [Mid term study Example](#mid-term-study-example)
* [Short term study Example](#short-term-study-example)
* [HiLo of the Month Example](#hilo-month-example)

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
* Heatmap of SPX index (sum of percentage change for last 10 years) showing weak seasonalities during August and second half of September. Strong up trend (% up move) can be expected during first half of April. 

![Heat year](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/00a_heatmap_p_Open%20to%20Close%20_%20UPDOWN%20(RTH%20range).png)
* Closer look on individual months will help with timeing entries and exists. For example: second half of October is usually good time to initiate long term LONG possition in SPX/ES/SPDR with a potential of holding till the end of the calendar year and catching historically strongest period of the year.

![SPX October](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/000_seasonality_all/10_October.png)

## Mid term study Example
*  Study of weekly volatility during the year. Data for last 20 years indicates October is the most volatile month of the year.

![Weekly RNG](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/004_heatmap_W_pR_HL_mean.png) 

## Short term study Example
*  Releationship between RTH range and IB range for different opening types and days of the week. Useing Seaborn-Implot to fit regression models across conditional subsets of a dataset.
```python
sns.lmplot(data=df, x='IB_RNG', y='RTH_RNG', col='DoW', hue="OOR", height=5)
plt.show()
```

![Implot RNG](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/002_lmplot_of_IB_rng_and_RTH_rng_SAMPLE.png)

*  Simple intraday study of RTH High and Low in S&P500 futures (15 minutes dataset, 2010-2020). How often is High or Low of the cash session made in first one hour of trading ?

```python
sns.set_theme(style="whitegrid")
sns.barplot(x="time", y="prcnt", data=df, ci=None, palette="mako")
plt.xticks(rotation=70)
plt.suptitle('High or Low of the RTH session (%) 2010-2020')
plt.show()
```

![Bar2plot RNG](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/017_ES_RTH_HiLo.png)

## High & Low of the Month Study
*  Not all buyers and sellers try to time the market. The U.S. stock market has been used as a long-term investment for retirement portfolios for decades, and the amount of money being moved in and out of the market has increased significantly during the past 20 years, Institutions, such as Vanguard and Fidelity, that control IRAs, 401K, and other retirement plans have an obligation to put new money into the market, or redeem it, by the EOM. Not all investments have daily liquidity. In addition, some firms must realize their gains or losses at the EOM for accounting purposes. Non U.S. firms, investing in the U.S. markets, may close out their profitable positions at the EOM and repartiate their gains. Based on those information we may try and test if there is any significant and usefull edge for trading US indices.
*  Starting with 1Minute dataset we will actually need to make new datasets by aggregationg data to 1D (daily) and 1M (monthly), merge them, compare High/Low conditions and groupby results.

* From timestamp/date column we will make new Day, Week, Month and Year colums that will be used for aggregation and grouping.
```python
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.dayofweek
df['Week'] = df['Date'].dt.isocalendar().week
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.isocalendar().year
```
* Making daily / monthly bars and merging datasets together.
```python
df2 = df.groupby(['Year', 'Month', 'Week', 'Day']).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
df3 = df.groupby(['Year', 'Month']).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
df4 = pd.merge(df2, df3, on=['Year', 'Month'])
```

* Checking if its Up or Down day and comparing its High/Low to High/Low of the Month. Final column 'signalBOTH' is True(1) if row made High in Down month ir Low in Up month (for now we care only about when is the best day of the month to enter a position).
```python
df['Hi'] = [1 if c == sma else 0 for c, sma in zip(df['High_x'], df['High_y'])]
df['Lo'] = [1 if c == sma else 0 for c, sma in zip(df['Low_x'], df['Low_y'])]
df['UD'] = [1 if c2 > c3 else 0 for c2, c3 in zip(df['Close_y'], df['Open_y'])]
df['Hi_D'] = [1 if c2 == 1 and c3 == 0 else 0 for c2, c3 in zip(df['Hi'], df['UD'])]
df['Lo_U'] = [1 if c2 == 1 and c3 == 1 else 0 for c2, c3 in zip(df['Lo'], df['UD'])]
df['signalBOTH'] = [1 if c2 == 1 or c3 == 1 else 0 for c2, c3 in zip(df['Hi_D'], df['Lo_U'])]
```

* Next main step would be to groupby and sum results based on Day of the Month and plot the results. We can always for example test more specific conditions like test only Up months and its Low of the month and see if there is bigger significance compare to testing Up and Down months together. There is plenty of options and combinations / "filters" that can be tested but overfitting it for specific market conditions/time period is usually conterproductive in a big picture.
```python
df2 = df.groupby(['DoM']).agg({'signalBOTH': 'sum'})
```
*  Dataset that we just made can answer questions like - What day of the month will probably make the low of the whole month? (Best time for opening a Buy and Hold possition is with a huge margin first day of the month - based on this test.

![LoM](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/011_M%20Lo%20v%20UM%20by%20TDoM.png) 

*  Heatmap showing when are Highs and Lows of months made. (Best time for opening and closing long term possitions is clearly start and end of the month)

![HLoM](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/010_heatmap_M_HoL_sum%20(RTH).png) 

## ---
Past performance is not indicative of future results. Data and information provided may be delayed. Data and information is provided for informational purposes only, and is not intended for trading purposes.
