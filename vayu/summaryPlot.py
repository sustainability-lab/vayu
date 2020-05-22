def summaryPlot(df):
    """ Plots import summary of data frame given. Plots line plots
        and histograms for each polutant as well as statiscs such as 
        mean,max,min,median, and 95th percentile
        
        Parameters
        ----------
        df: data frame
            data frame to be summarised. Must contain a date field
            and at least one other parameter 
    """
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy import array
    import matplotlib.patches as mpatches
    import seaborn as sns
    from matplotlib.pyplot import figure

    pm10_s = 0
    pm10_m = 0
    pm10_h = 0
    pm25_s = 0
    pm25_m = 0
    pm25_h = 0
    so2_s = 0
    so2_m = 0
    so2_h = 0
    co_s = 0
    co_m = 0
    co_h = 0
    o3_s = 0
    o3_m = 0
    o3_h = 0
    no2_s = 0
    no2_m = 0
    no2_h = 0

    class color:
        # Allows for bolded and underlined text
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    # Reads df and fills empty values
    df.index = pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_all = df.resample("1D")
    df_all = df
    df_all = df_all.fillna(method="ffill")

    dataPoints = ["pm25", "co", "so2", "pm10", "o3", "no2", "nox", "wd", "ws"]

    for column in df_all.columns:
        if str(column) == "pm10":
            df_pm10 = df_all["pm10"]
            for (_, data) in df_pm10.iteritems():
                if data < 100:
                    pm10_s += 1
                elif data > 100 and data < 250:
                    pm10_m += 1
                elif data > 250:
                    pm10_h += 1

        if str(column) == "pm25":
            df_pm25 = df_all["pm25"]
            for (_, data) in df_pm25.iteritems():
                if data < 60:
                    pm25_s += 1
                elif data > 60 and data < 90:
                    pm25_m += 1
                elif data > 100:
                    pm25_h += 1

        if str(column) == "co":
            df_co = df_all["co"]
            for (_, data) in df_co.iteritems():
                if data < 2:
                    co_s += 1
                elif data > 2 and data < 10:
                    co_m += 1
                elif data > 10:
                    co_h += 1

        if str(column) == "so2":
            df_so2 = df_all["so2"]
            for (_, data) in df_so2.iteritems():
                if data < 80:
                    so2_s += 1
                elif data > 80 and data < 380:
                    so2_m += 1
                elif data > 380:
                    so2_h += 1

        if str(column) == "o3":
            df_o3 = df_all["o3"]
            for (_, data) in df_o3.iteritems():
                if data < 100:
                    o3_s += 1
                elif data > 100 and data < 168:
                    o3_m += 1
                elif data > 168:
                    o3_h += 1

        if str(column) == "no2":
            df_no2 = df_all["no2"]
            for (_, data) in df_no2.iteritems():
                if data < 80:
                    no2_s += 1
                elif data > 80 and data < 180:
                    no2_m += 1
                elif data > 180:
                    no2_h += 1

    i = 0
    sub = 1
    while i < 9:
        # Plots line and histogram plots for ecery polutant
        # in the correct location based on subplot

        plt.figure(1, figsize=(25, 25))
        plt.subplot(9, 3, sub)
        sub = sub + 1
        a = df_all[dataPoints[i]].plot.line(color="gold")
        a.axes.get_xaxis().set_visible(False)
        a.yaxis.set_label_position("left")
        plt.ylabel(dataPoints[i], fontsize=30, bbox=dict(facecolor="whitesmoke"))

        plt.subplot(9, 3, sub)

        sub = sub + 1
        plt.hist(df_all[dataPoints[i]], bins=50, color="green")

        ax1 = plt.subplot(9, 3, sub)

        # fig1,ax1 = plt.subplots()

        sub = sub + 1

        labels = ["Safe", "Moderate", "High"]
        if dataPoints[i] == "pm10":
            sizes = [pm10_s, pm10_m, pm10_h]
        elif dataPoints[i] == "pm25":
            sizes = [pm25_s, pm25_m, pm25_h]
        elif dataPoints[i] == "so2":
            sizes = [so2_s, so2_m, so2_h]
        elif dataPoints[i] == "co":
            sizes = [co_s, co_m, co_h]
        elif dataPoints[i] == "o3":
            sizes = [o3_s, o3_m, o3_h]
        elif dataPoints[i] == "no2":
            sizes = [no2_s, no2_m, no2_h]

        explode = [0, 0, 1]
        ax1.pie(
            sizes,
            explode=explode,
            labels=labels,
            autopct="%1.1f%%",
            shadow=False,
            startangle=90,
        )
        ax1.axis("equal")

        sizes = [0, 0, 0]

        i = i + 1
    i = 0
    while i < 9:
        # Calculates statistics
        nDf = df[dataPoints[i]]
        missing = nDf.isna().sum() + sum(n < 0 for n in nDf)
        minVal = nDf.min()
        maxVal = nDf.max()
        meanVal = nDf.mean()
        medianVal = nDf.median()
        percentile = nDf.quantile(0.95)
        print("---------------")
        print(color.BOLD + color.UNDERLINE + dataPoints[i] + color.END)
        print("min = " + str(0))
        print("max = " + str(maxVal))
        print("missing = " + str(missing))
        print("mean = " + str(meanVal))
        print("median = " + str(medianVal))
        print("95th percentile = " + str(percentile))
        i = i + 1


# =============================================================================
# df = pd.read_csv('mydata.csv')
# summaryPlot(df)
# =============================================================================
