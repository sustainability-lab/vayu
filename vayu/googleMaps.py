def googleMaps(df, lat, long, pollutant, dataLoc):
    """Plots a geographical plot.

    Plots a folium plot of longitude and latitude points 
    provided with information about each point when clicked 
    on.

    Parameters
    ----------
    df: pandas.DataFrame
        minimally containing date and values of pollutant, city,
        longitude, latitude, and AQI
    lat: str
        Name of column in df of where latitude points are
    long: str
        Name of column in df of where longitude points are
    pollutant: str
        Name of pollutant 
    dataLoc: str
        Name of df column where pollutanat values are stored

    """
    import folium
    import webbrowser
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    latitude = 37.0902
    longitude = -95.7129
    Arithmetic_Mean_map = folium.Map(location=[latitude, longitude], zoom_start=4)

    # =============================================================================
    # df = pd.read_csv('interpolData.csv')
    # =============================================================================

    some_value = pollutant
    df = df.loc[df["Parameter Name"] == some_value]

    some_value = "2018-05-07"
    df = df.loc[df["Date Local"] == some_value]

    df = df.sample(frac=1)

    # df_train, df_test = train_test_split(df, test_size=0.2)
    df["Arithmetic Mean Q"] = pd.qcut(df[dataLoc], 4, labels=False)
    colordict = {0: "lightblue", 1: "lightgreen", 2: "orange", 3: "red"}

    for lat, lon, Arithmetic_Mean_Q, Arithmetic_Mean, city, AQI in zip(
        df[lat],
        df[long],
        df["Arithmetic Mean Q"],
        df[dataLoc],
        df["City Name"],
        df["AQI"],
    ):
        folium.CircleMarker(
            [lat, lon],
            radius=0.15 * AQI,
            popup=(
                "City: "
                + str(city).capitalize()
                + "<br>"
                #'Bike score: ' + str(bike) + '<br>'
                "Arithmetic_Mean level: "
                + str(Arithmetic_Mean)
                + "%"
            ),
            color="b",
            key_on=Arithmetic_Mean_Q,
            threshold_scale=[0, 1, 2, 3],
            fill_color=colordict[Arithmetic_Mean_Q],
            fill=True,
            fill_opacity=0.7,
        ).add_to(Arithmetic_Mean_map)
    Arithmetic_Mean_map.save("mymap.html")


# df = pd.read_csv('interpolData.csv')
# googleMaps(df,'Latitude','Longitude','Ozone','Arithmetic Mean')
