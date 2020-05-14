def scatterPlot(df, x, y, **kwargs):
    """
    Parameters
    ----------
    df: data frame 
        data frame containing at least 
        2 numeric variables to plot
    x: type string
        name of x variable to plot
    y: type string
        name of y variable to plot
        
    """
    import numpy as np
    import seaborn as sns
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    from math import pi

    pm10 = df.pm10
    o3 = df.o3
    ws = df.ws
    wd = df.wd
    nox = df.nox
    no2 = df.no2

    #########################################
    # converts wind data to randians
    df = pd.DataFrame({"speed": ws, "direction": wd})
    df["speed_x"] = df["speed"] * np.sin(df["direction"] * pi / 180.0)
    df["speed_y"] = df["speed"] * np.cos(df["direction"] * pi / 180.0)
    fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_aspect("equal")
    _ = df.plot(kind="scatter", x="speed_x", y="speed_y", alpha=0.35, ax=ax)

    ####################################
    # simple seaborn plot that shows how given variables relate with one another
    if x == "nox":
        x = nox
    elif x == "no2":
        x = no2
    elif x == "o3":
        x = o3
    elif x == "pm10":
        x = pm10
    if y == "nox":
        y = nox
    elif y == "no2":
        y = no2
    elif y == "o3":
        y = o3
    elif y == "pm10":
        y = pm10

    sns.jointplot(x=x, y=y, kind="hex")

    plt.show()


# =============================================================================
# df = pd.read_csv("mydata.csv")
# scatterPlot(df,'nox','no2')
# =============================================================================
