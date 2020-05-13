def timeProp(df, year, pollutant, 
    avg_days, date_time_col_name, 
    sorted_bars=True):
    """
    Plot a stacked bar graph of all data in the df
    based on frequency of wind direction in compass
    directions. Takes the average of every 3 days
    in each bar. The hight of the bar is value of 
    the pollutant that 3 day period. The bars are 
    binned proportionaly based on the overall value of the 
    pollutant 
    
    Parameters
    ----------
    df: data frame
        data frame which has the fields of date and the pollutant
        to be graphed
    year: type string
        The year of which the data will be cut
    pollutant: type string
        The pollutant of which to plot
    avg_days: type integer
      number of days to take the average of (controlling 
      granularity of the X-axis)
    date_time_col_name: type string
      df column name containing date-time stamps  
    """
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy import array
    import matplotlib.patches as mpatches

    # =============================================================================
    #     Cuts data into the year specified and averages the
    #     values of each day
    # =============================================================================
    df.index = pd.to_datetime(df[date_time_col_name])
    df = df.drop(date_time_col_name, axis=1)
    df_year = df[year]
    df_year = df_year.fillna(method="ffill")
    df_year["month"] = df_year.index.month

    # New df containing only the values of the pollutant specified
    polArray = df[year].resample("1D").mean()
    polArray = df_year[pollutant]

    nA = []
    neA = []
    eA = []
    seA = []
    sA = []
    swA = []
    wA = []
    nwA = []
    polMeanS = 0
    polMeanE = avg_days
    dfStart = 0
    dfEnd = 24 * avg_days  # 24*3 for 3 day average

    x = 0

    while x < int(
        365 / avg_days
    ):  # example: 365 days / 3 = 121 floored. Represents number of bars total
        n = 0
        ne = 0
        e = 0
        se = 0
        s = 0
        sw = 0
        w = 0
        nw = 0
        a = df_year[dfStart:dfEnd]
        b = a["wd"]

        i = 0
        while (
            i < 24 * avg_days
        ):  # Bins the wd data into categories for stacked bar graph
            if b[i] > 348.75 or b[i] < 33.75:
                n = n + 1
            elif b[i] > 33.75 and b[i] < 78.75:
                ne = ne + 1
            elif b[i] > 78.75 and b[i] < 123.75:
                e = e + 1
            elif b[i] > 123.75 and b[i] < 168.75:
                se = se + 1
            elif b[i] > 168.75 and b[i] < 213.75:
                s = s + 1
            elif b[i] > 213.75 and b[i] < 258.75:
                sw = sw + 1
            elif b[i] > 258.75 and b[i] < 303.75:
                w = w + 1
            elif b[i] > 303.75 and b[i] < 348.75:
                nw = nw + 1

            i = i + 1
        # calculates the 3 day proportion mean of each polutant and stores
        # it in a new list
        n = (n / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        ne = (ne / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        e = (e / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        se = (se / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        s = (s / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        sw = (sw / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        w = (w / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())
        nw = (nw / 24 * avg_days) * (polArray[polMeanS:polMeanE].mean())

        nA.append(n)
        neA.append(ne)
        eA.append(e)
        seA.append(se)
        sA.append(s)
        swA.append(sw)
        wA.append(s)
        nwA.append(nw)
        x = x + 1
        # Adds to start and end values to get through end of df
        polMeanS = polMeanS + avg_days
        polMeanE = polMeanE + avg_days
        dfStart = dfStart + 24 * avg_days
        dfEnd = dfEnd + 24 * avg_days

    #########################################

    # Plots the stacked bar graph with specific color represtations.
    # A legend is also plotted
    color_list = ["red", "blue", "green", "purple", "orange", "yellow", "brown", "pink"]

    X = np.arange(int(365 / avg_days))
    data = np.array([nA, neA, eA, seA, sA, swA, wA, nwA])

    if sorted_bars:
        for ix, x in enumerate(X):
            vals = data[:, ix]  # pollutant contributions (len == 8)
            assert len(vals) == len(color_list)
            # sorting based on the contributions
            col = sorted(zip(vals, color_list), key=lambda x: x[0], reverse=True)
            for i in range(data.shape[0]):
                plt.bar(
                    x, col[i][0], bottom=np.sum([c[0] for c in col[:i]]), color=col[i][1],
                )
    else:
        X = np.arange(data.shape[1])
        for i in range(data.shape[0]):
            plt.bar(
                X,
                data[i],
                bottom=np.sum(data[:i], axis=0),
                color=color_list[i % len(color_list)],
            )

    # Legend stuff.
    red_patch = mpatches.Patch(color="red", label="North")
    blue_patch = mpatches.Patch(color="blue", label="North East")
    green_patch = mpatches.Patch(color="green", label="East")
    purple_patch = mpatches.Patch(color="purple", label="South East")
    orange_patch = mpatches.Patch(color="orange", label="South")
    yellow_patch = mpatches.Patch(color="yellow", label="South West")
    brown_patch = mpatches.Patch(color="brown", label="West")
    pink_patch = mpatches.Patch(color="pink", label="North West")
    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc=2,
        borderaxespad=0.0,
        handles=[
            red_patch,
            blue_patch,
            green_patch,
            purple_patch,
            orange_patch,
            yellow_patch,
            brown_patch,
            pink_patch,
        ],
    )

    # Setting fonts
    plt.xticks(
        np.arange(0, int(365 / avg_days), 30 / avg_days),
        (
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ),
    )
    plt.title("Wind Direction")
    plt.xlabel("Contribution weighted by Mean")
    plt.ylabel("Pollutant (µg/m³)")
    plt.rcParams["figure.figsize"] = 20, 6
    plt.show()


# =============================================================================
# mydata = pd.read_csv('mydata.csv')
# timeProp(mydata,'2003','so2')
# =============================================================================
