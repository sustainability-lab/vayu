# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from windrose import WindroseAxes
import windrose
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import pi


mydata = pd.read_csv("mydata.csv")
#print(mydata.head())

pm10 = mydata.pm10
o3 = mydata.o3
ws = mydata.ws
wd = mydata.wd
nox = mydata.nox
no2 = mydata.no2


#########################################

df = pd.DataFrame({"speed": ws, "direction": wd})
df['speed_x'] = df['speed'] * np.sin(df['direction'] * pi / 180.0)
df['speed_y'] = df['speed'] * np.cos(df['direction'] * pi / 180.0)
fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
_ = df.plot(kind='scatter', x='speed_x', y='speed_y', alpha=0.35, ax=ax)

#print(mydata.head())
####################################
#print(no2)
x = nox
y = no2

sns.jointplot(x=x, y=y, kind='hex')

plt.show()


  