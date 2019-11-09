#!/usr/bin/env python
# coding: utf-8

# In[1]:


import altair as alt
from vega_datasets import data
import pandas as pd


# In[2]:


alt.data_transformers.enable('json')
alt.renderers.enable('notebook')


# # Airports of the World
# 
# ## An Interactive Altair Scatterplot

# The following airports data is taken from [this website](https://openflights.org/data.html). The raw data is hosted on Github and can be accessed [here](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat).
# 
# The idea was originally inspired by [this plot](https://vega.github.io/vega-lite/examples/geo_rule.html) in Vega, however the direction in which I took my plot changed quite a bit through the process of making this visualization.

# In[6]:


# loading the data

airports_data_full = pd.read_csv('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat', header = None)


# In[7]:


airports_data_full.head()


# In[8]:


# This cell contains the necessary wrangling
# I renamed the columns from numbers to descriptive labels, subsetted only the columns that I needed to plot, and cleaned up the timezone column by removing rows containing "\\N" and rounding the timezones represented as floats to the nearest integer.

airports_data = airports_data_full.rename(columns={0: "airport_id", 1: "name", 2: "city", 3: "country", 4: "iata", 5: "icao", 6: "latitude", 7: "longitude", 8: "altitude", 9: "timezone", 10: "dst", 11: "timezone2", 12: "tz", 13: "type"})

airports_data = airports_data[['name', 'city', 'country', 'latitude', 'longitude', 'timezone']]

airports_data = airports_data[airports_data['timezone'] != "\\N"]

airports_data['timezone'] = airports_data['timezone'].astype(float).round().astype(int)

airports_data.head()


# > The following is a scatterplot showing the geographic coordinates of all the airports in the world which are listed in the `airports_data` dataframe. The points are colored by timezone, which ranges from -12 to 13. The plot is interactive, and hovering over a point will provide the name of the airport, the main city which it serves, the country that it is located in, and its timezone. I find it very interesting how clearly the map of the world shows up when this data is plotted, and which areas of the world have the highest concentration of airports.

# In[27]:


airports = alt.Chart(airports_data).mark_point(filled=True, size = 4).encode(
    alt.X("longitude", title = "Longitude"),
    alt.Y("latitude", title = "Latitude"),
    alt.Color("timezone:N", title = "Timezone"),
    tooltip = ['name', 'city', 'country', 'timezone']
).properties(
    width=700,
    height=500,
    title = "Airports of the World"
).project('naturalEarth1')

airports

