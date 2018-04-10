import gmplot
import json

with open("openrice_data.json") as json_file:
    original_data = json.load(json_file)

gmap = gmplot.GoogleMapPlotter(22.325222,114.1664163, 16)

latitude = []
longitude = []

for original in original_data:  
    for key, value in original.items():              
        if(key in "address"):             
            latitude.append(value[0])
            longitude.append(value[1])

gmap.heatmap(latitude, longitude)

gmap.draw("map.html")