def timePlot(df, year, month, 
    pollutants=["ws", "nox", "o3", "pm25", "pm10"]):
    """
    Plot time series of pollutants for given month and year.
        
    Parameters
    ----------
    df: data frame
        a data frame of time series. Must have a date field
        and at least one variable to plot
    year: str
        year of which data will be cut
    month: int
        month of what plot will be graphed
    pollutants: list
        column names of pollutatnts to compare
    """
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # Cuts the df down to the month specified
    df.index = pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_n = df[year]
    df_n = df_n.fillna(method="ffill")
    df_n["month"] = df_n.index.month
    df_n.index.dayofweek
    df_n_1 = df_n[df_n.month == month]
    # New lists that have the value of the pollutant in the month specified

    color_list = ["red", "blue", "green", "purple", "orange"]

    plt.figure(1)
    # series of `len(pollutants)` plots in one large plot that contains the
    # time series of the polutants

    axs = []

    for ix, pollutant in enumerate(pollutants):
        values = df_n_1[pollutant]
        color = color_list[ix % len(color_list)]

        # plotting
        plt.subplot(f"{len(pollutants)}1{ix}")
        a = values.plot.line(color=color)
        a.axes.get_xaxis().set_visible(False)
        a.yaxis.set_label_position("right")
        axs.append(a)
        plt.ylabel(pollutant)

    # making dates visible.
    axs[0].axes.get_xaxis().set_visible(True)
    return axs
