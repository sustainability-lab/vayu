def selectByDate(df, year):
    """ 
    Utility function to cut given dataframe by the year 
    and find the average value of each day 
    
    Parameters
    ----------
    df: data frame
        a data frame containing a date field
    year: type string
        a year to select to cut data
    """
    import pandas as pd
    import numpy as np

    df.index = pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_n = df[year].resample("1D").mean()
    df_n = df_n.fillna(method="ffill")
    df_n["month"] = df_n.index.month
    df_n.index.dayofweek
    print(df_n)


# =============================================================================
# df = pd.read_csv("mydata.csv")
# selectByDate(df,'2003')
# =============================================================================
