def timeVariation(df, pollutant):
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
    pollutant: str
      Name of variable to plot

    """
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np
    import pandas as pd
    from numpy import array

    df["date"] = pd.to_datetime(df.date)

    df_days = df
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
    pollutant = ["pm10", "no2", "pm25", "so2"]

    for i in range(len(dayWeek)):
        plt.figure(1, figsize=(40, 5))
        plt.subplot(1, 7, i + 1)
        plt.grid()

        df_day = df_days.get_group(dayWeek[i])
        df_day["hour"] = df_day["date"].dt.hour

        df_day_m = df_day.groupby("hour").mean()
        df_day_m = df_day_m.reset_index()

        df_day_s = df_day.groupby("hour").std()
        df_day_s = df_day_s.reset_index()

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

    plt.figure(2, figsize=(35, 5))
    plt.subplot(1, 3, 1)

    df_hour = df
    df_hour["hour"] = df_hour["date"].dt.hour

    df_hour_m = df.groupby("hour").mean()
    df_hour_m = df_hour_m.reset_index()

    df_hour_s = df.groupby("hour").std()
    df_hour_s = df_hour_s.reset_index()

    plt.grid()

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
    df_month = df
    df_month["month"] = df_month["date"].dt.month

    df_month_m = df_month.groupby("month").mean()
    df_month_m = df_month_m.reset_index()

    df_month_s = df_month.groupby("month").std()
    df_month_s = df_month_s.reset_index()

    plt.grid()

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
    df_weekday = df
    df_weekday["weekday"] = df_weekday["date"].dt.weekday

    df_weekday_m = df_weekday.groupby("weekday").mean()
    df_weekday_m = df_weekday_m.reset_index()

    df_weekday_s = df_weekday.groupby("weekday").std()
    df_weekday_s = df_weekday_s.reset_index()

    plt.grid()

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


# =============================================================================
# df = pd.read_csv("mydata.csv")
# timeVariation(df,['pm10'])
# =============================================================================
