import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from numpy import array

def time_variation(df:str, pollutant:list=['pm25']):
    """ 
    Plots four plots:
    - The average pollutant level per day by 
    each hour for each day of the week across all of the data
    - The average pollutant level by each hour, 
    across all data
    - The average pollutant level by each month of the
    year for across data
    - The average pollutant level per day of the week 
    across all data
    
    Parameters
    ----------
    df: pandas.DataFrame
      data frame of hourly data. 
      Must include a date field and at least one variable to plot
    pollutant: list
      Name of variables to plot

    """
   

    df["date"] = pd.to_datetime(df.date)

    df_days=df
    df_hour=df
    df_month=df
    df_weekday = df
    
    df_days["day"] = df_days["date"].dt.day_name()
    df_days = df_days.set_index(keys=["day"])
    df_days = df_days.groupby(["day"])

    dayWeek = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for i in range(len(dayWeek)):
        plt.figure(1, figsize=(40, 5))
        plt.subplot(1, 7, i + 1)
        plt.grid()

        df_day = df_days.get_group(dayWeek[i])
        df_day["hour"] = df_day["date"].dt.hour

        df_day_m = df_day.groupby("hour").mean().reset_index()
        df_day_s = df_day.groupby("hour").std().reset_index()
       

        for k in range(len(pollutant)):
            plt.plot(df_day_m["hour"], df_day_m[pollutant[k]], label=pollutant[k])
            plt.fill_between(
                df_day_s["hour"],
                df_day_m[pollutant[k]] - 0.5 * df_day_s[pollutant[k]],
                df_day_m[pollutant[k]] + 0.5 * df_day_s[pollutant[k]],
                alpha=0.2,
            )
            plt.xlabel(dayWeek[i])
            plt.legend()
    plt.savefig("TimeVariationPlots1.png", bbox_inches="tight")

    plt.figure(2, figsize=(35, 5))
    plt.subplot(1, 3, 1)
    plt.grid()

    df_hour["hour"] = df_hour["date"].dt.hour
    df_hour_m = df.groupby("hour").mean().reset_index()
    df_hour_s = df.groupby("hour").std().reset_index()
    
    for i in range(len(pollutant)):
        plt.plot(df_hour_m["hour"], df_hour_m[pollutant[i]], label=pollutant[i])
        plt.fill_between(
            df_hour_s["hour"],
            df_hour_m[pollutant[i]] - 0.5 * df_hour_s[pollutant[i]],
            df_hour_m[pollutant[i]] + 0.5 * df_hour_s[pollutant[i]],
            alpha=0.2,
        )
        plt.xlabel("Hour")
        plt.legend()

    plt.subplot(1, 3, 2)
    plt.grid()

    df_month["month"] = df_month["date"].dt.month
    df_month_m = df_month.groupby("month").mean().reset_index()
    df_month_s = df_month.groupby("month").std().reset_index()
    
    for i in range(len(pollutant)):
        plt.plot(df_month_m["month"], df_month_m[pollutant[i]], label=pollutant[i])
        plt.fill_between(
            df_month_s["month"],
            df_month_m[pollutant[i]] - 0.5 * df_month_s[pollutant[i]],
            df_month_m[pollutant[i]] + 0.5 * df_month_s[pollutant[i]],
            alpha=0.2,
        )
        plt.xlabel("Month")
        plt.legend()

    plt.subplot(1, 3, 3)
    plt.grid()
    
    df_weekday["weekday"] = df_weekday["date"].dt.weekday
    df_weekday_m = df_weekday.groupby("weekday").mean().reset_index()
    df_weekday_s = df_weekday.groupby("weekday").std().reset_index()

    for i in range(len(pollutant)):
        plt.plot(
            df_weekday_m["weekday"], df_weekday_m[pollutant[i]], label=pollutant[i]
        )
        plt.fill_between(
            df_weekday_s["weekday"],
            df_weekday_m[pollutant[i]] - 0.5 * df_weekday_s[pollutant[i]],
            df_weekday_m[pollutant[i]] + 0.5 * df_weekday_s[pollutant[i]],
            alpha=0.2,
        )
        plt.xlabel("WeekDay")
        plt.legend()
    plt.savefig("TimeVariationPlots2.png", bbox_inches="tight")
    print("Your plots has also been saved")
    plt.show()
    




# =============================================================================
# df = pd.read_csv("mydata.csv")
# time_variation(df, pollutant=['pm25','nh3'])
# =============================================================================
