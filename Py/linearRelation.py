# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:03:47 2019

@author: Man Vinayaka
"""
def linearRelation(df,pol1,pol2):
    
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy  import array
    import seaborn as sns
    
    year = ['1998','1999','2000','2001','2002','2003','2004','2005']
    df.index= pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    
    i = 0
    values = []
    while i<8:
        df_new= df[year[i]].resample("1D").mean()
        df_new = df_new.fillna(method='ffill')
        df_new['month'] = df_new.index.month
        #df_new.index.dayofweek
        nox = df_new[pol1].mean()
        so2 = df_new[pol2].mean()
        values.append(so2/nox)
        i = i+1
    df_1 = pd.DataFrame(values)
    df_1.columns = ['div'] 
    #print(df_1)
    
    var1 = []
    var2 = []
    i = 0
    x = 0
    j = 0
    while i <8:
        
        df_new= df[year[j]].resample("1D").mean()
        df_new = df_new.fillna(method='ffill')
        df_new['month'] = df_new.index.month
        df_new['day']=df_new.index.dayofweek
        df_new['hour']=df_new.index.hour
        i = i+1
        j=j+1
        x = 0
        while x<12:
            a = df_new[df_new.month==x]
            mean_var1 = a[pol1].mean()
            var1.append(mean_var1)
            x = x+1
    
    i = 0
    x = 0
    j = 0
    while i <8:
        
        df_new= df[year[j]].resample("1D").mean()
        df_new = df_new.fillna(method='ffill')
        df_new['month'] = df_new.index.month
        df_new['day']=df_new.index.dayofweek
        df_new['hour']=df_new.index.hour
        i = i+1
        j=j+1
        x = 0
        while x<12:
            a = df_new[df_new.month==x]
            mean_var2 = a[pol2].mean()
            var2.append(mean_var2)
            x = x+1
    res = [i / j for i, j in zip(var2, var1)]
    df_2 = pd.DataFrame(res)
    df_2.columns = [pol2 +'/'+ pol1] 
    
    scatterY = []
    t = 0
    while t<8:
        r = 0
        while r<12:
            scatterY.append(t+(r/12))
            r = r+1
        t = t+1
    #print(scatterY)
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)
    
    ax.set_ylim(bottom=0.015, top=0.040)
    ax.plot(df_1,color="red")
    ax.set_xlabel("Year", color="red")
    ax.set_ylabel(pol2+'/'+ pol1, color="red")
    ax.tick_params(axis='x', colors="red")
    ax.tick_params(axis='y', colors="red")
    
    ax2.scatter(scatterY,res, color="blue")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.xaxis.set_label_position('top') 
    ax2.yaxis.set_label_position('right') 
    ax2.tick_params(axis='x', colors="blue")
    ax2.tick_params(axis='y', colors="blue")
    
    
    plt.show()


# =============================================================================
# df = pd.read_csv("mydata.csv")
# linearRelation(df,'nox','so2')
# =============================================================================

