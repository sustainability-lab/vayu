# -- coding utf-8 --

Created on Thu Jul 25 143303 2019

@author Man Vinayaka

def interpolPlot(dataFile,pollutant,shapeFile)
    
    from polire.trend.trend import Trend
    import pandas as pd
    from sklearn.model_selection import train_test_split
    import matplotlib.pyplot as plt
    import numpy as np
    from geopandas import GeoDataFrame
    from shapely.geometry import Polygon, MultiPolygon
    
    df = pd.read_csv(dataFile)
    
    some_value = pollutant
    df = df.loc[df['Parameter Name'] == some_value]
    
    some_value = '2018-05-07'
    df = df.loc[df['Date Local'] == some_value]
    
    df = df.sample(frac=1)
    
    df_train, df_test = train_test_split(df, test_size=0.2)
    
    trainX = df_train[['Longitude', 'Latitude']].values
    trainy = df_train['Arithmetic Mean'].values
    
    def collec_to_gdf(collec_poly)
        Transform a `matplotlib.contour.QuadContourSet` to a GeoDataFrame
        polygons, colors = [], []
        for i, polygon in enumerate(collec_poly.collections)
            mpoly = []
            for path in polygon.get_paths()
                try
                    path.should_simplify = False
                    poly = path.to_polygons()
                    # Each polygon should contain an exterior ring + maybe hole(s)
                    exterior, holes = [], []
                    if len(poly)  0 and len(poly[0])  3
                        # The first of the list is the exterior ring 
                        exterior = poly[0]
                        # Other(s) are hole(s)
                        if len(poly)  1
                            holes = [h for h in poly[1] if len(h)  3]
                    mpoly.append(Polygon(exterior, holes))
                except
                    print('Warning Geometry error when making polygon #{}'
                          .format(i))
            if len(mpoly)  1
                mpoly = MultiPolygon(mpoly)
                polygons.append(mpoly)
                colors.append(polygon.get_facecolor().tolist()[0])
            elif len(mpoly) == 1
                polygons.append(mpoly[0])
                colors.append(polygon.get_facecolor().tolist()[0])
        return GeoDataFrame(
            geometry=polygons,
            data={'RGBA' colors},
            crs={'init' 'epsg4326'})
        
    plt.figure(figsize=(14, 8))
    h = plt.scatter(trainX[, 0], trainX[, 1], c = trainy)
    plt.title(The training set used.)
    plt.colorbar(h)
    
    # data = np.pr('temp.csv', delimiter=',')
    x = trainX[, 0]
    y = trainX[, 1]
    
    z = trainy
    x1max, x2max = np.max(trainX, axis=0)
    x1min, x2min = np.min(trainX, axis=0)
    xi = np.linspace(x1min, x1max, 100)
    yi = np.linspace(x2min, x2max, 100)
    Xi, Yi = np.meshgrid(xi, yi)
    t = Trend(order=2)
    t.fit(trainX, z)
    
    # zi = t.predict(np.asarray([Xi.ravel(), Yi.ravel()]).T)
    zi = t.predict_grid((x1min, x1max), (x2min, x2max)).reshape(100, 100)
    zi = zi.reshape(Xi.shape)
    
    nb_class = 15 # Set the number of class for contour creation
    # The class can also be defined by their limits like [0, 122, 333]
    collec_poly = plt.contourf(
        Xi, Yi, zi, nb_class, 
        vmax=abs(zi).max(), vmin=-abs(zi).max(),
        cmap='inferno',
    )
    
    gdf = collec_to_gdf(collec_poly)
    
    boundary = GeoDataFrame.from_file(shapeFile)
    boundary.drop(boundary.index[[34, 35, 36, 40, 41,49,31]], inplace=True)
    #boundary
    
    ax = boundary.plot(color='white', edgecolor='black',
                       figsize=(40, 40))
    gdf.plot(ax=ax, alpha=0.4, cmap='inferno')



# =============================================================================
# a =  interpolData.csv
# b =  'Ozone'
# c = 'tl_2017_us_state.shp'
# interpolPlot(a,b,c)
# =============================================================================
