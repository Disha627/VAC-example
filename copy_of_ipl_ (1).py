# -*- coding: utf-8 -*-
"""Copy of IPL_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WItpE-Qhm3U5fD21gjfDFOuezoY_1SMS
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("/content/data (1) (1).csv")
print(data)

data.info()

data.describe()

data.head(16)

data.tail(12)

data.groupby('season').count()

data.columns

data.isnull().sum()

sns.pairplot(data,hue="city")

sns.barplot(x='city',y='date',data=data)

sns.scatterplot(x='season',y='toss_decision',data=data)

win_by_runs=data['win_by_runs']
plt.plot(win_by_runs)
plt.show()