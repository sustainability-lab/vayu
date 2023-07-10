import folium
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
    
def google_maps(df:pd.DataFrame, lat:str, long:str, pollutant:str, date:str, markersize:int,zoom:int):
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
    zoom: int
        The int by which you want to zoom in the plot

    """
   
    df1 = df[df['date'] == date]

    lat= df1[lat].values[0] 
    long=df1[long].values[0] 
    my_map4 = folium.Map(location = [lat, long], zoom_start = zoom)

    for lat,long,pol,st in zip(df['latitude'],df['longitude'],df[pollutant],df['station']):
        folium.CircleMarker([lat, long],radius=markersize * pol, popup=(str(st).capitalize()+"<br>"+ str(round(pol, 3))), fill=True, fill_opacity=0.7, color = 'red').add_to(my_map4)

    my_map4.save("googleMaps.html")
    print('your map has been saved')
    return my_map4


#Example:
# df = pd.read_csv('interpolData.csv')
# Call the function and display the map in Jupyter Notebook
# map_obj = google_maps(df, 'latitude', 'longitude', 'pm25', '2022-02-23', 5,10)
# map_obj
