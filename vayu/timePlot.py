def timePlot(df, year, month):
    """ Plot time series of ws,nox,o3,pm25,pm10 given a month and year
		
		Parameters
		----------
		df: data frame
			a data frame of time series. Must have a date field
			and at least one variable to plot
		year: type string
			year of which data will be cut
		month: type int
			month of what plot will be graphed
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
    ws = df_n_1["ws"]
    nox = df_n_1["nox"]
    o3 = df_n_1["o3"]
    pm25 = df_n_1["pm25"]
    pm10 = df_n_1["pm10"]

    plt.figure(1)
    # series of 5 plots in one large plot that contains the
    # time series of the polutants

    plt.subplot(511)
    a = nox.plot.line(color="red")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel("nox")

    plt.subplot(512)
    a = o3.plot.line(color="blue")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel("o3")

    plt.subplot(513)
    a = pm25.plot.line(color="green")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel("pm25")

    plt.subplot(514)
    a = pm10.plot.line(color="purple")
    a.axes.get_xaxis().set_visible(False)
    a.yaxis.set_label_position("right")
    plt.ylabel("pm10")

    plt.subplot(515)
    a = ws.plot.line(color="orange")
    a.yaxis.set_label_position("right")
    plt.ylabel("ws")


# =============================================================================
# mydata = pd.read_csv('mydata.csv')
# timePlot(mydata,'2003',8)
# =============================================================================
