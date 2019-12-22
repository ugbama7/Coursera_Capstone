#!/usr/bin/env python
# coding: utf-8

# ### Capstone Project - PREDICTING THE FUTURE OF GIRL CHILD EDUCATION AMONG NEIGHBOURHOOD IN NIGERIA BY PATRICK MOSES
# 
# 
# 

# ### Introduction: Business Problem:

# 
#  Education is an important foundation to imp-rove the status of women and has also been recognized as a fundamental strategy for development. No sustainable development is possible if women remain un-educated, discriminated against and disenfranchise-sed. Improving and widening access to education, especially basic education, is not only an objective in itself but also accelerates social and economic advancement1. The evidence is out: nations that invest in girls‟ education enhance economic productivity and growth. In fact, the World Bank has stated that there is no investment more effective for achieving development goals than educating girls. 
# The second Millennium Development Goal challenges the international community’s commitment to ensure universal primary school completion and to eliminate gender disparities in primary and secondary education by 2015. This goal is grounded in the recognition that access to basic education is a human right, and a vital part of individuals‟ capacity to lead lives that they value3. In addition, education is a powerful instrument that enables women to access a variety of opportunities, while rendering them less vulnerable to HIV/AIDS, abuse, and exploitation 
# The purpose of this project is to assess the current status of girl-child education in three com-munities in the Zazzau Emirate of Kaduna State in northwestern Nigeria and to predict the future.
# 

#  ### Data Description

# To examine the above said, following data sources will be used:

# #### 1. Dataset from Zazzau Community:
# 

# Having that the dataset for Zazzau comunnity was limited, the newyork city dataset gotten from Link: https://geo.nyu.edu/catalog/nyu_2451_34572 will be used s plain sample to carrout this project.

# Description: the Zazzau Neighborhoo point file will be created just like  New York City Neighborhood Names point file was created as a guide to New York City’s neighborhoods 
# that appear on the web resource, “New York: A City of Neighborhoods.” just like the newyork dataset, the Zazau community will estimates of label centroids were established at a 1:1,000 scale, but are ideally viewed at a 1:50,000 scale. This dataset will provide the addresses of neighborhood of NYC in json format. 
# An extract of the json is as follows: 

# In[4]:


{'type': 'Feature',
'id': 'nyu_2451_34572.306',
'geometry': {'type': 'Point',
'coordinates': [-74.08173992211962, 40.61731079252983]},
'geometry_name': 'geom',
'properties': {'name': 'Fox Hills',
'stacked': 2,
'annoline1': 'Fox',
'annoline2': 'Hills',
'annoline3': None,
'annoangle': 0.0,
'borough': 'Staten Island',
'bbox': [-74.08173992211962,
40.61731079252983,
-74.08173992211962,
40.61731079252983]}}


# ### 2. Foursquare API:
# 
#     Link: https://developer.foursquare.com/docs
#     Description: Foursquare API, a location data provider, will be used to make RESTful API calls to retrieve data about venues in different neighborhoods of Zazzau  . This is the link to Foursquare Venue Category Hierarchy. Venues retrieved from all the neighborhoods are categorized broadly into "Arts & Entertainment", "College & University", "Event", "Food", "Nightlife Spot", "Outdoors & Recreation", etc. An extract of an API call is as follows: 

# In[ ]:


'categories': [{'id': '4bf58dd8d48988d110941735',
'name': 'Italian Restaurant',
'pluralName': 'Italian Restaurants',
'shortName': 'Italian',
'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/italian_',
'suffix': '.png'},
'primary': True}],
'verified': False,
'stats': {'tipCount': 17},
'url': 'http://eccorestaurantny.com',
'price': {'tier': 4, 'message': 'Very Expensive', 'currency'


# 
# ### 2. Methodology
# 
# all  the dependencies need will be downloaded from the various library.
# 

# In[3]:


import numpy as np 
import pandas as pd 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import json 
get_ipython().system('conda install -c conda-forge geopy --yes')
from geopy.geocoders import Nominatim
import requests
from pandas.io.json import json_normalize
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium


# 
# ### Download and Explore Zazzau dataset
# 
# In order to compare the neighborhoods of  Zazzau community, a dataset is required that contains the neighborhoods, with respective latitude and longitude coordinates.
# 
# using the below link dataset
# 
#     To the dataset: https://geo.nyu.edu/catalog/nyu_2451_34572, and
#     To its downloadable json format file: https://cocl.us/new_york_dataset/newyork_data.json
# 
# 

# In[4]:


get_ipython().system("wget -q -O 'newyork_data.json' https://ibm.box.com/shared/static/fbpwbovar7lf8p5sgddm06cgipa2rxpe.json")
print('Data downloaded!')


# All the relevant data is in the features key, which is basically a list of the neighborhoods. So, let's define a new variable that includes this data.

# In[7]:


with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)
newyork_data


# In[9]:


neighborhoods_data = newyork_data['features']


# In[11]:




neighborhoods_data[305]


# We then Tranform the data into a pandas dataframe

# In[14]:


column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude']
neighborhoods = pd.DataFrame(columns=column_names)


for data in neighborhoods_data:
    borough = neighborhood_name = data['properties']['borough'] 
    neighborhood_name = data['properties']['name']
    neighborhood_latlon = data['geometry']['coordinates']
    neighborhood_lat = neighborhood_latlon[1]
    neighborhood_lon = neighborhood_latlon[0]
    neighborhoods = neighborhoods.append({'Borough': borough,'Neighborhood': neighborhood_name,'Latitude': neighborhood_lat,'Longitude': neighborhood_lon}, ignore_index=True)
