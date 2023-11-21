# %%
# Import packages

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import dataretrieval.nwis as nwis
import json
import urllib.request as req
import urllib
from scipy import stats
from sklearn.linear_model import LinearRegression
from datetime import date

# %%
# Get data from Rest API using function

def pull_data(stationID, start_date, end_date):
    url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no="+ stationID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no', 'datetime',
                                                   'flow', 'code'],parse_dates=['datetime'],
                                                   index_col=['datetime'])
    return data

site = '09506000'
start = '2018-01-01'
end = '2023-11-19'

data = pull_data(site, start, end)  # save API query to variable

# %%
# Define Functions
# Mean Flow Function
# Inputs required:
#       dataframe, period (Weekly = 'W', Monthly = 'M', Yearly = 'Y'),
#       data_col, start_date, and end_date for calc


def calc_mean(dataframe, period, data_col, start_date, end_date):
    df = dataframe[start_date:end_date]  # Filter data based on dates input
    mean_flow = df.resample(period).mean(data_col)  # Calculate from input
    return mean_flow

# Max Flow Function
# Inputs required:
#       dataframe, period (Weekly = 'W', Monthly = 'M', Yearly = 'Y'),
#       data_col, start_date, and end_date for calc


def calc_max(dataframe, period, data_col, start_date, end_date):
    df = dataframe[start_date:end_date]  # Filter data based on dates input
    max_flow = df.resample(period).max(data_col)  # Calculate from input
    return max_flow

# Min Flow Function
# Inputs required:
#       dataframe, period (Weekly = 'W', Monthly = 'M', Yearly = 'Y'),
#       data_col, start_date, and end_date for calc


def calc_min(dataframe, period, data_col, start_date, end_date):
    df = dataframe[start_date:end_date]  # Filter data based on dates input
    min_flow = df.resample(period).max(data_col)  # Calculate from input
    return min_flow

# %%
# Plot Monthly Average flow for selected time

mean_period = 'M'  # Set period to calculate mean for

mean_plot_data_2023 = calc_mean(data, mean_period, 'flow', '2023-01-01',
                                '2023-11-11')
mean_plot_data_2022 = calc_mean(data, mean_period, 'flow', '2022-01-01',
                                '2022-12-31')
mean_plot_data_2021 = calc_mean(data, mean_period, 'flow', '2021-01-01',
                                '2021-12-31')
mean_plot_data_2020 = calc_mean(data, mean_period, 'flow', '2020-01-01',
                                '2020-12-31')
mean_plot_data_2019 = calc_mean(data, mean_period, 'flow', '2019-01-01',
                                '2019-12-31')
mean_plot_data_2018 = calc_mean(data, mean_period, 'flow', '2018-01-01',
                                '2018-12-31')

# Plot all monthly averages from 2018-2023

fig, ax = plt.subplots()
ax.plot(mean_plot_data_2023['flow'], color='black', label='2023')
ax.plot(mean_plot_data_2022['flow'], color='green', label='2022')
ax.plot(mean_plot_data_2021['flow'], color='yellow', label='2021')
ax.plot(mean_plot_data_2020['flow'], color='red', label='2020')
ax.plot(mean_plot_data_2019['flow'], color='purple', label='2019')
ax.plot(mean_plot_data_2018['flow'], color='orange', label='2018')
ax.set(title="Monthly Avg Flow 2018-2023", xlabel="Date",
       ylabel="Flow [cfs]", yscale='log')  # Set plot attributes
ax.set_facecolor('gray')  # Set the background color
plt.xticks(rotation=45)  # Rotate the x-axis labels 45°
plt.grid()  # Turn on the grid
plt.legend()  # Plot the legend

# %%
# Plot Weekly Average flow for selected time

mean_period = 'W'  # Set period to calculate mean for

mean_plot_data_2023 = calc_mean(data, mean_period, 'flow', '2023-01-01',
                                '2023-10-28')
mean_plot_data_2022 = calc_mean(data, mean_period, 'flow', '2022-01-01',
                                '2022-12-31')
mean_plot_data_2021 = calc_mean(data, mean_period, 'flow', '2021-01-01',
                                '2021-12-31')
mean_plot_data_2020 = calc_mean(data, mean_period, 'flow', '2020-01-01',
                                '2020-12-31')
