# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import earthpy as et

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('C:\\Users\\dave8\\Desktop\\HAS_tools\\homework-ddrainer\\data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

flow_data.ndim
flow_data.shape
flow_data.dtype
# %%
# Starter Code
# Count the number of values with flow < 100 and month ==9
flow_count = np.sum((flow_data[:,3] < 300) & (flow_data[:,1]==9))

criteria = (flow_data[:, 3]< 300) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.nanmean(pick_data)
flow_median = np.nanmedian(pick_data)

# Calculate the average flow for these same criteria 

crit_flow_mean = np.nanmean(flow_data[(flow_data[:,3] < 300) & (flow_data[:,1]==9),3])

print("Flow meets this criteria", flow_count, " times")
print('And has an average value of', crit_flow_mean, "when this is true")
print('The median flow is', flow_median, 'for this criteria.')

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=20)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')


# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.nanquantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.nanquantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])

# %%
# Plot histogram of Sep data < 300 cfs

plt.hist(pick_data)
plt.title('Streamflow in Sep < 300 cfs')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

print(np.nanmax(pick_data))
print(np.nanmin(pick_data))
print(np.nanmedian(pick_data))

# %%
sep_flow = (flow_data[:, 1] == 9)
sep_pick_data = flow_data[sep_flow, 3]

print(np.nanmax(sep_pick_data))
print(np.nanmin(sep_pick_data))
print(np.nanmedian(sep_pick_data))


#%%
my_sep_bins = np.linspace(0, 1000, num=20)

plt.hist(sep_pick_data, bins = my_sep_bins)
plt.title('Streamflow in Sep (all)')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
print(sep_pick_data)

# %%
