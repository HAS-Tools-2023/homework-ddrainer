# Starter code from Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../../data', filename)
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

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 100) & (flow_data[:,1]==9))


criteria = (flow_data[:, 3] > 100) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

# Calculate the average flow for these same criteria 

flow_mean = np.mean(flow_data[(flow_data[:,3] > 100) & (flow_data[:,1]==9),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
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
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])

# %%
# Count the number of values with flow > 100 and month ==9
flow_count = np.sum((flow_data[:,3] > 100) & (flow_data[:,1]==9))


criteria = (flow_data[:, 3] > 100) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

flow_mean = np.mean(flow_data[(flow_data[:,3] > 100) & (flow_data[:,1]==9),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# %%

# This is my very rough stab at trying to figure out the streamflow forecast for this week
flow_2week = np.nanmean(flow_data[-14:,3]) # mean of last 14 days
print("The average flow for the last two weeks is ", flow_2week)

flow_4week = np.nanmean(flow_data[-28:,3]) # mean of last 28 days
print("The average flow for the last four weeks is ", flow_4week)

median_2week = np.nanmedian(flow_data[-14:,3]) # median of last 14 days
print("The median flow for the last two weeks is ", median_2week)

median_4week = np.nanmedian(flow_data[-28:,3]) # median of last 28 days
print("The median flow for the last four weeks is ", median_4week)

max_2week = np.nanmax(flow_data[-14:,3]) # max of last 14 days
print("The max flow for the last two weeks is ", max_2week)

max_4week = np.nanmax(flow_data[-28:,3]) # max of last 28 days
print("The max flow for the last four weeks is ", max_4week)


# %%
### HW5 Answers

# #1 Answer -- Create flow_data array created above from the code from last week, create
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
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

# %%
# #2 Answer -- Create a new numpy array that has the same four columns as 
# flow_data but includes only the data for the five year period from 
# 1/1/2015-12/31/2019.

flow_5year = []

# one line of code
flow_5year = flow_data[(flow_data[:, 0] >= 2015) & (flow_data[:, 0] <= 2019),:], print(flow_5year)

# two lines of code
flow_5year = flow_data[(flow_data[:, 0] >= 2015) & (flow_data[:, 0] <= 2019),:]
print(flow_5year)

# use a for loop
# ???

# print out dimensions of flow_5year
print('The dimensions of flow_5year are ', np.shape(flow_5year))
print('There are ', flow_5year.ndim, ' dimensions in the flow_year array.')

# average flow for new 5-year period
print('The mean flow from 2015 to 2019 is ', np.mean(flow_5year[:,3]), 'cfs')

# %%
# Convert the flow from cfs to cf

flow_daily = np.copy(flow_5year) # copy the 5-year data

modified_flow = flow_5year[:,3] * 86400 # multiply only the flow column by 86,400 to convert

flow_daily[:, 3] = modified_flow # replace the data in the array with the new data in cf

print("New Array with cf instead of cfs:")
print(flow_daily)

# %%
# Sum all of the flow data in cf for the 5-year period and get first 5 flow values
# #3 Answers

# Get the total flow
total_flow = np.sum(flow_daily[:,3])

print('The total daily flow for this 5-year period is: ', total_flow, 'cubic feet (cf)')

#%%
# Get the first 5 flow values

flow_first5 = flow_daily[:5, 3]
print('The first 5 flow values are: ', flow_first5)

# %%
# test array stuff

array = [1,2,3]

np.repeat(array, 5)
np.tile(array,5)
np.arange(0,12,2)

# %%
# more test array stuff

array = np.zeros((5,3))

array[:,0] = np.tile(np.arange(2015,2020,1),1)
array[:,1] = np.tile(np.arange(1,6,1),1)


print(array)

# %%
for i in range(5):
    ytemp = array[i,0]
    mtemp = array[i,1]
    print(ytemp,mtemp)
    


# %%
# last question for 60 months of averages

flow_monthly = np.zeros((60,3))

flow_monthly[:,0] = np.tile(np.arange(2015,2020,1),12) # create the years in column 1 (index 0)
flow_monthly[:,1] = np.tile(np.arange(1,13,1),5) # create the months in column 2 (index 1)

print(flow_monthly)

# %%
# Creating the final product

for i in range(60):
    ytemp = flow_monthly[i,0]
    mtemp = flow_monthly[i,1]
    print(ytemp,mtemp)

print(flow_monthly)

# %%
yr_input = 2015
mon_input = 1

new_column_values = []

while yr_input <= 2019:

    while mon_input <= 12:
        target_year = yr_input
        target_month = mon_input
        year_mask = (flow_5year[:, 0] == target_year)
        month_mask = (flow_5year[:, 1] == target_month)
        selected_rows = flow_5year[year_mask & month_mask]
        if len(selected_rows) > 0:
            average_value = np.mean(selected_rows[:, 3])
            #print(f"Average for {target_year}-{target_month}: {average_value}")
        mon_input = mon_input + 1
        new_column_values.append(average_value)

    yr_input = yr_input + 1
    mon_input = 1

new_column = np.array(new_column_values)
new_column = new_column[:, np.newaxis]
flow_monthly = np.column_stack((flow_monthly, new_column))

print(flow_monthly)
# %%
print(flow_monthly[:5])

# HINT1: I would first create an array that has just the months and year values in it an then loop over that to fill in the flow values
#You can create values from 1-12 and repeate those values 5 times to fill in the months using the functions np.arange and np.tile

flow_monthly = np.zeros((60, 3))
months = np.tile(np.arange(1, 13, 1), 5)

# You can then repeat each of the year values 12 times using the function np.arrange and np.repeat
years=np.repeat(np.arange(start=2015, stop=2020, step=1),12)

flow_monthly[:,0]=years
flow_monthly[:,1]=months
nmonth=60

for m in range(nmonth):
    ytemp= flow_monthly[m,0]
    mtemp= flow_monthly[m,1]
    ipick=(flow_data[:,0]==ytemp) & (flow_data[:,1]==mtemp)
    flow_monthly[m,2]=np.mean(flow_data[ipick, 3])
    print('Step', m, 'Year=', ytemp, "Month=", mtemp, "flow", flow_monthly[m,2])

flow_monthly 
# %%
