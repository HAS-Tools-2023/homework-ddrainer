## Exercises for thursday's class

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
# modify the following to create a pandas dataframe where 
# the column 'datetime' is a datetime object. You should do this two ways:
# (1) by modifying the read.table function arguments directly. 
# (2) keeping the read.table line I have below the same and 
# modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 

#Method 1
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'], parse_dates=['datetime'],
                            index_col='datetime')

#Method 2
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])
data.info()

# Parse dates to datetime object
data['datetime'] = pd.to_datetime(data['datetime'])

data.info()
# Set datetime as the index
data = data.set_index('datetime')

# Check it
data.info()
data.head()
data.index

# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using 
# the 'date' column as the index and making sure to treat that column as a datetime object. 

daymet_df = pd.read_csv('daymet.csv', index_col='date', parse_dates=['date'])

#2.2: Explore this dataset and report what variables 
# it contains, what date ranges are covered and the frequency of the data. 

daymet_df.info()

#2.3  Make a scatter plot of day length (dayl) vs 
# maximum temperature. 

fig, ax = plt.subplots()
fig.set_size_inches(10,7)
ax.scatter(daymet_df['dayl (s)'], daymet_df['tmax (deg c)'],
                        marker='x', s=10, color='tomato', label='Daily Max Temp')
ax.set_title='Max Temp vs. Day Length'
ax.legend()

#2.4 Make a plot with three lines (1) average, 
# (2) min and (3) max shortwave radiation (srad) vs the month of the year for all years
# after 2015

#plt.fill, can also use resample "m"
