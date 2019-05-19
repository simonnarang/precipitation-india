import csv
import pandas as pd
import requests
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA356m4BlWKTUjGBC37v1967x1SjSrYcAg')

components = dict()
components['country'] = 'India'
components['postal_code_prefix'] = '764'
result = gmaps.geocode('Koraput')[0]

print(result)

# for i in range(2010, 2017):
# with open('precip.2010.txt.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split('    ') for line in stripped if line)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)

precip_2017 = pd.read_csv("precip.2017.txt",
                 delim_whitespace=True,
                 # nrows=5,
                 # usecols=range(0,14),
                 header=None)
print(df[0])

# geodata = dict()
# geodata['lat'] = result['geometry']['location']['lat']
# geodata['lng'] = result['geometry']['location']['lng']
# geodata['address'] = result['formatted_address']
#
# print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
