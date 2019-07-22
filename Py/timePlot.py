# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:50:55 2019

@author: Man Vinayaka
"""


def timePlot(df,year,month):
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    df.index= pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_n= df[year]
    df_n = df_n.fillna(method='ffill')
    df_n['month'] = df_n.index.month
    df_n.index.dayofweek
    df_n_1 = df_n[df_n.month==month]
    ws = df_n_1['ws']
    nox = df_n_1['nox']
    o3 = df_n_1['o3']
    pm25 = df_n_1['pm25']
    pm10 = df_n_1['pm10']
    plt.figure(1)
    plt.subplot(511)
    a = nox.plot.line(color="red")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel('nox')
    #plt.x_axis('off')
    plt.subplot(512)
    a = o3.plot.line(color="blue")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel('o3')
    plt.subplot(513)
    a = pm25.plot.line(color="green")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel('pm25')
    plt.subplot(514)
    a = pm10.plot.line(color="purple")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel('pm10')
    plt.subplot(515)
    a = ws.plot.line(color="orange")
    a.yaxis.set_label_position("right")
    plt.ylabel('ws')
    #plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #fancybox=True, shadow=True, ncol=5)

    #a.axes.get_xaxis().set_visible(False)
    #print(df_n_1)
# =============================================================================
# mydata = pd.read_csv('mydata.csv')
# #selectByDate(mydata,'2003',8)
# timePlot(mydata,'2003',8)
# =============================================================================
