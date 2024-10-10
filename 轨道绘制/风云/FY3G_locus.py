import folium
import pandas as pd

df = pd.read_csv('轨道绘制/风云/FY3G_geodata_2024_401-407_corrected.csv')
df_station = pd.read_csv('轨道绘制/地面站/站点三花.csv')

df.rename(columns={
    'DayOfMonth': 'day',
    'Year': 'year',
    'Month': 'month',
    'Hour': 'hour',
    'Minute': 'minute',
    'Second': 'second',
    'Latitude': 'latitude',
    'Longitude': 'longitude'
}, inplace=True)

df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute', 'second']])

center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=center, zoom_start=10)

layer_control = folium.LayerControl()
base_group = folium.FeatureGroup(name='Base Group').add_to(m)


df['day'] = df['date'].dt.date 
for day, group in df.groupby(df['day']):

    subgroup = folium.FeatureGroup(name=str(day)).add_to(m)

    points = list(zip(group['latitude'], group['longitude']))

    folium.PolyLine(
        points,
        color="blue",  
        weight=10,  
        opacity=0.5,  
    ).add_to(subgroup)

for _, row in df_station.iterrows():
    folium.Marker(
        location=[row['y'], row['x']],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(base_group)

m.add_child(folium.LayerControl())

m.save("trajectory_map.html")

