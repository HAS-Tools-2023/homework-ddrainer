# %%
# Using old code from last week...b/c it works.

# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter

# %%
# Set the file name & path and read data
filename = '../../../data/streamflow_week8.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../../data/streamflow_week8.txt'

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], 
        parse_dates=['datetime'])


# %%
# Set datetime as the index
data = data.set_index('datetime')

# %%
# Calculate Monthly Avg Flow for 2023

monthly_avg = data['flow'].resample('M').max()
monthly_avg = pd.DataFrame(monthly_avg)
monthly_avg_2023 = monthly_avg[monthly_avg.index.year == 2023]

fig, ax = plt.subplots()
ax.plot(monthly_avg_2023['flow'], color='r', label='Monthly Avg')
ax.set(title="Monthly Avg Flow", xlabel="Date",
       ylabel="Flow [cfs]", yscale='log')
plt.xticks(rotation=45)
plt.grid()
plt.legend()

# %%
# Get Weekly Mean Flow for Oct

# Set variables
year = 2020
month = 10

# Work some python magic--calculate min, max, mean for weeks in Oct
wmax_flow = data['flow'].resample('W').max()
wmin_flow = data['flow'].resample('W').min()
wmean_flow =data['flow'].resample('W').mean()

oct_wmax = wmax_flow[wmax_flow.index.month == month]
oct_wmin = wmin_flow[wmin_flow.index.month == month]
oct_wmean = wmean_flow[wmean_flow.index.month == month]

oct_recent_max = oct_wmax[oct_wmax.index.year >= year]
oct_recent_min = oct_wmin[oct_wmin.index.year >= year]
oct_recent_avg = oct_wmean[oct_wmean.index.year >= year]

#oct_recent_max.reset_index()
oct_recent_max = pd.DataFrame(oct_recent_max)
oct_recent_min = pd.DataFrame(oct_recent_min)
oct_recent_avg = pd.DataFrame(oct_recent_avg)

oct_wmean = pd.DataFrame(oct_wmean)
oct_wmax = pd.DataFrame(oct_wmax)
oct_wmin = pd.DataFrame(oct_wmin)

# Set variables
year = 2020
month = 11

# Work some python magic--calculate min, max, mean for weeks in Oct
wmax_flow = data['flow'].resample('W').max()
wmin_flow = data['flow'].resample('W').min()
wmean_flow =data['flow'].resample('W').mean()

nov_wmax = wmax_flow[wmax_flow.index.month == month]
nov_wmin = wmin_flow[wmin_flow.index.month == month]
nov_wmean = wmean_flow[wmean_flow.index.month == month]

nov_recent_max = nov_wmax[nov_wmax.index.year >= year]
nov_recent_min = nov_wmin[nov_wmin.index.year >= year]
nov_recent_avg = nov_wmean[nov_wmean.index.year >= year]

#oct_recent_max.reset_index()
nov_recent_max = pd.DataFrame(nov_recent_max)
nov_recent_min = pd.DataFrame(nov_recent_min)
nov_recent_avg = pd.DataFrame(nov_recent_avg)

nov_wmean = pd.DataFrame(nov_wmean)
nov_wmax = pd.DataFrame(nov_wmax)
nov_wmin = pd.DataFrame(nov_wmin)

# %%
# Plot Oct vs Nov Data

# Data for the first subplot
x_values_subplot1 = oct_recent_max.index.day
x_values_subplot2 = nov_recent_max.index.day

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)  # 1 row, 2 columns
ax1.plot(oct_recent_max['flow'], color='r', label='Weekly Max')
ax1.plot(oct_recent_min['flow'], color='b', label='Weekly Min')
ax1.plot(oct_recent_avg['flow'], color='k', label='Weekly Avg')
ax1.set(title="Oct Weekly Flow Since 2020", xlabel="Date",
       ylabel="Flow [cfs]", ylim=(0,300))
ax1.grid(True)
ax1.set_xticklabels(x_values_subplot1, rotation=45)
ax1.legend()

ax2.plot(nov_recent_max['flow'], color='orange', label='Weekly Max')
ax2.plot(nov_recent_min['flow'], color='purple', label='Weekly Min')
ax2.plot(nov_recent_avg['flow'], color='green', label='Weekly Avg')
ax2.set(title="Nov Weekly Flow Since 2020", xlabel="Date",
       ylabel="Flow [cfs]")
ax2.grid(True)
ax2.set_xticklabels(x_values_subplot2, rotation=45)
ax2.legend()

# %%
# Get October Data Based on Timeseries and Make Forecasts

####################
# Get Weekly Data
monthly_data = data['2023-09-25':'2023-10-22']
last_week = data['2023-10-15':'2023-10-21']
last_3weeks = data['2023-10-01':'2023-10-21']
oct_means = oct_wmean['flow'].mean()
nov_means = nov_wmean['flow'].mean()

# Calculate Avgs
last_week_avg = last_week['flow'].mean()
last_3weeks_avg = last_3weeks['flow'].mean()

# Make a Forecast
week1_fcst = int(oct_means - (monthly_data.loc['2023-10-21','flow']) + last_week_avg*0.61)
week2_fcst = int(nov_means - (monthly_data.loc['2023-10-21','flow']) + last_3weeks_avg*0.15)

# Plot Data with Avg
fix, ax = plt.subplots()
ax.plot(last_3weeks['flow'], color='orange', label='Observed Flow')
ax.plot(wmean_flow['2023-09-25':'2023-10-22'], color='gray', label='Weekly Mean')
ax.plot(hline=last_week_avg)
ax.plot(hline=last_3weeks_avg)
ax.plot(hline=week1_fcst)
ax.plot(hline=week2_fcst)

# Set limits for horizontal line for avgs
x_min, x_max = ax.get_xlim()
horizontal_value = last_week_avg
horizontal_value2 = last_3weeks_avg
horizontal_value3 = week1_fcst
horizontal_value4 = week2_fcst

# Plot horizontal Line Avg
ax.hlines(horizontal_value, x_min, x_max, color='red', linestyle='--', linewidth=2)
ax.text(x_max, horizontal_value, 'Last Week Avg', va='center', ha='left', color='red')

ax.hlines(horizontal_value2, x_min, x_max, color='purple', linestyle='--', linewidth=2)
ax.text(x_max, horizontal_value2, '3-Week Avg', va='center', ha='left', color='purple')

ax.hlines(horizontal_value3, x_min, x_max, color='green', linestyle='dotted', linewidth=2)
ax.text(x_max, horizontal_value3, '1-Week Fcst', va='center', ha='left', color='green')

ax.hlines(horizontal_value4, x_min, x_max, color='blue', linestyle='dotted', linewidth=2)
ax.text(x_max, horizontal_value4, '2-Week Fcst', va='center', ha='left', color='blue')

# Set Graph Attributes
ax.set(title="October Flow & Forecasts", xlabel="Date", ylabel="Flow[cfs]")
plt.xticks(rotation=45)
plt.grid()
plt.legend(loc='lower right')

# Print My Forecast and a Message
print("Dave's week 1 forecast is ", week1_fcst, 'cfs. Thank you for doing my work for me!')
print("Dave's week 2 forecast is ", week2_fcst, "cfs. You're great at this, I should pay you!")

# %%
