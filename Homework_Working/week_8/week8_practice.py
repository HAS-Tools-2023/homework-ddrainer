# %%
# Using old code from last week...b/c it works.

# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name and path to where you have stored the data
filename = '../../data/streamflow_week7.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week7.txt'

# %%
#Read the data into a pandas dataframe
#data=pd.read_table(filepath, sep = '\t', skiprows=31,
#        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
#        )

# Expand the dates to year month day
#data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
#data['year'] = data['year'].astype(int)
#data['month'] = data['month'].astype(int)
#data['day'] = data['day'].astype(int)

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], 
        parse_dates=['datetime'])

#%%
# Line Plot for All Data
fig, ax = plt.subplots()
ax.scatter(data['datetime'], data['flow'])
ax.set_xlabel('Years')
ax.set_ylabel('Streamflow in cfs')
ax.set_title('Streamflow for 1989-2023')

# Line Plot for All Data with Log Y-Scale
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Flow [cfs]",
       yscale='log')

#%%
# Set the datetime column as the index
data = data.set_index('datetime')

#%%
# Now I can plot this even more easily
# it will assume my x axis is the index
fig, ax = plt.subplots()
ax.plot(data['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Flow [cfs]",
       yscale='log')

#%%
data[data.index.year == 2013].head()
data[data.index.month == 5]

#%%

# data["2013"].head() #This line doesn't work

oct_data = data[data.index.month == 10]
oct_mean = oct_data['flow'].resample('w').mean()



fig, ax = plt.subplots()
ax.plot(oct_mean)
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Flow [cfs]")

# %%
