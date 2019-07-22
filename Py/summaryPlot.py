# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:48:26 2019

@author: Man Vinayaka
"""

def summaryPlot(df):
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy  import array
    import matplotlib.patches as mpatches
    import seaborn as sns
    from matplotlib.pyplot import figure
    class color:
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    
    df.index= pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_all= df.resample("1D")
    df_all = df_all.fillna(method='ffill')
    dataPoints = ['pm25','co','so2','pm10','o3','no2','nox','wd','ws']
    #print(df_all)
    
    i = 0
    sub = 1
    while i<9:
    
        plt.figure(i+1,figsize=(50, 50))
        plt.subplot(9,2,sub)
        sub = sub+1
        a = df_all[dataPoints[i]].plot.line(color="gold")
        a.axes.get_xaxis().set_visible(False)
        a.yaxis.set_label_position("left")
        plt.ylabel(dataPoints[i],fontsize=75,bbox=dict(facecolor='whitesmoke'))
        #print(df['pm25'].max())
        
        plt.subplot(9,2,sub)
        sub = sub + 1
        plt.hist(df_all[dataPoints[i]],bins = 50,color = 'green')
        i = i+1
    i = 0
    while i<9:
        nDf = df[dataPoints[i]]
        missing = nDf.isna().sum() + sum(n < 0 for n in nDf)
        minVal = nDf.min()
        maxVal = nDf.max()
        meanVal = nDf.mean()
        medianVal = nDf.median()
        percentile = nDf.quantile(0.95)
        print('---------------')
        print(color.BOLD + color.UNDERLINE+dataPoints[i]+ color.END)
        print('min = '+ str(0))
        print('max = '+ str(maxVal))
        print('missing = '+ str(missing))
        print('mean = '+ str(meanVal))
        print('median = '+ str(medianVal))
        print('95th percentile = '+ str(percentile))
        i = i+1

#df = pd.read_csv('mydata.csv')
#summaryPlot(df)