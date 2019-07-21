# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:40:26 2019

@author: Man Vinayaka
"""
import pandas as pd
import numpy as np
#Select by Data
def selectByDate(df,year):
    file = input ("Enter file name (ex: X.csv): " ) 
    #############
    df = pd.read_csv(file)
    df.index= pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_n= df[year].resample("1D").mean()
    df_n = df_n.fillna(method='ffill')
    df_n['month'] = df_n.index.month
    df_n.index.dayofweek
    print(df_n)

selectByDate(df,'2003')
