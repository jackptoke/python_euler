import json

#explore the structure of the data
filename = 'data/all_month.geojson'

with open(filename) as f:
    all_eq_data = json.load(f)
    # print(all_eq_data)

# readable_file = 'data/all_month_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

mags, lons, lats = [], [], []
all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[ :10])
print(lons[:5])
print(lats[:5])


