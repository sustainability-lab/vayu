import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime as dt
import matplotlib as mpl
import numpy as np
from numpy import vstack
from numpy import array

def trend_level(df:pd.DataFrame, pollutant:str, **kwargs):
    """
    Plot that shows the overall pollutant trend for every year in the 
    df. It takes the average hour value of each month and plots a heatmap
    showing what times of the year there is a high concentration of the 
    pollutant.

    Parameters
    ----------
    df: pd.DataFrame
        Data frame of complete data
    pollutant: str
        Name of the data series in df to produce plot.
    """
   

    df.index = pd.to_datetime(df.date)
    pollutant_series = df[pollutant]
    unique_years = np.unique(df.index.year)
    num_unique_years = len(unique_years)
    fig, ax = plt.subplots(nrows=num_unique_years, figsize=(20, 20))

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    for i, year in enumerate(unique_years):
       
        year_string = str(year)
        pollutant_series_year = pollutant_series[year_string]
        t = pollutant_series_year.groupby(
            [pollutant_series_year.index.month, pollutant_series_year.index.hour]
        ).mean()
        two_d_array = t.values.reshape(12, 24).T
        heatmap_ax = ax[i] if num_unique_years > 1 else ax
        sns.heatmap(
            two_d_array,
            cbar=True,
            linewidth=0,
            cmap="Spectral_r",
            vmin=0,
            vmax=400,
            ax=heatmap_ax
        )
        heatmap_ax.set_xticklabels(months)
        heatmap_ax.set_ylabel("Hour of the Day")
        heatmap_ax.set_title(year_string)
        heatmap_ax.invert_yaxis()
        
    plt.savefig("TrendLevelPlot.png", bbox_inches="tight",dpi=300)
    print("Your plots has also been saved")
    plt.show()  # Display the plot


# =============================================================================
# df = pd.read_csv("mydata.csv")
# trend_level(df, 'pm25')
# =============================================================================
