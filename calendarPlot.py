# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:52:41 2019

@author: Man Vinayaka
"""

#!/usr/bin/env python
# coding: utf-8



import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy  import array

mydata = pd.read_csv("mydata.csv")
#print(mydata.head())

pm10 = mydata.pm10
o3 = mydata.o3
ws = mydata.ws
wd = mydata.wd
nox = mydata.nox
no2 = mydata.no2
pm25 = mydata.pm25



def calendar_array(dates, data):
    
    i, j = zip(*[d.isocalendar()[1:] for d in dates])
    i = np.array(i) - min(i)
    j = np.array(j) - 1
    ni = max(i) + 1

    calendar = np.nan * np.zeros((ni, 7))
    calendar[i, j] = data
    return i, j, calendar


def calendar_heatmap(ax, dates, data):
    i, j, calendar = calendar_array(dates, data)
    im = ax.imshow(calendar, interpolation='none', cmap='YlOrRd')
    label_days(ax, dates, i, j, calendar)
   # ax.figure.colorbar(im)


def label_days(ax, dates, i, j, calendar):
    ni, nj = calendar.shape
    day_of_month = np.nan * np.zeros((ni, 7))
    day_of_month[i, j] = [d.day for d in dates]

    for (i, j), day in np.ndenumerate(day_of_month):
        if np.isfinite(day):
            ax.text(j, i, int(day), ha='center', va='top')
            ################
            ax.arrow(j, i, avg_ws[int(day)-1+a]*np.cos(avg_wd[int(day)-1+a]*np.pi/180.)/15., 
                                  -avg_ws[int(day)-1+a]*np.sin(avg_wd[int(day)-1+a]*np.pi/180.)/15.,
                                  head_width=0.05, head_length=.1, fc='k', ec='k')
            ##################
    ax.set(xticks=np.arange(7), 
           xticklabels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    ax.xaxis.tick_top()


#############
df = pd.read_csv("mydata.csv")
df.index= pd.to_datetime(df.date)
df = df.drop("date", axis=1)
df_2003= df['2003'].resample("1D").mean()
df_2003 = df_2003.fillna(method='ffill')
df_2003['month'] = df_2003.index.month
df_2003.index.dayofweek

t = 1
fig,ax = plt.subplots(figsize=(10,10), nrows=4, ncols=3)


while t<=12:
    
    avg_ws = []
    avg_wd = []
    avg_pm25 = []
    df_2003_1 = df_2003[df_2003.month==t]
    avg_wd = df_2003_1['wd']
    avg_ws = df_2003_1['ws']
    avg_pm25 = df_2003_1['pm25']
    print(avg_wd[0:5])
    
    #############
    i = 1
    a = 0
    b = len(avg_pm25)
    while i<=1:
        data = avg_pm25[a:b]
        num = len(data)
        if t ==12:
            start = dt.datetime(2003, 1, 1)
        else:
            start = dt.datetime(2003, t, 1)
        dates = [start + dt.timedelta(days=i) for i in range(num)] 
        #fig,ax = plt.subplots(figsize=(10,10))
        #plt.subplot(4,3,t)
        #axes = fig.add_subplot(4, 3, t)
        #fig, ax = plt.subplots(nrows=4, ncols=3)
        month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        ax[(t-1)//3][(t-1)%3].set_title(month_labels[t-1])
        calendar_heatmap(ax[(t-1)//3][(t-1)%3], dates, data)
        i = i+1
    t = t+1 

plt.tight_layout()
    #plt.subplot(4,3,t-1)
plt.show()
x = range(10)
y = range(10)



plt.show()
plt.close('all')






