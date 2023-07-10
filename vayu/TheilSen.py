import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import ScalarFormatter

def theilsen(df:pd.DataFrame, pollutant:str):
    """Connected scatter plot.

    Plots a connected scatter plot of the average value of
    the pollutant every month of every year. Then plots a
    line of best fit through the plot showing the user
    the overall trend of the pollutant through the years.
    
    Parameters
    ----------
    df: data frame
        minimally containing date and at least one other
        pollutant 
    pollutant: type string
        A pollutant name correspoinding to 
        a variable in a data frame, ex: 'pm25'

    """
    
    df.index = pd.to_datetime(df.date)
    unique_years = np.unique(df.index.year)

    var2 = []
    scatterX = []

    for year in unique_years:
        df_year = df[df.index.year == year]
        df_monthly = df_year.resample("M").mean()
        monthly_mean = df_monthly[pollutant].values
        var2.extend(monthly_mean)
        scatterX.extend(np.arange(len(monthly_mean)) / 12 + year)

    y = np.array(var2)
    x = np.array(scatterX)

    def best_fit(X, Y):
        xbar = np.mean(X)
        ybar = np.mean(Y)
        n = len(X)

        numer = np.sum(X * Y) - n * xbar * ybar
        denum = np.sum(X ** 2) - n * xbar ** 2

        b = numer / denum
        a = ybar - b * xbar

        return a, b

    a, b = best_fit(x, y)

    fig, ax = plt.subplots()
    ax.plot(x, y, "-o")
    ax.set_xlabel("Year")
    ax.set_ylabel(pollutant)
    ax.set_title("TheilSen plot")
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="red")

    # Format y-axis tick labels
    ax.xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
    plt.savefig("TheilSenplot.png", bbox_inches="tight")
    print("Your plot has also been saved")

    plt.show()


# =============================================================================
# df = pd.read_csv("mydata.csv")
# theilsen(df, 'pm25')
# =============================================================================
