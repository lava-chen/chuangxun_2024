'''from gmplot import GoogleMapPlotter

# 定义地图中心和缩放级别
center_lat = 37.7749  # 纬度
center_lng = -122.4194  # 经度
zoom = 10
apikey = ''  # 替换为您的Google Maps API密钥

# 初始化自定义地图
gmap = GoogleMapPlotter(center_lat, center_lng, zoom, apikey)

# 定义卫星扫描轨迹的坐标（示例）
latitudes = [37.7749, 37.7849, 37.7949, 37.8049, 37.8149]
longitudes = [-122.4194, -122.4094, -122.3994, -122.3894, -122.3794]

# 在地图上绘制轨迹
gmap.plot(latitudes, longitudes, 'blue', edge_width=2)  # 轨迹颜色为蓝色

# 绘制地图
gmap.draw("satellite_track.html")  # 输出为HTML文件'''

import folium

# 创建一个中心在特定坐标的地图
my_map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# 添加标记
folium.Marker([40.7128, -74.0060], popup="New York").add_to(my_map)

# 保存为 HTML 文件
my_map.save("my_map.html")
