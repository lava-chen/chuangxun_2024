import geopandas as gpd
import pandas as pd

shapefile_path = '轨道绘制/地面站/站点三花.shp'

gdf = gpd.read_file(shapefile_path)
print(gdf.head())

print(gdf['geometry'].geom_type)

print(type(gdf['geometry'].values[0]))

print(gdf['geometry'].values[0].x)

points = pd.DataFrame({'x': [gdf['geometry'].values[i].x for i in range(len(gdf))],
                        'y': [gdf['geometry'].values[i].y for i in range(len(gdf))]})

points.to_csv('轨道绘制/地面站/站点三花.csv', index=False)