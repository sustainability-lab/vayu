import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def time_plot(df:pd.DataFrame, year:str, pollutants:list=["pm25"]):
    """
    Plot time series of pollutants for given month and year.
        
    Parameters
    ----------
    df: data frame
        a data frame of time series. Must have a date field
        and at least one variable to plot
    year: str
        year of which data will be cut
    pollutants: list
        column names of pollutatnts to compare
    """
    
     # Cuts the df down to the month specified
    df.index = pd.to_datetime(df.date)
    df_n_1 = df[(df.index.year == int(year))]
    #df_n_1 = df[(df.index.month == int(month)) & (df.index.year == int(year))]
    
    fig = go.Figure()
    
    for pollutant in pollutants:
        if pollutant in df_n_1.columns:
            values = df_n_1[pollutant]
            
            # Add trace for each selected pollutant
            fig.add_trace(go.Scatter(
                x=values.index,
                y=values.values,
                name=pollutant
            ))
        else:
            print(f"Warning: {pollutant} data not found.")
        
    # Configure layout
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
                #active=2
            ),
            rangeslider=dict(
                visible=True
            ),
            
            type="date"
        )
    )
    
    fig.show()

#Example:
#time_plot(df, 2022, pollutants=['pm25','pm10','ws','wd'...and so on])
#--------------------
    