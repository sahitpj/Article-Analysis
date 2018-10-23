import csv 
import pandas as pd

data = []
with open('data.csv', 'r') as File: 
    reader = csv.DictReader(File)
    for row in reader:
        data.append(row)


df = pd.DataFrame(data)

df_f = []
for i in xrange(len(df)):
    if int(df.iloc[i]['flag']) == 1:
        #print df.loc[i]
        d = {
            'filename': df.iloc[i]['filename'],
            'keywords': df.iloc[i]['keywords'],
            'link':df.iloc[i]['link'],
            'place':df.iloc[i]['place'],
            'year': int(df.iloc[i]['year']),
            'month': int(df.iloc[i]['month']),
        }
        df_f.append(d)

df_final = pd.DataFrame(df_f)

"""
first visu - place wise
"""


import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import numpy as np


# from geopy.geocoders import Nominatim
# geolocator = Nominatim()

# fig = plt.figure(num=None, figsize=(12, 8) )
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='c')
# m.drawcoastlines()
# #m.fillcontinents(color='tan',lake_color='lightblue')
# m.drawparallels(np.arange(-90.,91.,30.),labels=[True,True,False,False],dashes=[2,2])
# m.drawmeridians(np.arange(-180.,181.,60.),labels=[False,False,False,True],dashes=[2,2])
# m.drawmapboundary(fill_color='lightblue')
# count = 0
# for i in xrange(len(df_final)):
#     try:
#         r = df_final.loc[i]
#         location = geolocator.geocode(r['place'])
#         longitude = location.longitude
#         latitude = location.latitude  
#         x,y = m(longitude, latitude)
#         year_ = int(r['year'])
#         if year_ == 207: 
#             m.plot(x,y,marker='o',color='r',markersize=2)
#         elif year_ == 2018:
#             m.plot(x,y,marker='o',color='b',markersize=2)
#         count += 1
#     except:
#         None
        
# plt.title("PM Speeches")   
# plt.show() 




d1 = {}
for i in xrange(len(df_final)):
    try:
        d1[df_final.iloc[i]['place']] += 1
    except:
        d1[df_final.iloc[i]['place']] = 1


print d1
    



d = {'hyderabad': 36, 'sangam': 1, 'karwar': 2, 'guwahati': 5, 'mumbai': 73, 'thane': 6, 'raipur': 4, 'krishnagiri': 1, 'amritsar': 2, 'pilibhit': 2, 'kannur': 1, 'thrissur': 1, 'coimbatore': 9, 'chennai': 19, 'tripunithura': 1, 'noida': 18, 'vasco': 1, 'agartala': 1, 'allahabad': 1, 'rudrapur': 1, 'panchkula': 5, 'meerut': 1, 'manali': 1, 'surat': 2, 'bhiwandi': 1, 'darjeeling': 1, 'madurai': 8, 'attari': 1, 'kozhikode': 2, 'panaji': 5, 'goa': 1, 'rohtak': 2, 'burdwan': 1, 'bareilly': 4, 'bhopal': 15, 'shimla': 4, 'chenna': 1, 'chandrapur': 1, 'vijayawada': 4, 'chikkamagaluru': 1, 'bhubaneswar': 2, 'pune': 20, 'lucknow': 27, 'jaipur': 10, 'ambernath': 1, 'barwani': 1, 'puducherry': 3, 'hubballi': 3, 'kanpur': 6, 'titwala': 1, 'dehradun': 3, 'ballia': 1, 'guirgaon': 1, 'dharamshala': 3, 'agra': 6, 'ranchi': 3, 'NA': 188, 'bengaluru': 32, 'patna': 14, 'mangaluru': 6, 'jaisalmer': 1, 'chandigarh': 21, 'erode': 1, 'rajkot': 3, 'jabalpur': 1, 'tuticorin': 1, 'palwal': 1, 'udupi': 1, 'ahmedabad': 12, 'gurugram': 15, 'kota': 1, 'tirupur': 1, 'kanyakumari': 1, 'gaya': 1, 'bijnor': 1, 'bankura': 1, 'palanpur': 1, 'indore': 7, 'kolhapur': 1, 'patiala': 5, 'ghaziabad': 7, 'visakhapatnam': 7, 'thiruvananthapuram': 7, 'jamshedpur': 1, 'salem': 2, 'nashik': 3, 'ludhiana': 15, 'mysuru': 2, 'trichy': 4, 'kendrapada': 1, 'tirupati': 1, 'varanasi': 1, 'vadodara': 22, 'ambala': 2, 'itanagar': 1, 'kolkata': 25, 'gurgaon': 2, 'tiruvannamalai': 1, 'aurangabad': 3, 'srinagar': 4, 'nawada': 1, 'imphal': 4, 'ajnala': 1, 'thiruvanathapuram': 2, 'nagpur': 22, 'malappuram': 3, 'bathinda': 4, 'kochi': 3}