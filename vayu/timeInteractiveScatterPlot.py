def timeInteractiveScatterPlot(
    df,
    date_time_col_name,
    location_col_name,
    value_col_name,
    latitude_col_name,
    longitude_col_name,
    start_date,
    end_date,
    pollutant_ID,
    width=800,
    height=660,
    location=[22, 82],
    zoom_start=4.5,
    control_scale=True,
    tiles="Stamen Terrain",
    min_lat=6,
    max_lat=105,
    min_lon=68,
    max_lon=97,
    period="PT1M",
    date_options="YYYY-MM-DD HH:mm",
):

    """ Plots a time interactive scatter plot 
      of a given pollutant for given duration 
      of time.

  Parameters
  ----------
  df: data frame 
      minimally containing time stamps, location, 
      pollutant value, latitude and longitude

  date_time_col_name : type string
                       name of column in df having time stamps

  location_col_name : type string
                      name of column in df having station name

  value_col_name: type string
                  name of column in df having value of pollutant

  latitude_col_name : type string
                      name of column in df having latitute

  longitude_col_name : type string
                       name of column in df having longitude
                  
  start_date: type string
             time stamp corresponding to startdate,
             ex : '2019-08-01 00:00:00+05:30'

  end_date : type string
             time stamp corresponding to end date,
             ex : '2019-08-05 00:00:00+05:30'

  pollutant_ID: type integer
              A pollutant ID correspoinding to 
              a pollutant, ex: 1 for PM2.5
  """

    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import folium
    from folium.plugins import TimestampedGeoJson
    import branca.colormap as cm
    import json

    pollutants = {
        1: {
            "notation": "PM2.5",
            "name": "Particulate matter < 10 µm",
            "bin_edges": np.array([10, 20, 30, 40, 50, 70, 100, 150, 200]),
        },
        2: {
            "notation": "SO2",
            "name": "Sulphur dioxide",
            "bin_edges": np.array([15, 30, 45, 60, 80, 100, 125, 165, 250]),
        },
        3: {
            "notation": "PM10",
            "name": "Particulate matter < 10 µm",
            "bin_edges": np.array([10, 20, 30, 40, 50, 70, 100, 150, 200]),
        },
        4: {
            "notation": "O3",
            "name": "Ozone",
            "bin_edges": np.array([30, 50, 70, 90, 110, 145, 180, 240, 360]),
        },
        5: {
            "notation": "NO2",
            "name": "Nitrogen dioxide",
            "bin_edges": np.array([25, 45, 60, 80, 110, 150, 200, 270, 400]),
        },
        6: {
            "notation": "CO",
            "name": "Carbon monoxide",
            "bin_edges": np.array([1.4, 2.1, 2.8, 3.6, 4.5, 5.2, 6.6, 8.4, 13.7]),
        },
    }

    def color_coding(poll, bin_edges):
        """ Maps polluatnt value to the bins
    """
        idx = np.digitize(poll, bin_edges, right=True)
        return color_scale[idx]

    def prepare_data(df):
        """ Returns a df for selected time range
        indexed by location and time stamp.
        Adds a color column according to the pollutant value.
    """
        print("Preparing the data frame...")
        df[date_time_col_name] = pd.to_datetime(df[date_time_col_name])
        df = df[
            (df[date_time_col_name] >= start_date)
            & (df[date_time_col_name] <= end_date)
        ]

        df = df.set_index(keys=[location_col_name, date_time_col_name])
        df = df.sort_index()

        df[value_col_name] = df.groupby(level=0)[value_col_name].bfill().fillna(0)
        df["color"] = df[value_col_name].apply(
            color_coding, bin_edges=pollutants[pollutant_ID]["bin_edges"]
        )
        print(df.head(5))
        return df

    def create_geojson_features(df):
        """ Creates a Geo JSON
    """
        print("Creating Geo JSON...")
        features = []
        for _, row in df.iterrows():
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row[longitude_col_name], row[latitude_col_name]],
                },
                "properties": {
                    "popup": row[location_col_name].__str__()
                    + "\n"
                    + pollutants[pollutant_ID]["notation"]
                    + " "
                    + row[value_col_name].__str__()
                    + " µg/m³",
                    "time": row[date_time_col_name].__str__(),
                    "style": {"color": row["color"]},
                    "icon": "circle",
                    "iconstyle": {
                        "fillColor": row["color"],
                        "fillOpacity": 0.8,
                        "stroke": "true",
                        "radius": 7,
                    },
                },
            }
            features.append(feature)
        return features

    def make_map(features):
        """ Returns a HTML file with time interactive scatter plot
    """
        print("Plotting the map...")
        pollution_map = folium.Map(
            width=width,
            height=height,
            location=location,
            zoom_start=zoom_start,
            control_scale=True,
            tiles=tiles,
            min_lat=min_lat,
            max_lat=max_lat,
            min_lon=min_lon,
            max_lon=max_lon,
        )

        colormap.add_to(pollution_map)

        TimestampedGeoJson(
            {"type": "FeatureCollection", "features": features},
            period=period,
            add_last_point=True,
            auto_play=False,
            loop=False,
            max_speed=1,
            loop_button=True,
            date_options=date_options,
            time_slider_drag_update=True,
        ).add_to(pollution_map)
        print("Saved the map.")
        return pollution_map

    # =============================================================================
    #     Creates a colormap for legend.
    # =============================================================================
    color_scale = np.array(
        [
            "#053061",
            "#2166ac",
            "#4393c3",
            "#92c5de",
            "#d1e5f0",
            "#fddbc7",
            "#f4a582",
            "#d6604d",
            "#b2182b",
            "#67001f",
        ]
    )
    colormap = cm.LinearColormap(colors=color_scale, vmin=0, vmax=200)
    colormap = colormap.to_step(index=pollutants[pollutant_ID]["bin_edges"])
    colormap.caption = pollutants[pollutant_ID]["notation"] + " gradient scale"

    # =============================================================================
    #     Prepares the data frame.
    #     Creates a Geo JSON to be added to map.
    # =============================================================================
    clean_df = prepare_data(df)
    clean_df = clean_df.reset_index()

    features = create_geojson_features(clean_df)
    map_ = make_map(features)

    return map_
