import csv
import pandas as pd
import requests
import googlemaps
from datetime import datetime
import numpy as np
from statistics import mean
import json

threshold = 1e-5

def file_name_for_year(year):
    return 'precip.' + str(year) + '.txt'

gmaps = googlemaps.Client(key="AIzaSyD8EhjC417yAfHz3u5wbQr7F2g9zIzArT4")
districts = pd.read_csv("district_list_original.csv")

# Geocode each of the 51 cities
city_info_dict = dict()
for index, row in districts.iterrows():
    res = gmaps.geocode(row['District Name'], components=dict(country="India"))
    city_info_dict[row['District Name']] = res[0]
    #print(res)

# Geocode each of the 51 districts
district_info_dict = dict()
for index, row in districts.iterrows():
    res = gmaps.geocode("%s District" %(row['District Name']), components=dict(country="India"))
    district_info_dict[row['District Name']] = res[0]
    #print(res)

bounding_boxes_dict = dict()
for name, district in district_info_dict.items():
    if district["address_components"][0]["long_name"] != city_info_dict[name]["address_components"][0]["long_name"]:
        v = city_info_dict[name]
        # Please Check these districts
        print("Name = {}\ncity_info = {}\ndistrict_info = {}".format(name, city_info_dict[name], district))
    else:
        v = district
    lat_0 = v['geometry']['bounds']['southwest']['lat']
    lat_1 = v['geometry']['bounds']['northeast']['lat']
    lng_0 = v['geometry']['bounds']['northeast']['lng']
    lng_1 = v['geometry']['bounds']['southwest']['lng']
    bounding_boxes_dict[name] = (min(lat_0, lat_1), max(lat_0, lat_1), min(lng_0, lng_1), max(lng_0, lng_1))

def intersection(lat, lng, box):
    lat_0 = max(lat-0.25, box[0])
    lat_1 = min(lat+0.25, box[1])
    lng_0 = max(lng-0.25, box[2])
    lng_1 = min(lng+0.25, box[3])
    return 0.0 if (lat_0+threshold>lat_1) or (lng_0+threshold>lng_1) else (lat_1-lat_0)*(lng_1-lng_0)

count = 0
results = list()
for year in range(2010, 2017+1):
    year_data = pd.read_csv(file_name_for_year(year), delim_whitespace=True, header=None)
    shape = year_data.values.shape
    year_data_dict = {
        (year_data.values[i][0], year_data.values[i][1], ): year_data.values[0][2:]
        for i in range(shape[0])
    }
    for name, v in bounding_boxes_dict.items():
        total_area = (v[1]-v[0])*(v[3]-v[2])
        # all possible intersection (lat, lng) pairs
        r = [x//0.5*0.5+0.25 for x in v]
        lats = list()
        x = r[0]
        while x<=r[1]:
            lats.append(x)
            x += 0.5
        lngs = list()
        x = r[2]
        while x<=r[3]:
            lngs.append(x)
            x += 0.5
        # intersections of bounding box and [lat-0.25, lat+0.25]*[lng-0.25, lng+0.25]
        intersections = [(intersection(lat, lng, v), year_data_dict[(lng, lat,)]) for lat in lats for lng in lngs if (lng, lat,) in year_data_dict]
        # sum of area of intersections should == area of bounding box
        accumulated_area = sum([x[0] for x in intersections])
        if not abs(accumulated_area - total_area) < threshold:
            # Check! there are missing points
            print("Name = {}\nYear = {}".format(name, year))
            count += 1
        monthly_result = [sum([x[0] / accumulated_area * x[1][i] for x in intersections]) for i in range(12)]
        results.append({
            'District Name': name + str(year),
            'January': monthly_result[0],
            'February': monthly_result[1],
            'March':monthly_result[2],
            'April':monthly_result[3],
            'May':monthly_result[4],
            'June':monthly_result[5],
            'July':monthly_result[6],
            'August':monthly_result[7],
            'September':monthly_result[8],
            'October':monthly_result[9],
            'November':monthly_result[10],
            'December':monthly_result[11],
        })
print('RESULTS:')
print(results)
print('MISSING DATA:')
print(count)
# f = open(results)
# data = json.load(f) f.close()
#
# f=csv.writer(open('results.csv','wb+'))
#
# for item in data: f.writerow([item['pk'], item['model']] + item['fields'].values())