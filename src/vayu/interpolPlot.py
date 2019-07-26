# -- coding utf-8 --
"""
Created on Thu Jul 25 143303 2019

@author Man Vinayaka
"""


def interpolPlot(
    df, shape_df, long, lat, pollutant, resolution=100, partitions=15, cmap="inferno"
):

    import geopandas
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from geopandas import GeoDataFrame
    from shapely.geometry import Polygon, MultiPolygon
    from sklearn.ensemble import RandomForestRegressor

    from polire.custom import CustomInterpolator

    df = df.sample(frac=1)
    trainX = df[[long, lat]].values
    trainy = df[pollutant].values

    def collec_to_gdf(collec_poly):
        """Transform a `matplotlib.contour.QuadContourSet` to a GeoDataFrame"""
        polygons, colors = [], []
        for i, polygon in enumerate(collec_poly.collections):
            mpoly = []
            for path in polygon.get_paths():
                try:
                    path.should_simplify = False
                    poly = path.to_polygons()
                    # Each polygon should contain an exterior ring + maybe hole(s):
                    exterior, holes = [], []
                    if len(poly) > 0 and len(poly[0]) > 3:
                        # The first of the list is the exterior ring :
                        exterior = poly[0]
                        # Other(s) are hole(s):
                        if len(poly) > 1:
                            holes = [h for h in poly[1:] if len(h) > 3]
                    mpoly.append(Polygon(exterior, holes))
                except:
                    print("Warning: Geometry error when making polygon #{}".format(i))
            if len(mpoly) > 1:
                mpoly = MultiPolygon(mpoly)
                polygons.append(mpoly)
                colors.append(polygon.get_facecolor().tolist()[0])
            elif len(mpoly) == 1:
                polygons.append(mpoly[0])
                colors.append(polygon.get_facecolor().tolist()[0])
        return GeoDataFrame(
            geometry=polygons, data={"RGBA": colors}, crs={"init": "epsg:4326"}
        )

    z = trainy
    x1max, x2max = np.max(trainX, axis=0)
    x1min, x2min = np.min(trainX, axis=0)
    xi = np.linspace(x1min, x1max, resolution)
    yi = np.linspace(x2min, x2max, resolution)
    Xi, Yi = np.meshgrid(xi, yi)
    t = CustomInterpolator(RandomForestRegressor)
    t.fit(trainX, z)

    zi = t.predict(np.asarray([Xi.ravel(), Yi.ravel()]).T)
    zi = zi.reshape(Xi.shape)

    collec_poly = plt.contourf(
        Xi, Yi, zi, partitions, vmax=abs(zi).max(), vmin=-abs(zi).max(), cmap=cmap
    )
    plt.close()

    gdf = collec_to_gdf(collec_poly)
    gdf["geo"] = gdf["geometry"].astype(str)

    res_intersection = geopandas.overlay(shape_df, gdf, how="intersection")
    ax = res_intersection.plot(column="geo", cmap=cmap, figsize=(40, 40))
    plt.axis("off")
    return ax


# =============================================================================
# shapeFile = "re/tl_2017_us_state.shp"
# long = "Logitude"
# lat = "Latitude"
# pollutant = "Arithmetic Mean"
# df = pd.read_csv(daily_44201_2018.csv)
# shape_df = GeoDataFrame.from_file(shapeFile)
# shape_df.drop(shape_df.index[[34, 35, 36, 40, 41,49,31]],
# inplace=True)
# interpolPlot(df, shape_df, long, lat, pollutant)
# =============================================================================
