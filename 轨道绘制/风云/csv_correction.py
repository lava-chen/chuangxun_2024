import pandas as pd
df = pd.read_csv('轨道绘制/风云/FY3G_geodata_2024_401-407.csv')
df = df[df['Latitude'] != -9999.9]

df.to_csv('轨道绘制/风云/FY3G_geodata_2024_401-407_corrected.csv', index=False)
