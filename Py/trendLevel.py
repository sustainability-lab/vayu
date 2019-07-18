import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import vstack
import pandas as pd
from numpy  import array
import seaborn as sns

df = pd.read_csv("mydata.csv")
df.index= pd.to_datetime(df.date)
year = ['1998','1999','2000','2001','2002','2003']

def trend_level(df, pollutant, **kwargs):
    """
    df: pd.DataFrame with pd.DateTimeIndex as the index
    """
    pollutant_series = df[pollutant]
    unique_years = np.unique(df.index.year)[:6]
    num_unique_years = len(unique_years)
    fig, ax = plt.subplots(nrows=num_unique_years, sharex=True, figsize=(10, 50))
    for i, year in enumerate(unique_years):
        year_string = f'{year}'
        pollutant_series_year = pollutant_series[year_string]
        t = pollutant_series_year.groupby([pollutant_series_year.index.month, pollutant_series_year.index.hour]).mean()
        two_d_array= t.values.reshape(12, 24).T
        sns.heatmap(two_d_array, cbar = True,linewidth=0, cmap = 'Spectral_r',vmin=0, vmax=400, ax=ax[i])
        ax[i].set_title(year_string)
        ax[i].invert_yaxis()
    return ax

trend_level(df,'nox')