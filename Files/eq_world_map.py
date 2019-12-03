import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#explore the structure of the data
filename = 'data/all_month.geojson'

with open(filename) as f:
    all_eq_data = json.load(f)

mags, lons, lats = [], [], []
all_eq_dicts = all_eq_data["features"]
# print(len(all_eq_dicts))
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Global Earth Quakes in the last 30 days (2019)")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="global_earthquakes.html")
