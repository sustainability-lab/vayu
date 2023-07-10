import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from numpy import array
import matplotlib.patches as mpatches
import seaborn as sns
from matplotlib.pyplot import figure

def summary_plot(df: pd.DataFrame):
    """ Plots import summary of data frame given. Plots line plots
        and histograms for each polutant as well as statiscs such as 
        mean,max,min,median, and 95th percentile
        
        Parameters
        ----------
        df: data frame
            data frame to be summarised. Must contain a date field
            and at least one other parameter 
    """
   
    # Initialize variables
    pollutants = ["pm10", "pm25", "sox", "co", "o3", "nox", "pb", "nh3"]
    categories = ["s", "m", "h"]

    counts = {pollutant: {category: 0 for category in categories} for pollutant in pollutants}

    
    df.index = pd.to_datetime(df.date)
    df = df.drop("date", axis=1)
    df_all = df.resample("1D")
    df_all = df.copy()
    df_all = df_all.fillna(method="ffill")
    #print(df_all.columns)

    # Calculate counts for each pollutant category
    for pollutant in pollutants:
        if pollutant in df_all.columns:
            column_data = df_all[pollutant]
            #print(df_all)
            for _, data in column_data.iteritems():
                if pollutant in ["pm10", "pm25"]:
                    if data < 100:
                        counts[pollutant]["s"] += 1
                    elif data < 250:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "co":
                    if data < 2:
                        counts[pollutant]["s"] += 1
                    elif data < 10:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "sox":
                    if data <= 80:
                        counts[pollutant]["s"] += 1
                    elif data <= 380:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "o3":
                    if data < 100:
                        counts[pollutant]["s"] += 1
                    elif data < 168:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "nox":
                    if data < 80:
                        counts[pollutant]["s"] += 1
                    elif data < 180:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "pb":
                    if data <= 1:
                        counts[pollutant]["s"] += 1
                    elif data <= 2:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
                elif pollutant == "nh3":
                    if data <= 400:
                        counts[pollutant]["s"] += 1
                    elif data <= 800:
                        counts[pollutant]["m"] += 1
                    else:
                        counts[pollutant]["h"] += 1
         
                

    # Plot line, histogram, and pie charts for each pollutant
    fig, axes = plt.subplots(len(df_all.columns), 3, figsize=(25,25))

    for i, pollutant in enumerate(df_all.columns):
        ax_line = axes[i, 0]
        ax_hist = axes[i, 1]
        ax_pie = axes[i, 2]

        df_all[pollutant].plot.line(ax=ax_line, color="gold")
        ax_line.axes.get_xaxis().set_visible(False)
        ax_line.yaxis.set_label_position("left")
        ax_line.set_ylabel(pollutant, fontsize=30, bbox=dict(facecolor="whitesmoke"))

        ax_hist.hist(df_all[pollutant], bins=50, color="green")

        labels = ["Safe", "Moderate", "High"]
        sizes = [counts[pollutant][category] for category in categories]
        explode = [0, 0, 1]

        ax_pie.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
        ax_pie.axis("equal")

        ax_pie.set_xlabel("Statistics")
      
        print(f"{pollutant}\nmin = {df_all[pollutant].min():.2f}\nmax = {df_all[pollutant].max():.2f}\nmissing = {df_all[pollutant].isna().sum()}\nmean = {df_all[pollutant].mean():.2f}\nmedian = {df_all[pollutant].median():.2f}\n95th percentile = {df_all[pollutant].quantile(0.95):.2f}\n")

    plt.savefig("summary_plot.png", dpi=300, format="png")
    plt.show()
    print("your plots has also been saved")
    plt.close()


# =============================================================================
# df = pd.read_csv('mydata.csv')
# summary_plot(df)
# =============================================================================
