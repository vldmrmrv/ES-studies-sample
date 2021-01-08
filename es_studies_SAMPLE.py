import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.options.display.max_rows = 299
pd.options.display.max_columns = 99

df = pd.read_csv('es_data_raw.csv', sep=';')

print(df.head())

# 001 %change by day of the week
df3 = df[df['DoW'].isin(['1', '2', '3', '4', '5'])]
palette = sns.color_palette("flare", as_cmap=True)
sns.histplot(data=df3, x="prcnt", kde=True, element="step", hue="DoW", palette=palette, fill=False)
plt.show()

# 002 lmplot of IB rng vs RTH rng
sns.lmplot(data=df, x='IB_RNG', y='RTH_RNG', col='DoW', hue="OOR", height=5)
plt.show()

# 003 high of the week by day study - aggregate daily to weekly HiLo
weekly_limits = df.groupby(['Y', 'W']).agg({'BOTH_H': 'max', 'BOTH_L': 'min'}).reset_index()
weely_limits.to_csv('weekly.csv')

df_with_weekly_limits = pd.merge(df, weekly_limits, on=['Y', 'W'])
df_with_weekly_limits.to_csv('daily_weekly_together.csv')
