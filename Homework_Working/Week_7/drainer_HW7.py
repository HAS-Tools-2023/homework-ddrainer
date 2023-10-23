# Starter code from Week 6 using for Week 7
# %%
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
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Assignment 7 Work

# set day variables
start_day = 22
end_day = 28

# Select specific rows for October based on above variables
selected_rows = data.loc[(data['month'] == 10) & (data['day'] <= end_day) & (data['day'] >= start_day)]

# Compute some stuff...
avg_oct_weekly_flow = selected_rows.groupby(['year']).agg({'flow': 'mean'})
max_oct_weekly_flow = selected_rows.groupby(['year']).agg({'flow': 'max'})
min_oct_weekly_flow = selected_rows.groupby(['year']).agg({'flow': 'min'})
median_oct_weekly_flow = selected_rows.groupby(['year']).agg({'flow': 'median'})

# %%
# Bar Graph 

fig, ax = plt.subplots()
ax.bar(avg_oct_weekly_flow.index, avg_oct_weekly_flow['flow'], color='green')
ax.set_xlabel('Years')
ax.set_ylabel('Streamflow in cfs')
ax.set_title('Avg Streamflow for Week of 22-28 Oct')

fig, ax = plt.subplots()
ax.bar(max_oct_weekly_flow.index, max_oct_weekly_flow['flow'], color)
ax.set_xlabel('Years')
ax.set_ylabel('Streamflow in cfs')
ax.set_title('Max Streamflow for Week of 22-28 Oct')

# Scatter Plot
fig, ax = plt.subplots()
ax.scatter(avg_oct_weekly_flow.index, avg_oct_weekly_flow['flow'])

# %%
# Plot #1: Line Plot
ax = plt.axes()

ax.plot(avg_oct_weekly_flow, linewidth=3, linestyle='dashed', color='g')
ax.set_xlabel('Year')
ax.set_ylabel('Flow (cfs)')
ax.grid('r')
ax.set_facecolor('lightblue')
ax.set_title('Avg Flow 22-28 Oct from 1989-2022')

# %%
## Plot #2: Scatter Plot
plt.style.use('bmh')
ax=selected_rows.plot.scatter(x='year', y='flow',
                     c='day', colormap='cividis', marker='^')
ax.set_title("Weekly 22-28 Oct Flow from 1989-2022")
ax.set_facecolor('lightblue')

# %%
## Plot #3: Multiple Line Plots
plt.style.use('ggplot')
ax = plt.axes()
ax.plot(max_oct_weekly_flow, linestyle='-', color='r', label='Max')
ax.plot(min_oct_weekly_flow, linestyle='-.', color='b', label='Max')
ax.plot(median_oct_weekly_flow, linestyle='dashed', color='k', label='Min')
ax.set_xlabel('year')
ax.set_ylabel('Flow(cfs)')
ax.set_title('Flow Statistics for 22-28 Oct from 1989-2022')
ax.set_facecolor("chartreuse")
ax.legend()

# %%
## Plot #4: Histogram
start_day = 22
end_day = 28

# Select specific rows for days of the month based on above variables
selected_rows = data.loc[(data['month'] == 10) & (data['day'] <= end_day) & (data['day'] >= start_day)]

plt.hist(selected_rows["flow"], bins=100, color='blue', edgecolor='green')
plt.title('Frequency of Streamflow for Week of 22-28 Oct')
plt.ylabel('Count')
plt.xlabel('Streamflow Bins in cfs')
plt.xticks(range(0, 1100, 50), rotation=45)

# %%
## Plot #5: Subplots

fig, axs = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
fig.suptitle('Weekly Flow Statistics for 22-28 Oct All Years', fontsize=20)

axs[0,0].plot(avg_oct_weekly_flow, linewidth=1, linestyle='-', color='g')
axs[0,0].set_title('Average')
axs[0,0].set_facecolor('lightblue')

axs[0,1].plot(max_oct_weekly_flow, linewidth=1, linestyle='dashed', color='r')
axs[0,1].set_title('Max')
axs[0,1].set_facecolor('lightgreen')

axs[1,0].plot(min_oct_weekly_flow, linewidth=1, linestyle='dotted', color='b')
axs[1,0].set_title('Min')
axs[1,0].set_facecolor('lightpink')

axs[1,1].plot(median_oct_weekly_flow, linewidth=1, linestyle='-.', color='k')
axs[1,1].set_title('Median')
axs[1,1].set_facecolor('orange')

fig.supxlabel('Years')
fig.supylabel('Streamflow in cfs')


# %%
