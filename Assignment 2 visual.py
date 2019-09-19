# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:27:27 2019

@author: Calvin
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mydataset = pd.read_csv("HPI_master.csv")
df = pd.DataFrame(mydataset['period'])
df2 = pd.DataFrame(mydataset['index_sa'])
df3 = pd.DataFrame(mydataset[['index_sa','index_nsa']])
df4 = pd.DataFrame(mydataset[['index_nsa']])


#period line graph
plt.figure()
df.plot.line()
plt.title("Period Line Graph")
plt.xlabel("Entry")
plt.ylabel("Period")
plt.show()

#index_sa line graph
plt.figure()
df2.plot.line()
plt.title("Index_sa line graph")
plt.xlabel("Entry Number")
plt.ylabel("Index_Sa")
plt.show()

#period bar graph
plt.figure()
df.period.value_counts().plot.bar()
plt.title("Period Bar Graph")
plt.xlabel("Period")
plt.ylabel("Number of entries")
plt.show()

#index_sa histogram
plt.figure()
df2.plot.hist()
plt.title("index_sa histogram")
plt.show()

#period pie chart
plt.figure()
df.period.value_counts().plot.pie()
plt.title("Period Pie Chart")
plt.show()

#index_sa/index_nsa scatter
plt.figure()
df3.plot.scatter(x='index_sa', y = 'index_nsa')
plt.title('index_sa and index_nsa scatter plot')
plt.show()

#3d map
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(df, df2, df4, c = 'r', marker = 'o')
plt.title("3D scatter plot")
plt.xlabel("Period")
plt.ylabel("index_sa")
plt.show()
