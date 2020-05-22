def smoothTrend(df, date_col_name, pollutant_col_name):

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import pandas as pd
    import numpy as np
    import calendar

    """Plots a connected scatter plot of the average value of
          the pollutant every month of every year. Then plots a
          smooth line of best fit through the plot showing the user
          the overall trend of the pollutant through the years.
      
      Parameters
      ----------
      df: data frame
        minimally containing date and at least one other
        pollutant 

     date: type string
       Name of the column having dates

     pollutant: type string
        A pollutant column name correspoinding to 
        a variable in a data frame, ex: 'pm25' 
        """

    df["date"] = pd.to_datetime(df[date_col_name])

    df_year = df
    df_year["year"] = df_year["date"].dt.year
    df_year["month"] = df_year["date"].dt.month
    df_year = df_year.groupby(["year", "month"]).mean()
    df_year = df_year.reset_index()

    years = np.unique(df_year["year"])
    months = np.unique(df_year["month"])
    num_years = len(years)

    plt.figure(1, figsize=(30, 8))

    result_t = [k for k in range(0, 12)]

    temp = 0
    a = 0
    prev = 0
    months = []
    name = []
    minor = []

    for i in range(num_years):
        df_imply = df_year
        df_imply = df_imply.loc[df_year["year"] == years[i]]
        m = df_imply["month"].unique()
        months.append(m)
        count_row = df_imply.shape[0]
        result_t = [k for k in range(temp, temp + count_row)]
        minor.append(temp + count_row)
        temp = temp + count_row
        if i == 0:
            plt.plot(
                result_t,
                df_imply[pollutant_col_name],
                color="red",
                linestyle="--",
                dashes=(10, 5),
                label="Concentration monthly averaged",
            )
        else:
            plt.plot(
                result_t,
                df_imply[pollutant_col_name],
                color="red",
                linestyle="--",
                dashes=(10, 5),
            )

    tick = np.array(months)

    for i in range(len(tick)):
        for j in range(len(tick[0])):
            name.append(str(years[a]) + " " + calendar.month_name[tick[i][j]])
            if j + 1 + prev == minor[a]:
                prev = minor[a]
                a = a + 1

    name = np.asarray(name)

    plt.xticks(range(0, len(name)), name, rotation="vertical")
    plt.xlabel("Timeline", fontsize=16)
    plt.ylabel("Concentration of Pollutant", fontsize=16)

    df_year = df_year.groupby(["year"]).mean()

    minor = [minor[-1]] + minor[:-1]

    minor[0] = 0

    minor = [(k + k + 1) / 2 for k in minor]

    plt.plot(
        minor,
        df_year[pollutant_col_name],
        color="black",
        label="Concentration yearly averaged",
    )

    plt.legend(loc="upper right", bbox_to_anchor=(1.1, 1.1), fontsize=16)
    plt.show()
