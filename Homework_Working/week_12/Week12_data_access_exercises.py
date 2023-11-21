# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis
import datetime
import os
import json
import urllib.request as req
import urllib

# %%
# Exercise 1:
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location
# and date range. 

def pull_data(stationID, start_date, end_date):
    url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no="+ stationID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no', 'datetime',
                                                   'flow', 'code'],parse_dates=['datetime'],
                                                   index_col=['datetime'])
    return data


site = '09506000'
start = '2022-11-14'
end = '2023-11-19'

pull_data(site, start, end)

# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 

verde1 = pull_data('09506000', start, end)  # Verde River Camp
verde2 = pull_data('09504950', start, end)  # Above Camp Verde
verde3 = pull_data('09508000', start, end)  # Verde River Below East Childs, AZ

#3. Make a timeseries plot showing the data from all 3 gauges.

fig, ax = plt.subplots()
ax.plot(verde1.index, verde1['flow'], label='Verde River Camp', color='green')
ax.plot(verde2.index, verde2['flow'], label='Above Camp Verde', color='blue')
ax.plot(verde3.index, verde3['flow'], label='Below Camp Verde', color='orange')
ax.set(title="Past Year's Flow at \n Selected Sites Along Verde River", xlabel="Date",
       ylabel="Avg Daily Flow (cfs)",
       yscale='log')
ax.legend()
ax.grid()

# %%
# %%
# Exercise 2:

# 1. Download the dataset from the class notes and determine what (1) type of
# python object the station observations are and (2) what all variables are
# included in the observations.

my_token = '7ebaa414907445589854ffb4c4059d23'

base_url = 'https://api.synopticdata.com/v2/stations/timeseries'

# Specific arguments for the data that we want
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': my_token} 

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this 
responseDict = json.loads(response.read())

# Get object type
type(responseDict['STATION'][0]['OBSERVATIONS'])

# Get variables within object observations dict
responseDict['STATION'][0]['OBSERVATIONS'].keys()

#2. Modify the API call to return accumulated precipitation instead
# (variable name = 'precip_accum', set the units to 'metric')
# and make a plot of the daily max accumulated precipitation

my_token = '7ebaa414907445589854ffb4c4059d23'

base_url = 'https://api.synopticdata.com/v2/stations/timeseries'

# Specific arguments for the data that we want
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': my_token}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this 
responseDict = json.loads(response.read())

# Get object type
type(responseDict['STATION'][0]['OBSERVATIONS'])

# Get variables within object observations dict
responseDict['STATION'][0]['OBSERVATIONS'].keys()

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

units = responseDict['UNITS']

data = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').max()

plt.plot(data_daily)
plt.xticks(rotation=45)
plt.xlabel('Date'), plt.ylabel('Accum Precip'), plt.title('Daily Max\n Accumulated Precip')
# %%
