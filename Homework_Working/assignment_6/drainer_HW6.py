# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = '../../data/streamflow_week6.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week6.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


# %%
# Assignment 6 Question Answers

print(data)
print(data.describe())
print('Here is a list of all the columns:', data.columns.to_list())

print("The last 5 rows, showing highest 5 flows: ", data.sort_values(['flow']).tail())
print("The first 5 rows, showing the lowest 5 flows: ", data.sort_values(['flow']).head())

monthly_stats = data.groupby(pd.Grouper('month'))

monthly_flow_stats = monthly_stats['flow'].describe()
print(monthly_flow_stats)

# %%
# Get all rows within 10% of Week 1 Forecast only for October

week1_fcst = 80
specific_value = data['flow'].iloc[0]

min_value = week1_fcst - (0.10 * specific_value)
max_value = week1_fcst + (0.10 * specific_value)

filtered_flow = data[(data['flow'] >= min_value) & (data['flow'] <= max_value) & (data['month'] == 10)]

print(filtered_flow)

# %%
# Get all rows within 5% of Week 1 Forecast only for October

week1_fcst = 80
specific_value = data['flow'].iloc[0]

min_value = week1_fcst - (0.05 * specific_value)
max_value = week1_fcst + (0.05 * specific_value)

filtered_flow = data[(data['flow'] >= min_value) & (data['flow'] <= max_value) & (data['month'] == 10)]

print(filtered_flow)

# %%
# Get all rows within 1% of Week 1 Forecast only for October

week1_fcst = 80
specific_value = data['flow'].iloc[0]

min_value = week1_fcst - (0.01 * specific_value)
max_value = week1_fcst + (0.01 * specific_value)

filtered_flow = data[(data['flow'] >= min_value) & (data['flow'] <= max_value) & (data['month'] == 10)]

print(filtered_flow)

# %%
# Warm up exercises: 
# Pandas Exercise One

import numpy as np
import pandas as pd

