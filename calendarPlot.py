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
    im = ax.imshow(calendar, interpolation='none', cmap='coolwarm')
    label_days(ax, dates, i, j, calendar)
    label_months(ax, dates, i, j, calendar)
    ax.figure.colorbar(im)
    
    #ax.figure.colorbar(figsize=(10, 10))

def label_days(ax, dates, i, j, calendar):
    ni, nj = calendar.shape
    day_of_month = np.nan * np.zeros((ni, 7))
    day_of_month[i, j] = [d.day for d in dates]

    for (i, j), day in np.ndenumerate(day_of_month):
        if np.isfinite(day):
            #print(ax)
# =============================================================================
#             if j ==12:
#                 day = day+1
# =============================================================================
            ax.text(j, i, int(day), ha='center', va='top')
            if avg_ws[int(day)-1+a]<=5:
                ax.text(j,i,"    -->", ha = 'left', va = 'bottom', rotation = avg_wd[int(day)-1+a])#########
            elif avg_ws[int(day)-1+a]<=10:
                ax.text(j,i,"    ---->", ha = 'left', va = 'bottom', rotation = avg_wd[int(day)-1+a])#########
            elif avg_ws[int(day)-1+a]>10 :
                ax.text(j,i,"    ------>", ha = 'left', va = 'bottom', rotation = avg_wd[int(day)-1+a])#########
            #print(avg_wd.dtype)
    ax.set(xticks=np.arange(7), 
           xticklabels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    ax.xaxis.tick_top()

def label_months(ax, dates, i, j, calendar):
    month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                             'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    months = np.array([d.month for d in dates])
    uniq_months = sorted(set(months))
    yticks = [i[months == m].mean() for m in uniq_months]
    labels = [month_labels[m - 1] for m in uniq_months]
    ax.set(yticks=yticks)
    ax.set_yticklabels(labels, rotation=90)

#############

df = pd.read_csv("mydata.csv")
avg_ws = []
for j in range(0,len(df),24):
    x = df["ws"][j:j+24].values
    x = x[~np.isnan(x)]
    avg_x = np.mean(x)
    avg_ws.append(avg_x)
avg_wd = []
for j in range(0,len(df),24):
    x = df["wd"][j:j+24].values
    x = x[~np.isnan(x)]
    avg_x = np.mean(x)
    avg_wd.append(avg_x)
avg_pm25 = []
for j in range(0,len(df),24):
    x = df["pm25"][j:j+24].values
    x = x[~np.isnan(x)]
    avg_x = np.mean(x)
    avg_pm25.append(avg_x)

avg_ws = array( avg_ws )
avg_ws=avg_ws.astype(np.int)
avg_wd = array( avg_wd )
avg_wd=avg_wd.astype(np.int)
#np.array(avg_wd, dtype=np.int32)

#############33
i = 1
a = 1826
b = 1857
while i<=12:
    data = avg_pm25[a:b]
    num = len(data)
    if i!=12:
        start = dt.datetime(2019, i, 1)
    elif i == 12:
        start = dt.datetime(2017, i, 2)
    dates = [start + dt.timedelta(days=i) for i in range(num)] 
    fig, ax = plt.subplots(figsize=(10,10))
    
    calendar_heatmap(ax, dates, data)
    #plt.subplot(4,3,i)
    i = i+1
    if i ==2:
        a = a+31
        b = b+28
    elif i==3:
        a = a+28
        b = b+31
    elif i%2!=0:
        a = a+30
        b = b+31
    elif i%2==0:
        a = a+31
        b = b+30
        
plt.show()
plt.close('all')






