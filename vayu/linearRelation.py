def linearRelation(df, pol1, pol2):
    """Plots the slope `m` by fitting a linear model between
    pol1 and plo2, i.e., plo1

    This plot given two pollutants will graph the linear 
    relationship. The df given will be converted to the slope
    between the pollutants. 
        
    Parameters
    ----------
    df: data frame
        minimally containing date and two pollutants
    pol1: type string
        First pollutant that when plotted would appear
        on the x-axis of a relationship, ex: 'nox'
    pol2: type string
        Second pollutant that when plotted would appear
        on the y-axis of a relationship, ex: 'pm10'     
    """
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy import array
    import seaborn as sns

    df.index = pd.to_datetime(df.date)
    unique_years = np.unique(df.index.year)

    """
    Finds the unique years in the given data
    and converts it to a string type within a list 
    to be called on later to determine manipulation 
    of data
    """
    i = 0
    year = []
    while i < len(unique_years):
        year.append(str(unique_years[i]))
        i = i + 1
    # print(year)
    num_unique_years = len(year)
    df = df.drop("date", axis=1)

    """
    Will create a df(df_1) varying in lentgh based on the
    number of years that the data contains. The df 
    consists of the slope between the two given pollutants
    """
    i = 0
    values = []
    while i < num_unique_years:
        df_new = df[year[i]].resample("1D").mean()
        df_new = df_new.fillna(method="ffill")
        df_new["month"] = df_new.index.month
        # df_new.index.dayofweek
        pol_1 = df_new[pol1].mean()
        # this might not be entirely correct.
        # TODO: we want to take the average of the slope.
        # [Not take the average and find the slope]
        # Additionally, we would like to have the option of
        # changing the granularity.
        pol_2 = df_new[pol2].mean()
        values.append(pol_2 / pol_1)
        i = i + 1
    df_1 = pd.DataFrame(values)
    df_1.columns = ["div"]
    
    """ Creates a df for the first polutant that 
        contains the average value for every month
        of every year given
    """
    var1 = []
    var2 = []
    i = 0
    x = 0
    j = 0
    while i < num_unique_years:

        df_new = df[year[j]].resample("1D").mean()
        df_new = df_new.fillna(method="ffill")
        df_new["month"] = df_new.index.month
        df_new["day"] = df_new.index.dayofweek
        df_new["hour"] = df_new.index.hour
        i = i + 1
        j = j + 1
        x = 0
        while x < 12:
            a = df_new[df_new.month == x]
            mean_var1 = a[pol1].mean()
            var1.append(mean_var1)
            x = x + 1

    """ Creates a df for the second polutant that 
        contains the average value for every month
        of every year given
    """
    i = 0
    x = 0
    j = 0
    while i < num_unique_years:

        df_new = df[year[j]].resample("1D").mean()
        df_new = df_new.fillna(method="ffill")
        df_new["month"] = df_new.index.month
        df_new["day"] = df_new.index.dayofweek
        df_new["hour"] = df_new.index.hour
        i = i + 1
        j = j + 1
        x = 0
        while x < 12:
            a = df_new[df_new.month == x]
            mean_var2 = a[pol2].mean()
            var2.append(mean_var2)
            x = x + 1

    """ Finds the slope of the new dataframe
    """
    res = [i / j for i, j in zip(var2, var1)]
    df_2 = pd.DataFrame(res)
    df_2.columns = [pol2 + "/" + pol1]

    """ creates a list that contains the year values 
        of each data point to use for graphing a 
        scatterplot
    """
    scatterY = []
    t = 0
    while t < num_unique_years:
        r = 0
        while r < 12:
            scatterY.append(t + (r / 12))
            r = r + 1
        t = t + 1

    """ Plots a line plot of the average slope between the
        two pollutants given for every year. That plot is then superimposed 
        with a scatter plot of the average value of every month of every year
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)

    ax.plot(df_1, color="red", label = f"average slope between {pol1} & {pol2}")
    ax.set_xlabel("Year", color="red")
    ax.set_ylabel(f"Pollutant ratio ({pol2}/{pol1})", color="red")
    ax.tick_params(axis="x", colors="red")
    ax.tick_params(axis="y", colors="red")
    ax.set_xticklabels(unique_years)
  
    ax2.scatter(scatterY, res, color="blue", label = "average value of (" + pol2 + 
                "/" + pol1 + ") for every month of year")
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.xaxis.set_label_position("top")
    ax2.yaxis.set_label_position("right")
    ax2.tick_params(axis="x", colors="blue")
    ax2.tick_params(axis="y", colors="blue")
    
    fig.legend(loc="upper right", bbox_to_anchor=(1.1,1.1))
    
    plt.show()


# =============================================================================
# df = pd.read_csv("mydata.csv")
# linearRelation(df,'nox','so2')
# =============================================================================
