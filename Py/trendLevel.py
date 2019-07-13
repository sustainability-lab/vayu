import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import vstack
import pandas as pd
from numpy  import array
import seaborn as sns

df = pd.read_csv("mydata.csv")
mydata = pd.read_csv("mydata.csv")

pm10 = mydata.pm10
o3 = mydata.o3
ws = mydata.ws
wd = mydata.wd
nox = mydata.nox
no2 = mydata.no2
pm25 = mydata.pm25


#df = df.drop("date", axis=1)
year = ['1998','1999','2000','2001','2002','2003']
y =1

while y<=6:
    df = pd.read_csv("mydata.csv")
    df.index= pd.to_datetime(df.date)
    df_2003 = df[year[y-1]]
    df_2003['month'] = df_2003.index.month
    y = y+1
    
    t_0 = []
    
    #################
    #fig,ax = plt.subplots(figsize=(10,10), nrows=2, ncols=3)
    h = 0
    while h <=23 :
        
        m = 1
        while m <=12:
            df = df_2003[df_2003.month==m]
            a = df.groupby(df.index.hour).mean()
        
            test = []
            test = a['nox']
            t_0.append(test[h])
            m = m+1
        h = h+1
    t_0 = np.reshape(t_0, (24, 12))
    
    ######################
    
    fig,ax = plt.subplots(figsize=(15,15))
    ax = sns.heatmap(t_0, cbar = True,linewidth=0, cmap = 'Spectral_r',vmin=0, vmax=400)
    plt.gca().invert_yaxis()
    ax.set_title(year[y-2])
    plt.show()