# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:50:49 2019

@author: Man Vinayaka
"""
def timeVariation(df,pollutant):

    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy  import array
    
    dayWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    
    df.index= pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_new= df
    df_new = df_new.fillna(method='ffill')
    df_new['month'] = df_new.index.month
    df_new['day']=df_new.index.dayofweek
    df_new['hour']=df_new.index.hour
    
    x = 0
    sub = 1
    
    while x<7:
        monday = []
        a = df_new[df_new.day==x]
        i = 0
        plt.figure(1,figsize=(50, 3))
        
        while i<24:
            b = a[a.hour==i]
            c = b[pollutant].mean()
            i = i+1
            monday.append(c)
        df_1 = pd.DataFrame(monday)
        df_1.columns = [pollutant]
        #plt.figure(1)
        plt.subplot(1,7,sub)
        plt.subplots_adjust(wspace = .2)
        sub = sub+1
        a = df_1[pollutant].plot.line(color="#ff9999")
        #a.axes.get_xaxis().set_visible(False)
        a.yaxis.set_label_position("left")
        plt.ylabel(pollutant)
        plt.xlabel('hours')
        plt.ylim((20,70))
        plt.xlim((0,23))
        plt.title(dayWeek[x])
        plt.grid()
        
        x = x+1
        
    a = df_new
    hourly = []
    i = 0
    plt.figure(2,figsize=(30, 3))
    while i<24:
            b = a[a.hour==i]
            c = b[pollutant].mean()
            i = i+1
            hourly.append(c)
    df_1 = pd.DataFrame(hourly)
    df_1.columns = [pollutant]      
    #print(df_1)
    plt.subplot(1,3,1)
    a = df_1[pollutant].plot.line(color="#ff9999")
        #a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("left")
    plt.ylabel(pollutant)
    plt.xlabel('hour')
    plt.ylim((20,45))
    plt.xlim((0,23))
    plt.grid()
    
    a = df_new.fillna(method='ffill')
    #print(df_new)
    monthly = []
    i = 0
    plt.figure(2,figsize=(30, 3))
    while i<12:
            b = a[a.month==i]
            c = b[pollutant].mean()
            i = i+1
            monthly.append(c)
    #print((monthly))
    df_1 = pd.DataFrame(monthly)
    df_1.columns = [pollutant]      
    #print(df_1)
    plt.subplot(1,3,2)
    a = df_1[pollutant].plot.line(color="#ff9999")
        #a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("left")
    plt.ylabel(pollutant)
    plt.xlabel('month')
    plt.ylim((30,40))
    plt.xlim((0,12))
    plt.grid()
    #print(c)
    x = 0
    weekday = []
    while x<7:
        monday = []
        a = df_new[df_new.day==x]
        i = 0
        plt.figure(2,figsize=(30, 3))
        
        while i<24:
            b = a[a.hour==i]
            c = b[pollutant].mean()
            i = i+1
            monday.append(c)
        df_1 = pd.DataFrame(monday)
        df_1.columns = [pollutant]
        weekday.append(df_1.mean())
        x= x+1
    #print(weekday)
    weekday = pd.DataFrame(weekday)
    weekday.columns = [pollutant]
    plt.subplot(1,3,3)
    a = weekday[pollutant].plot.line(color="#ff9999")
    a.yaxis.set_label_position("left")
    plt.ylabel(pollutant)
    plt.xlabel('weekday')
    plt.ylim((26,40))
    plt.xlim((0,6))
    plt.grid()





# =============================================================================
# df = pd.read_csv("mydata.csv")
# timeVariation(df,'pm10')
# =============================================================================
