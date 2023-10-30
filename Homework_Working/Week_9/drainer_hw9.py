# %%
# Using code from HW8, cleaned up using linter.

# Import the modules we will use
import os
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name, path, read data, and set index
filename = '../../data/streamflow_week9.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week9.txt'

# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=31,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

# Set datetime as the index
data = data.set_index('datetime')

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
# Test Calculate

# Monthly Tests
# Set variables


time_period = 'M'
start_date = '2023-01-01'
end_date = '2023-10-28'

calc_mean(data, time_period, 'flow', start_date, end_date)
calc_max(data, time_period, 'flow', start_date, end_date)
calc_min(data, time_period, 'flow', start_date, end_date)

# Weekly Tests
# Set variables

time_period = 'W'

calc_mean(data, time_period, 'flow', start_date, end_date)
calc_max(data, time_period, 'flow', start_date, end_date)
calc_min(data, time_period, 'flow', start_date, end_date)

# %%
# Plot Monthly Average flow for selected time

mean_period = 'M'  # Set period to calculate mean for

mean_plot_data_2023 = calc_mean(data, mean_period, 'flow', '2023-01-01',
                                '2023-10-28')
mean_plot_data_2022 = calc_mean(data, mean_period, 'flow', '2022-01-01',
                                '2022-10-31')
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
       ylabel="Flow [cfs]")  # Set plot attributes
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
                                '2022-10-31')
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
       ylabel="Flow [cfs]")  # Set plot attributes
ax.set_facecolor('gray')  # Set the background color
plt.xticks(rotation=45)  # Rotate the x-axis labels 45°
plt.grid()  # Turn on the grid
plt.legend()  # Plot the legend

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
monthly_data = data['2023-10-01':'2023-10-28']
last_week = data['2023-10-22':'2023-10-28']
last_4weeks = data['2023-10-01':'2023-10-28']
oct_means = oct_wmean['flow'].mean()
nov_means = nov_wmean['flow'].mean()

# Calculate Avgs
last_week_avg = last_week['flow'].mean()
last_4weeks_avg = last_4weeks['flow'].mean()

# Make a Forecast
week1_fcst = int(oct_means - (monthly_data.loc['2023-10-28','flow']) + last_week_avg*0.80)
week2_fcst = int(nov_means - (monthly_data.loc['2023-10-28','flow']) + last_4weeks_avg*0.20)

# Plot Data with Avg
fix, ax = plt.subplots()
ax.plot(last_4weeks['flow'], color='orange', label='Observed Flow')
ax.plot(wmean_flow['2023-10-01':'2023-10-29'], color='gray', label='Weekly Mean')
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
ax.hlines(horizontal_value, x_min, x_max, color='red', linestyle='--', linewidth=2)
ax.text(x_max, horizontal_value, 'Last Week Avg', va='center', ha='left', color='red')

ax.hlines(horizontal_value2, x_min, x_max, color='purple', linestyle='--', linewidth=2)
ax.text(x_max, horizontal_value2, '3-Week Avg', va='center', ha='left', color='purple')

ax.hlines(horizontal_value3, x_min, x_max, color='green', linestyle='dotted', linewidth=2)
ax.text(x_max, horizontal_value3, '1-Week Fcst', va='center', ha='left', color='green')

ax.hlines(horizontal_value4, x_min, x_max, color='blue', linestyle='dotted', linewidth=2)
ax.text(x_max, horizontal_value4, '2-Week Fcst', va='center', ha='left', color='blue')

# Set Graph Attributes
ax.set(title="October Observed Flow", xlabel="Date", ylabel="Flow[cfs]")
plt.xticks(rotation=45)
plt.grid()
plt.legend(loc='lower right')


# Print My Forecast and a Message
print('My week 1 forecast is ', week1_fcst, 'cfs. Thank you for doing my work for me!')
print('My week 2 forecast is ', week2_fcst, "cfs. You're great at this, I should pay you!")

# %%