mean_plot_data_2019 = calc_mean(data, mean_period, 'flow', '2019-01-01',
                                '2019-12-31')
mean_plot_data_2018 = calc_mean(data, mean_period, 'flow', '2018-01-01',
                                '2018-12-31')

# Plot all weekly averages from 2018-2023

fig, ax = plt.subplots()
ax.plot(mean_plot_data_2023['flow'], color='black', label='2023')
ax.plot(mean_plot_data_2022['flow'], color='green', label='2022')
ax.plot(mean_plot_data_2021['flow'], color='yellow', label='2021')
ax.plot(mean_plot_data_2020['flow'], color='red', label='2020')
ax.plot(mean_plot_data_2019['flow'], color='purple', label='2019')
ax.plot(mean_plot_data_2018['flow'], color='orange', label='2018')
ax.set(title="Weekly Avg Flow 2018-2023", xlabel="Date",
       ylabel="Flow [cfs]", yscale='log')  # Set plot attributes
ax.set_facecolor('gray')  # Set the background color
plt.xticks(rotation=45)  # Rotate the x-axis labels 45°
plt.grid()  # Turn on the grid
plt.legend()  # Plot the legend

# %%
# Create a forecast based on observed data compared to mean

wk_start = '2023-05-01'
wk_end = '2023-11-19'

weekly_data = data[wk_start:wk_end]

weekly_mean = calc_mean(weekly_data, 'W', 'flow', wk_start, wk_end)

fig, ax = plt.subplots()
ax.plot(weekly_mean['flow'], color='black', label='Weekly Mean Flow')


# %%
# Get October Data Based on Timeseries and Make Forecasts

latest_ob = '2023-11-19'

####################
# Get Weekly Data of interest
#monthly_data = data['2023-10-19':'2023-11-19']
last_week = data['2023-11-12':'2023-11-11']
last_month = data['2023-10-18':'2023-11-19']

# Calculate Avgs for last week and last 4 weeks
last_week_avg = last_week['flow'].mean()
last_month_avg = last_month['flow'].mean()

# Make a Forecast based on intuition
week1_fcst = int(last_month_avg - (last_month.loc[latest_ob, 'flow'] + last_week_avg*0.75)
week2_fcst = int(nov_means - (last_month.loc[latest_ob, 'flow']) +
                 last_month_avg)

# Plot Data with Avg comapred to observed flow
fix, ax = plt.subplots()
ax.plot(monthly_data['flow'], color='orange',
        label='Observed Flow')
ax.plot(wmean_flow['2023-10-01':'2023-11-12'], color='gray',
        label='Weekly Mean')
ax.plot(hline=last_week_avg)
ax.plot(hline=last_4weeks_avg)
ax.plot(hline=week1_fcst)
ax.plot(hline=week2_fcst)

# Set limits for horizontal line for avgs
x_min, x_max = ax.get_xlim()
horizontal_value = last_week_avg
horizontal_value2 = last_4weeks_avg
horizontal_value3 = week1_fcst
horizontal_value4 = week2_fcst

# Plot horizontal Line Avg
ax.hlines(horizontal_value, x_min, x_max, color='red', linestyle='--',
          linewidth=2)
ax.text(x_max, horizontal_value, 'Last Week Avg', va='center', ha='left',
        color='red')

ax.hlines(horizontal_value2, x_min, x_max, color='purple', linestyle='--',
          linewidth=2)
ax.text(x_max, horizontal_value2, '4-Week Avg', va='center', ha='left',
        color='purple')

ax.hlines(horizontal_value3, x_min, x_max, color='green', linestyle='dotted',
          linewidth=2)
ax.text(x_max, horizontal_value3, '1-Week Fcst', va='center', ha='left',
        color='green')

ax.hlines(horizontal_value4, x_min, x_max, color='blue', linestyle='dotted',
          linewidth=2)
ax.text(x_max, horizontal_value4, '2-Week Fcst', va='center', ha='left',
        color='blue')

# Set Graph Attributes
ax.set(title="Observed Flow and Forecast", xlabel="Date", ylabel="Flow[cfs]")
plt.xticks(rotation=45)
plt.grid()
plt.legend(loc='lower right')


# Print My Forecast and a Message
print('My week 1 forecast is ', week1_fcst, 'cfs.')
print('My week 2 forecast is ', week2_fcst, 'cfs.')

# %%
