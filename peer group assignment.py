#!/usr/bin/env python
# coding: utf-8

# ## Capstone Project

# ### 1.Introduction

# In Module 3, we explored New York City and the city of Toronto and segmented and clustered their neighborhoods. Both cities are very diverse and are the financial capitals of their respective countries. One of the ideas would be to compare the neighborhoods of the two cities and determine how similar or dissimilar they are.

# And the most important thing is who would be interested in my discussion problem. The answers are the investors who wants to open a restaurant, construct a school or start a company and they want to rent or buy a property estate. The purpose of this project is to help them better understand the Geographical advantages of different districts so that they can have a best choice of all kinds of investments. In addition, the factors on other advantages and disadvantages are considered.

# ### 2.Data used in this project

# To make good use of the foursquare location data, the labs done for Toronto segmented and clustered neighborhoods gave me good examples for new ideas. 
# 
# I would need to leverage the foursquare location data to solve or execute. Data science problems always target an audience and are meant to help a group of stakeholders solve a problem, so make sure that I explicitly describe the audience and why they would care about my problem.
#    
# From the results on New York and Toronto, the lab especially tells 10 most common venues in each district. The data set is about 2014 New York City Neighborhood Names. After transforming the data to Json files, it is easy to use Pandas to transform them into DataFrame. Then select the required data columns to appear and get the information we want. Geopy library is used to get the latitude and longitude values. With the locations the maps can be created and we will have a direct understanding of the neighborhoods and the purposed areas. The Folium library is also used to show maps on different requirements.
# 
# Finally, different analysis on Toronto will give us the related better data to open a company and choose a good place to resident in. And I hope my analysis will do good for them.

# ### 3.Methodology

# (a)  the Foursquare API was utilized because basic geographical location information and particular venues can be explored through Foursquare API. With a specific credentials client ID and secret, the required foursquare data can be accessed.
#  
# (b)  Folium is a great visualization library, the map can directly show us the overall shape of the place we want to know. The detailed information on different venues such as restaurants can be seen in a direct way. The investors can have a better understanding of the city of Toronto to choose his properties. People feel free to zoom into the above map, and click on each circle mark to reveal the name of the neighborhood and its respective borough.
# 
# (c) Json library is a lightweight data-interchange format. It is easy for humans to read and write. This can easily handle JSON files problems.
# 
# (d) k-means clustering was used. K-means is vastly used for clustering in many data science applications, especially useful if you need to quickly discover insights from unlabeled data. K-means include customer segmentation, understand what the visitors of a website are trying to accomplish, pattern recognition and data compression. The project mainly utilized its data compression application in real world. On a series dataset, k-means do good for clustering.
# 
# (e) basic numpy and pandas libraries are fundamental methods because dataframes are the basic tool to do any calculations or simulations. Also, some basic python languages are better utilized.
#    
#    
#   

# ### 4.Results

# From the results part, in east Toronto, most of the neighborhoods have the most common venues of coffee shops, pubs and parks. In central Toronto, most of the neighborhoods have the most common venues of lakes, grocery stores and restaurants. In downtown Toronto, cafes and different kinds of restaurants are distributed in different neighborhoods. There is also a unique place called Gay Bar in Church and Wellesley. In West Toronto, the kind of restaurants are more, such as Vietnamese restaurants and Mexican restaurants.
#   
# Actually, in Toronto, venues types are various and investors can choose their preferable neighborhoods to open the restaurants and the companies. In my opinion, their should be more crowds to make the neighborhood more developed. Data shown in my notebook told us comprehensive kinds of venues in different areas of Toronto.
#     

# ### 5.Discussion

# From data of top 10 common venues in Toronto, the best place for investors to open a restaurant or start a company should not be one, but also several choices. The data only showed us the current numbers of each kind of venues but no other factors such as cost of the place or environment.
# Finally, the investors will compare the several similar venues with less cost and more crowds. The two factors are not concerned in this project but we can estimate from the distribution of top ten common venues in results data from my last part of the notebook.
#    

# ### 6. Conclusion

# The investors to open a restaurant in Toronto should consider several factors. One is the data shown in my notebook, that is how many restaurants in different neighborhoods of every districts of Toronto. Second is the crowds of different districts, which depends on the kinds of venues in different areas. If there is more lakes, the number may be small.
# The investors should consider the competitive restaurants in the district. Try not to compete with those nearby with more similar kinds of restaurants as yours, that may do bad for the kind of investment. But for start a company, it is good to choose the place with more kinds of restaurants so that you will attract more employees to be hired.
#    

# 
