# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
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

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework.
# From here on out you should use only the lists created in the last block:
# flow, date, year, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []
print(ilist)

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 650 and month[i] == 9:
                ilist.append(i)

print(ilist)
# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified
# in the ilist
subset = [flow[j] for j in ilist]
print(subset)

# Alternatively I could have  written the for loop I used
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 650 and month[i]==9]
print(len(ilist2))

# %%
# Trying to get values for the mean, std, min, and max only
# for the month of Sep, had to create a subset to get the flow, otherwise
# it was giving me the line number of code for some reason

ilist3 = []

for i in range(len(flow)):
        if month[i] == 9:
                ilist3.append(i)

subset1 = [flow[j] for j in ilist3]
#print(subset1)

print("The mean flow in Sep is ", np.mean(subset1))
print("The standard deviation is ", np.std(subset1))
print("The max flow is ", np.max(subset1))
print("The min flow is ", np.min(subset1))

#%%
# average data for streamflow since Aug 1, 2023

ilist4 = []

for i in range(len(flow)):
        if year [i] == 2023 and month[i] >= 8:
                ilist4.append(i)

subset2 = [flow[j] for j in ilist4]

#print(subset2)
print("The mean flow in Aug/Sep 2023 is ", np.mean(subset2))
print("The standard deviation is ", np.std(subset2))
print("The max flow is ", np.max(subset2))
print("The min flow is ", np.min(subset2))

# %%
# Getting the object types for flow, year, month, and day for Q1
print(type(flow))
print(type(year))
print(type(month))
print(type(day))

#%%
# Testing objec type of a couple of items in the flow list
print(type(flow[0]))
print(type(flow[883]))

# %%
# Summing all of the object types in flow list
print(sum(isinstance(i, int) for i in flow))
print(sum(isinstance(i, str) for i in flow))
print(sum(isinstance(i, float) for i in flow))
print(sum(isinstance(i, bool) for i in flow))
# %%
# Printing the length of each list
list_of_lists = [flow,year,month,day]

for dlist in list_of_lists:
        print("The length of this list is", len(dlist))

# %%
# This is to calculate how many times the streamflow was greater than my 
# 9 Sep forecast of 48 cfs

ilist5 = []

for i in range(len(flow)):
        if flow [i] > 48:
                ilist5.append(i)

subset3 = [flow[j] for j in ilist5]

x = len(subset3)
y = len(flow)

print(x)
print(y)

print(x/y*100)

# %%
# This is to calculate how many times the streamflow was greater than my 
# 9 Sep forecast of 48 cfs in 2000 or before

ilist6 = []

for i in range(len(flow)):
        if flow [i] > 48 and year[i] <= 2000:
                ilist6.append(i)

subset4 = [flow[j] for j in ilist6]

ilist7 = []

for i in range(len(flow)):
        if year[i] <= 2000:
                ilist7.append(i)

x = len(subset4)
y = len(ilist7)

print(x)
print(y)

print(x/y*100)

# %%
# This is to calculate how many times the streamflow was greater than my 
# 9 Sep forecast of 48 cfs in 2010 or after

ilist8 = []

for i in range(len(flow)):
        if flow [i] > 48 and year[i] >= 2010:
                ilist8.append(i)

subset5 = [flow[j] for j in ilist8]

ilist9 = []

for i in range(len(flow)):
        if year[i] >= 2010:
                ilist9.append(i)

x = len(subset5)
y = len(ilist9)

print(x)
print(y)

print(x/y*100)

# %%
# This is one not very good way to count the numer of objects in list
# and try to print it.
print("This is the type of objects in a year.")
print("This is the ints.")
print(sum(isinstance(i, int) for i in year))
print("This is the strs.")
print(sum(isinstance(i, str) for i in year))
print("This is the floats.")
print(sum(isinstance(i, float) for i in year))
print("This is the bools.")
print(sum(isinstance(i, bool) for i in year))
# %%
print("This is the type of objects in a month.")
print("This is the ints.")
print(sum(isinstance(i, int) for i in month))
print("This is the strs.")
print(sum(isinstance(i, str) for i in month))
print("This is the floats.")
print(sum(isinstance(i, float) for i in month))
print("This is the bools.")
print(sum(isinstance(i, bool) for i in month))
# %%
print("This is the type of objects in a day.")
print("This is the ints.")
print(sum(isinstance(i, int) for i in day))
print("This is the strs.")
print(sum(isinstance(i, str) for i in day))
print("This is the floats.")
print(sum(isinstance(i, float) for i in day))
print("This is the bools.")
print(sum(isinstance(i, bool) for i in day))
#%%
print("This is the type of objects in flow.")
print("This is the ints.")
print(sum(isinstance(i, int) for i in flow))
print("This is the strs.")
print(sum(isinstance(i, str) for i in flow))
print("This is the floats.")
print(sum(isinstance(i, float) for i in flow))
print("This is the bools.")
print(sum(isinstance(i, bool) for i in flow))
# %%
