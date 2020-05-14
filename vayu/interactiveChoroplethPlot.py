# -*- coding: utf-8 -*-

"""
Created on Mon Aug 26 15:30:00 2019
@author: Tanmay Srivastava, Prerna Khanna
"""
#!/usr/bin/env python

def interactiveChoroplethPlot(
  gdf,
  df,
  pollutant,
  country,
  date_time_col_name,
  value_col_name,
  dist_col_name,
  start_date,
  end_date,
  opacity = 0.4
  ):
  
  """ Plots an Interactive Choropleth Plot
      of a given pollutant for given duration 
      of time.

  Parameters
  ----------

  gdf: geo pandas data frame 
       minimally containing DISTRICT	and geometry

  df: data frame 
      minimally containing time stamps and pollutant value

  pollutant: type string
             Name of pollutant ex: 'pm25'
  
  India: type string
         Name of country ex: 'India'            

  date_time_col_name: type string
                      name of column in df having time stamps

  value_col_name: type string
                  name of column in df having value of pollutant concentration
   
  dist_col_name: type string
                 name of column in df having district number            
  
  start_date: type string
              time stamp corresponding to startdate,
              ex : '2019-08-20-06:00'

  end_date: type string
            time stamp corresponding to end date,
            ex : '2019-08-20-23:00'
  
  opacity: type float
           A float value in range 0 to 1
           1 represents maximum opacity           
  """
  import plotly.graph_objects as go
  import plotly
  from folium import IFrame
  import matplotlib.pyplot as plt
  import geopandas as gpd
  import pandas as pd
  import numpy as np
  import seaborn as sns
  import folium
  import branca.colormap as cm
  import json
  from string import Template
  from folium.plugins import TimeSliderChoropleth
  from copy import deepcopy
  import os
  from .utils import Legend

  def color_coding(poll, bin_edges):
    """ Maps polluatnt value to the bins
    """
    idx = np.digitize(poll, bin_edges, right=True)
        
    return colors[idx] 
  
  def prepare_df(df):
    """ Returns a df for selected time range 
        and coverts timestamp to date time format.
        Adds a color column according to the pollutant value.
    """
    df = df[
            (df[date_time_col_name] >= start_date)
            & (df[date_time_col_name] <= end_date)
            ]
    time_ = df[date_time_col_name]
    df[date_time_col_name] = pd.to_datetime(time_).dt.strftime('%s')
    df = df.set_index(keys = [dist_col_name, date_time_col_name])
    df["color"] = df[value_col_name].apply(
        color_coding, bin_edges = cvals
    )
    df = df.reset_index()
    print(df.head())
    
    return df
    
  def create_popup_df(plot):
    """ Returns a df for selected time range.
        Adds a color column according to the pollutant value.
    """
    plot = plot[
            (plot[date_time_col_name] >= start_date)
            & (plot[date_time_col_name] <= end_date)
            ]
    plot = plot.set_index(keys = [dist_col_name, date_time_col_name])
    plot["color"] = plot[value_col_name].apply(
        color_coding, bin_edges = cvals
    )
    plot = plot.reset_index()
    
    return plot

  def prepare_style_dict(df, opacity):
    """
    Prepares a dictionary in the given format:

    styledict = {
            '0': {
            '2017-1-1': {'color': 'ffffff', 'opacity': 1}
            '2017-1-2': {'color': 'fffff0', 'opacity': 1}
            ...
            },
            ...,
            'n': {
            '2017-1-1': {'color': 'ffffff', 'opacity': 1}
            '2017-1-2': {'color': 'fffff0', 'opacity': 1}
            ...
            }
          }"""  
                
    features = {}
    for _, row in df.iterrows():  

      if row[dist_col_name] in features:    
        features[row[dist_col_name]].update({row[date_time_col_name]: {'color': row['color'],'opacity': opacity}
                                  })   
      else:
        feature = {
            row[dist_col_name] : {
                row[date_time_col_name]: {'color': row['color'],'opacity': opacity}
            }
        }    
        features.update(feature)  

    return features 

  def create_popup(index, district):
    """Creates an interactive timeseries popup for
       each district.    
    """
    district = str(district)
    i = index *97
    j = i + 97
    pop = plot[i:j]

    fig = go.Figure([go.Scatter(x=pop[date_time_col_name], y=pop[value_col_name])])
      
    fig.update_layout(
        title = Legend.country_pollutants[country][pollutant]["notation"],            
        xaxis_title="Time Stamp",
      yaxis_title="Pollutant Concentration (µg/m³)"
      )
    fig.update_xaxes(showticklabels=False)

    script = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')  

    html_start = """
    <html>
    <head>
      <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
    <h1>"%s"</h1>""" %district

    html_end = """
    </body>
    </html>"""

    html_final = html_start + script + html_end

    resolution, width, height = 75, 7, 5
    iframe = IFrame(html_final, width=(width*resolution)+75, height=(height*resolution)+50)
  
    return iframe 
  
  def make_map(gdf, geo, features):
    """ Returns a HTML file with time interactive choropleth plot
    """
    m = folium.Map([22, 82], tiles='Stamen Terrain', zoom_start=5)

    g = TimeSliderChoropleth(
        geo,
        styledict = features,
        ).add_to(m)

    colormap.add_to(m)
    style = {'fillColor': '#00000000', 'color': '#00000000'}

    #### adding tooltip #####
    '''folium.GeoJson(geo, tooltip = folium.features.GeoJsonTooltip(
        fields=['DISTRICT']),style_function=lambda x: style,
        ).add_to(m)'''

    for index, row in gdf.iterrows():  
      gs = folium.GeoJson(row['geometry'],style_function=lambda x: style)
      label = create_popup(index, row['DISTRICT'])

      folium.Popup(label, max_width=2560).add_to(gs)
      gs.add_to(m)
      
      if(index%20 == 0):
        print("Done for Districts ", index, " out of 640")
    
    m.save('TimeSliderChoropleth.html')
    print("Map created")
    return m

  def change_style(map_):
    """Changes time slider style.
       Makes the slider background transparent.
    """
    style_add = """
    <style>
      .slidecontainer {
        width: 90%;
      }
      
      .slider {
      -webkit-appearance: none;
      width: 100%;
      height: 15px;
      border-radius: 5px;  
      background: #383838;
      outline: none;
      opacity: 0.7;
      -webkit-transition: .2s;
      transition: opacity .2s;
    }

    .slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 25px;
      height: 25px;
      border-radius: 50%; 
      background: #02bd09;
      cursor: pointer;
    }

    .slider::-moz-range-thumb {
      width: 25px;
      height: 25px;
      border-radius: 50%;
      background: #02bd09;
      cursor: pointer;
    }
      </style>
    """
    f = open(os.path.join(os.getcwd(), 'TimeSliderChoropleth.html'),"r").read()
    insert_pos_1 =f.find("""<script src="https://d3js.org/d3.v4.min.js"></script>""")
    g = deepcopy(f)
    g = f[:insert_pos_1] + style_add + f[insert_pos_1:]

    style_2 = """.attr('class', 'slider')"""
    insert_pos_2 = g.find(""".style('align', 'center');""")
    j = deepcopy(g)
    j = g[:insert_pos_2] + style_2 + g[insert_pos_2:]

    '''style_3 = """position: absolute;"""
    insert_pos_3 = j.find("""  
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
        """
    )
    l = deepcopy(j)
    l = j[:insert_pos_3] + style_3 + j[insert_pos_3:]  

    style_4 = """          
          #slider {
            position:relative;
            z-index:99999;
          }
          #slider-value 
          {
            position:relative;
            z-index:99999; 
          }         
        """
    insert_pos_4 = l.find("""
    </style>

    <style>
      .slidecontainer {
        width: 90%;
      }
    """
    ) 
    k = deepcopy(l)
    k = l[:insert_pos_4] + style_4 + l[insert_pos_4:] ''' 
         
    with open("TimeSliderChoropleth.html","w") as h:
      h.write(j)
    print("Map saved")  


  # =============================================================================
  #     Creates a colormap for legend.
  # =============================================================================

  cvals  = Legend.country_pollutants[country][pollutant]['bin_edges']
  colors = Legend.country_pollutants[country][pollutant]['color_scale']

  colormap = cm.LinearColormap(colors=colors, vmin=0, vmax=600, index = cvals)
  colormap.caption = Legend.country_pollutants[country][pollutant]["notation"] + " gradient scale"

  # =============================================================================
  #     Converts geo pandas df to json format
  # =============================================================================  
  geo = json.loads(gdf.to_json())
  plot = df

  # =============================================================================
  #     Prepares the Dataframe
  # ============================================================================= 

  data_frame = prepare_df(df)
  pop_up_data_frame = create_popup_df(plot)
  style_dict = prepare_style_dict(data_frame, opacity)
  map_ = make_map(gdf, geo, style_dict)
  map_ = change_style(map_)

  return map_