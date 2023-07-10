def selectByDate(df, year, group=None, time_period='day'):
    """
    Utility function to cut a given dataframe by year and find the average value
    of each day, month, or year. Optionally, data can be grouped by specified columns.
    
    Parameters
    ----------
    df: data frame
        A data frame containing a date field and optional grouping columns.
    year: type string
        A year to select and filter the data.
    group: list, optional
        A list of columns to group the data by. Default is None (no grouping).
    time_period: {'day', 'month', 'year'}, optional
        The time period to compute the average value. Default is 'day'.
    
    Returns
    -------
    data frame
        A data frame with the average value of each day, month, or year.
        If group is specified, the data will be grouped accordingly.
    """
    import pandas as pd
    import numpy as np
    
    df['date'] = pd.to_datetime(df['date'])
    df_year = df[df['date'].dt.year == int(year)]
    
    if group:
        df_grouped = df_year.groupby(group).resample(time_period[0], on='date').mean(numeric_only=True)
        return df_grouped
    
    if time_period == 'month':
        df_month = df_year.resample('M', on='date').mean(numeric_only=True)
        return df_month
    elif time_period == 'year':
        df_yearly = df_year.resample('Y', on='date').mean(numeric_only=True)
        return df_yearly
    
    df_day = df_year.resample('D', on='date').mean(numeric_only=True)
    return df_day


# =============================================================================
# df = pd.read_csv("mydata.csv")
#selectByDate(df1,'2022',group=['latitude','longitude','station'], time_period='month')
# =============================================================================
