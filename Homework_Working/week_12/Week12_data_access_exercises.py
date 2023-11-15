# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis

# %%
# Exercise 1:
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 

def pull_data(stationID, start_date, end_date):
    url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + stationID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no', 'datetime',
                                                   'flow', 'code'],parse_dates=['datetime'],
                                                   index_col=['datetime'])
    return data


site = '09506000'
start = '2022-11-14'
end = '2023-11-14'

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