neighborhoods.head()


# we then Use geopy library to get the latitude and longitude values of New York City.

# In[15]:


address = 'New York City, NY'
geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of New York City are {}, {}.'.format(latitude, longitude))


# we then Create a map of New York with neighborhoods superimposed on top.

# In[17]:


map_newyork = folium.Map(location=[latitude, longitude], zoom_start=10)
for lat, lng, borough, neighborhood in zip(neighborhoods['Latitude'], neighborhoods['Longitude'], neighborhoods['Borough'], neighborhoods['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius = 5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
    parse_html=False).add_to(map_newyork)  
map_newyork


# having that Folium is a great visualization library.zooming into the above map, and click on each circle mark to reveal the name of the neighborhood and its respective borough.

# 
# ### Define Foursquare Credentials and Version
# 
#  we then Utilize the Foursquare API to explore the neighborhoods and segment them.
# 

# In[18]:


CLIENT_ID = 'XOKJYQNJOBDGS1WJQLVWK0KY2MX2LSBS2RQHYZ1IERYGZQM2' # your Foursquare ID
CLIENT_SECRET = 'JMKC15GZW4SFCQV32GOIZTXEJD4IHUGNM5L4U2SEXLBYPLHH' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


# In[30]:


url = 'https://api.foursquare.com/v2/venues/categories?&client_id={}&client_secret={}&v={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION)
category_results = requests.get(url).json()


# 
# #### Explore the first neighborhood to understand the results of GET Request
# 
# Get the neighborhood's name.
# 

# In[34]:




neighborhoods.loc[0, 'Neighborhood']


# Get the neighborhood's latitude and longitude values.

# In[36]:


neighborhood_latitude = neighborhoods.loc[0, 'Latitude'] # neighborhood latitude value
neighborhood_longitude = neighborhoods.loc[0, 'Longitude'] # neighborhood longitude value

neighborhood_name = neighborhoods.loc[0, 'Neighborhood'] # neighborhood name

print('Latitude and longitude values of {} are {}, {}.'.format(neighborhood_name, 
                                                               neighborhood_latitude, 
                                                               neighborhood_longitude))


# 

# In[37]:


LIMIT = 1 # limit of number of venues returned by Foursquare API
radius = 500 # define radius
categoryId = '4d4b7105d754a06374d81259' # category ID for "Food"

# create URL

url = 'https://api.foursquare.com/v2/venues/search?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&categoryId={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    neighborhood_latitude, 
    neighborhood_longitude, 
    radius,
    categoryId,
    LIMIT)
url # display URL


# Send the GET request and examine the resutls

# In[47]:


results = requests.get(url).json()


# 
# 
# ### The category name of the venue 'Carvel Ice Cream' is 'Food'.
# 
# As, our aim is to segment the neighborhoods of NYC with respect to the Food in its vicinity. We need to proceed further to fetch this data from all the 306 neighborhoods' venues.
# Let's create a function to repeat the following process to all the neighborhoods in NYC:
# 
#     Loop through neighborhoods
#         Create the API request URL with radius=500, LIMIT=100
#         Make the GET request
#         For each neighborhood, return only relevant information for each nearby venue
#         Append all nearby venues to a list
#     Unfold the list & append it to dataframe being returned
# 
# The categoryId parameter in the API request URL can be a comma seperated string. So, lets create a comma seperated string from category_dict.
# 

# In[49]:


categoryId_list = []
for key, value in category_dict.items():
    categoryId_list.append(key)
categoryId = ','.join(categoryId_list)


# #### 3. Analysis & Machine Learning
# Let's check the size of the resulting dataframe

# In[50]:


def getNearbyFood(names, latitudes, longitudes, radius=1000, LIMIT=500):
    not_found = 0
    print('***Start ', end='')
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(' .', end='')
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/search?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&categoryId={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius,
            "4d4b7105d754a06374d81259", # "Food" category id
            LIMIT)
            
        try:
            # make the GET request
            results = requests.get(url).json()['response']['venues']
            
            # return only relevant information for each nearby venue
            venues_list.append([(
                name, 
                lat, 
                lng, 
                v['name'], 
                v['location']['lat'], 
                v['location']['lng'],  
                v['categories'][0]['name']) for v in results])
        except:
            not_found += 1


    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Neighborhood', 
                  'Neighborhood Latitude', 
                  'Neighborhood Longitude', 
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
    print("\nDone*** with {} venues with incompelete information.".format(not_found))
    return(nearby_venues)


# Finally, let's visualize the resulting clusters

# In[57]:


manhattan_data = neighborhoods[neighborhoods['Borough'] == 'Manhattan'].reset_index(drop=True)
manhattan_data.head()


# In[58]:


address = 'Manhattan, NY'
geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(latitude, longitude))


# In[59]:


map_manhattan = folium.Map(location=[latitude, longitude], zoom_start=11)
for lat, lng, label in zip(manhattan_data['Latitude'], manhattan_data['Longitude'], manhattan_data['Neighborhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
    [lat, lng],
    radius=5,
    popup=label,
    color='blue',
    fill=True,
    fill_color='#3186cc',
    fill_opacity=0.7,
    parse_html=False).add_to(map_manhattan)  
map_manhattan


# ### 5. Results

# In[61]:


required_column_indices = [2,3,7]
required_column = [list(manhattan_data.values)[i] for i in required_column_indices]
required_column_indices = [2,3,7]


# In[ ]:




