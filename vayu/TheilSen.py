def TheilSen(df, pollutant):
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
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy import array
    import seaborn as sns
    import scipy
    from scipy import stats
    import math

    # =============================================================================
    # df = pd.read_csv("mydata.csv")
    # =============================================================================
    df.index = pd.to_datetime(df.date)
    unique_years = np.unique(df.index.year)
    # df = df[pd.notnull(df[pollutant])]

    i = 0
    year = []
    while i < len(unique_years):
        year.append(str(unique_years[i]))
        i = i + 1
    num_unique_years = len(year)

    # df = df.drop("date", axis=1)
    # print(df)
    i = 0
    x = 0
    j = 0
    var2 = []
    while i < num_unique_years:
        df_new = df[year[j]].resample("1D").mean()
        df_new = df_new.fillna(method="ffill")
        df_new["month"] = df_new.index.month
        # df_new['day']=df_new.index.dayofweek
        # df_new['hour']=df_new.index.hour
        i = i + 1
        j = j + 1
        x = 0
        while x < 12:
            a = df_new[df_new.month == x]
            mean_var2 = a[pollutant].mean()
            var2.append(mean_var2)
            x = x + 1
    i = 0
    while i < len(var2):
        if pd.notnull(var2[i]) == False:
            var2[i] = (var2[i - 1] + var2[i + 1]) / 2
        i = i + 1

    scatterX = []
    t = 0
    while t < num_unique_years:
        r = 0
        while r < 12:
            scatterX.append(t + (r / 12))
            r = r + 1
        t = t + 1

    y = var2
    x = scatterX

    def best_fit(X, Y):

        xbar = sum(X) / len(X)
        ybar = sum(Y) / len(Y)
        n = len(X)  # or len(Y)

        numer = sum([xi * yi for xi, yi in zip(X, Y)]) - n * xbar * ybar
        denum = sum([xi ** 2 for xi in X]) - n * xbar ** 2

        b = numer / denum
        a = ybar - b * xbar

        # print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

        return a, b

    a, b = best_fit(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # print(len(x))
    ax.plot(x, y, "-o")
    ax.set_xlabel("Year")
    ax.set_ylabel(pollutant)
    ax.set_title("TheilSen plot")
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color="red")
    plt.show()


# =============================================================================
# df = pd.read_csv("mydata.csv")
# TheilSen(df, 'o3')
# =============================================================================
