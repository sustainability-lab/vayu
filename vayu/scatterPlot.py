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

   
    #########################################
    # converts wind data to randians
    #df1 = pd.DataFrame({"speed": ws, "direction": wd})
    df["speed"+str(x)] = df['ws'] * np.sin(df['wd'] * pi / 180.0)
    df["speed"+str(y)] = df['ws'] * np.cos(df['wd'] * pi / 180.0)   
    fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    #ax.set_aspect("equal")
    _ = df.plot(kind="scatter", x="speed"+str(x), y="speed"+str(y), alpha=0.35, ax=ax)
    plt.show()
    

    ####################################
    # simple seaborn plot that shows how given variables relate with one another
    sns.jointplot(x=df[x].values, y=df[y].values, kind="hex")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
    
    
# =============================================================================
# df = pd.read_csv("mydata.csv")
# scatterPlot(df,'nox','no2')
# =============================================================================
