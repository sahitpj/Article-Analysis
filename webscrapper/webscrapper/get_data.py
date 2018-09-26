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
    
plt.plot(range(len(d.keys())), d.values())
plt.yticks(range(len(d.keys())), d.keys())
plt.show()