data = np.ones((7,3))
data_frame = pd.DataFrame(data, columns=['data1', 'data2', 'data3'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(data_frame)
# %%
# Change all rows with vowels to 3

first_df = data_frame # make a copy to a new dataframe

first_df.loc[['a','e']] = 3 # set row a and e to all 3

print(first_df)

# %%
# Multiply first 4 rows by 7

first_df.iloc[:4] = first_df.iloc[:4] * 7
first_df.loc[['a','b','c','d']] * 7

print(first_df)

# %%
# Create a checkerboard pattern of 1s and 0s using loc

first_df.loc[['a','c','e','g'], ['data1','data3']] = 0 # Set every other row in column data1 and data3 to 0
first_df.loc[['b','d','f'], ['data2']] = 0 # Set every other row in column data2 to 0

first_df.loc[['a','c','e','g'], ['data2']] = 1 # Set every other row in column data2 to 1
first_df.loc[['b','d','f'], ['data1','data3']] = 1 # Set every other row in columns data1 and data3 to 1

print(first_df)


# %%
# Create a checkerboard pattern of 1s and 0s using iloc

first_df.iloc[1::2, ::2] = 1 # Set odd rows, even columns to 1
first_df.iloc[::2, 1::2] = 1 # Set even rows, odd columns to 1
first_df.iloc[::2, ::2] = 0 # Set even rows, even columns to 0
first_df.iloc[1::2, 1::2] = 0 # Set odd rows, odd columsn to 0

print(first_df)


#%%
# Pandas Exercise Two
# Fill the NA values with 999

import pandas as pd
import numpy as np

data_frame = pd.DataFrame([[1, np.nan, 2],
                          [2, 3, 5],
                          [np.nan, 4, 6]])

print(data_frame)

fixed_df = data_frame.fillna(999)

print(fixed_df)

# %%
# 1. How do you see a quick summary of what is in `data`?

print('These are the summary statistics:')
print(data.describe())

print('This is the information block:')
print(data.info())


# %%
# 2. How do you get a listing of the columns in `data`?

print('Here is a list of all the columns:', data.columns.to_list())

# %%
# 3. How do you select the streamflow column in `data`?

data.loc[:,'flow']

#%%
# 4. How do you plot the streamflow in `data`?

data.plot(x='year', y='flow', kind='scatter')

# Customize the plot (optional)
plt.title('Streamflow')
plt.xlabel('Year')
plt.ylabel('Flow (cfs)')

plt.show()

#%%
# 5. How do you get the last streamflow value from `data`?

print("The last streamflow value is: ", data.iloc[-1,3], "cfs")

#%%
# 6. What is the mean streamflow value for entire period?

mean_flow = data['flow'].mean()

print("The mean streamflow for the period is: ", mean_flow, "cfs")

#%%
# 7. What is the maximum value for the entire period?

max_flow = data['flow'].max()

print("The max value for the period is: ", max_flow, "cfs")

#%%
# 8. How do you find the maximum streamflow value for each year?

yearly_max = data.groupby(['year']).agg({'flow': 'max'})

print("The max flow for each year is as follows: ", 
      yearly_max)

# %%
# Plot Max Yearly Flow
yearly_max.plot(kind='line')

plt.title('Yearly Max Flow')
plt.xlabel('Year')
plt.ylabel('Flow (cfs)')
plt.xticks(rotation=45)

plt.show()

# %%
# Assignment 6 Forecast Work

avg_monthly_flow = data.groupby(['month']).agg({'flow': 'mean'})
max_monthly_flow = data.groupby(['month']).agg({'flow': 'max'})
min_monthly_flow = data.groupby(['month']).agg({'flow': 'min'})

print("Average monthly flow is: ", avg_monthly_flow)
print("Max monthly flow is: ", max_monthly_flow)
print("Min monthly flow is: ", min_monthly_flow)


# %%
#avg_monthly_flow.plot(kind='line')
avg_monthly_flow2 = data.groupby(['month','year']).agg({'flow': 'mean'})

print(avg_monthly_flow2)

# %%

# Select specific rows for October where day < = 15
selected_rows = data.loc[(data['month'] == 10) & (data['day'] <= 15)]

avg_oct_flow_first_half = selected_rows.groupby(['year']).agg({'flow': 'mean'})

print(avg_oct_flow_first_half)

last_5_Oct = avg_oct_flow_first_half.tail() # get last 5 years of Oct avgs
print(last_5_Oct)

last_5_Oct_avg1 = last_5_Oct['flow'].mean() # average last 5 Oct avg flow
print(last_5_Oct_avg1) # average of last 5 years of Oct flow averages

# Select specific rows for October where day < = 15
selected_rows2 = data.loc[(data['month'] == 10) & (data['day'] >= 16)]

avg_oct_flow_second_half = selected_rows2.groupby(['year']).agg({'flow': 'mean'})

print(avg_oct_flow_second_half)

last_5_Oct2 = avg_oct_flow_second_half.tail() # get last 5 years of Oct avgs for second half of month

print(last_5_Oct2)

last_5_Oct_avg2 = last_5_Oct2['flow'].mean() # average last 5 Oct avg flow for second half of month
print(last_5_Oct_avg2) # average of last 5 years of Oct flow averages for second half

diff_avg_flow = avg_oct_flow_first_half['flow'] - avg_oct_flow_second_half['flow']

print(diff_avg_flow)

avg_oct_flow_first_half.plot(kind='line')

plt.title('Avg Oct Flow 1st Half')
plt.xlabel('Year')
plt.ylabel('Flow (cfs)')
plt.xticks(rotation=45)

avg_oct_flow_second_half.plot(kind='line')

plt.title('Avg Oct Flow 2nd Half')
plt.xlabel('Year')
plt.ylabel('Flow (cfs)')
plt.xticks(rotation=45)

diff_avg_flow.plot(kind='line')

plt.title('Difference in Flow from 1st Half to 2nd Half of Oct')
plt.xlabel('Year')
plt.ylabel('Flow (cfs)')
plt.xticks(rotation=45)

# %%
