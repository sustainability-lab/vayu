def googleMaps(df, lat, long, pollutant, date, markersize):
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
        Name of pollutant where values of that pollutant is stored.
    date: str
        visualizing the pollutant of a specific date.
    markersize: int
        The int by which the value of pollutant will be multiplied.

    """
    import folium
    import webbrowser
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    
    def googleMaps(df, lat, long, pollutant, date, markersize):
        df1=df
        print(date)
        df1=df[df['date']==date]
        print(df1)
    

    # =============================================================================
    # df = pd.read_csv('interpolData.csv')
    # =============================================================================

        lat= df1[lat].values[0] 
        long=df1[long].values[0] 
        my_map4 = folium.Map(location = [lat, long], zoom_start = 10)

        for lat,long,pol,st in zip(df['latitude'],df['longitude'],df[pollutant],df['station']):
            
            folium.CircleMarker([lat, long],radius=markersize * pol, popup=(str(st).capitalize()+"<br>"+ str(round(pol, 3))), fill=True, fill_opacity=0.7, color = 'red').add_to(my_map4)

        my_map4.save("googleMaps.html")
        print('your map has been saved')


#Example
# df = pd.read_csv('interpolData.csv')
#googleMaps(df, 'latitude', 'longitude', 'pm25', '2022-08-23', 5)
