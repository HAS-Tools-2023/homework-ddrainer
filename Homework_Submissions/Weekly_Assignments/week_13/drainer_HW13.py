# Name: David Drainer
# Date: 11/27/2023
# Title: Homework 13
# Note that there are 4 instances where the linter doesn't like my
# indentation on functions. I have tried to fix it but it keeps giving
# me errors no matter which way I indent them. I also can't seem to get
# rid of the indent error on line 195.

# %%
# Import packages

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# %%
# User Input Forecast Date for week 1 in YYYY-MM-DD format
# Forecast Date for week 2 will be calculated based on this date

fcst_date = '2023-12-04'

# User Input for USGS site code
site = '09506000'  # Camp Verde

# Define all functions to be used in code


def add_dates(input_date, num_days):
        """
        Add a specified number of days to a given date.

        Parameters:
        input_date (str): The input date in 'YYYY-MM-DD' format.
        num_days (int): The number of days to add.

        Returns:
        str: The resulting date after adding the specified number of days in
        'YYYY-MM-DD' format.
        """
        input_date = datetime.strptime(fcst_date, '%Y-%m-%d')
        output_date = input_date + timedelta(days=num_days)
        return output_date.strftime('%Y-%m-%d')


def sub_dates(input_date, num_days):
        """
        Subtract a specified number of days from a given date.

        Parameters:
        input_date (str): The input date in 'YYYY-MM-DD' format.
        num_days (int): The number of days to subtract.

        Returns:
        str: The resulting date after subtracting the specified number of days
        in 'YYYY-MM-DD' format.
        """
        input_date = datetime.strptime(fcst_date, '%Y-%m-%d')
        output_date = input_date - timedelta(days=num_days)
        return output_date.strftime('%Y-%m-%d')


def pull_data(stationID, start_date, end_date):
        """
        Pulls streamflow data from a Rest API for a specific USGS gauge.

        Parameters:
        stationID (str): The ID of the gauge.
        start_date (str): The start date of the data in 'YYYY-MM-DD' format.
        end_date (str): The end date of the data in 'YYYY-MM-DD' format.

        Returns:
        pandas.DataFrame: The streamflow data for the specified gauge and
        date range.
        """
        url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=" \
               "rdb&site_no=" + stationID + "&referred_module=sw&period=&" \
               "begin_date=" + start_date + "&end_date=" + end_date
        data = pd.read_table(url2, skiprows=30,
                             names=['agency_cd', 'site_no', 'datetime', 'flow',
                                    'code'], parse_dates=['datetime'],
                             index_col=['datetime'])
        return data


def calc_mean(dataframe, period, data_col, start_date, end_date):
        """
        Calculate the mean streamflow for a specified period.

        Parameters:
        dataframe (pandas.DataFrame): The dataframe containing the
        streamflow data.
        period (str): The period for which to calculate the mean (W - weekly,
        M - monthly, D - daily).
        data_col (str): The column name of the flow data in the dataframe.
        start_date (str): The start date of the period in 'YYYY-MM-DD' format.
        end_date (str): The end date of the period in 'YYYY-MM-DD' format.

        Returns:
        pandas.Series: The mean streamflow for the specified period.
        """
        df = dataframe[start_date:end_date]  # Filter data based on dates input
        mean_flow = df.resample(period).mean(data_col)  # Calculate from input
        return mean_flow

# %%
# Run code to get data and make forecasts

# Create relevant dates for forecasting


week2_fcst_date = add_dates(fcst_date, 7)  # 2 week forecast date
monthly_start = sub_dates(fcst_date, 31)  # Monthly start date
monthly_end = sub_dates(fcst_date, 8)  # Monthly end date
weekly_start = sub_dates(fcst_date, 15)  # Weekly start date
weekly_end = sub_dates(fcst_date, 8)  # Weekly end date

# Get last year's worth of data from Rest API for streamflow using
# function & save data to variable 'data'
start = sub_dates(monthly_start, 365)  # Start date for streamflow data
end = weekly_end  # End date for streamflow data

data = pull_data(site, start, end)  # save API query to variable

# %%
# Plot Data and Make Forecasts based on a good "SWAG"

# Get Monthly and Weekly Data of interest
monthly_data = data[monthly_start:monthly_end]
last_week = data[weekly_start:weekly_end]

# Calculate Weekly Mean Flow
weekly_mean = calc_mean(monthly_data, 'W', 'flow', monthly_start, monthly_end)

# Calculate Avgs for last week and last 4 weeks
last_week_avg = int(last_week['flow'].mean())
monthly_avg = int(monthly_data['flow'].mean())

# Make forecasts for week 1 and week 2 based on a good "SWAG";
# I added the most recent flow to the difference between the
# last week avg and the monthly avg, then multiplied by 85% for week 1
# and 90% for week 2. I then rounded the result to the nearest integer.
week1_fcst = int((weekly_mean.iloc[-1]['flow']) +
                 abs(last_week_avg-monthly_avg)*.85)
week2_fcst = int((monthly_data.iloc[-1]['flow']) +
                 abs(last_week_avg-monthly_avg)*.90)

# Plot Data with Avg compared to observed flow
fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(monthly_data['flow'], color='orange',
        label='Observed Flow')  # Daily Observed Flow Curve
ax.plot(weekly_mean['flow'], color='gray',
        label='Weekly Mean')  # Weekly Mean Curve
ax.plot(hline=last_week_avg)  # Last Week Avg Line
ax.plot(hline=monthly_avg)  # 4-Week Avg Line
ax.plot(hline=week1_fcst)  # Week 1 Forecast Line
ax.plot(hline=week2_fcst)  # Week 2 Forecast Line

# Set limits for horizontal line for avgs
x_min, x_max = ax.get_xlim()  # Get x-axis limits
horizontal_value = last_week_avg
horizontal_value2 = monthly_avg
horizontal_value3 = week1_fcst
horizontal_value4 = week2_fcst

# Plot horizontal Lines and Labels
# Last Week Avg Line
ax.hlines(horizontal_value, x_min, x_max, color='red', linestyle='--',
          linewidth=2, label=f'Last WK Avg: {last_week_avg} cfs')
ax.text(x_max, horizontal_value, 'Last Week Avg', va='center', ha='left',
        color='red')

# 4-Week Avg Line
ax.hlines(horizontal_value2, x_min, x_max, color='purple', linestyle='--',
          linewidth=2, label=f'4-WK Avg: {monthly_avg} cfs')
ax.text(x_max, horizontal_value2, '4-Week Avg', va='center', ha='left',
        color='purple')

# Week 1 Forecast Line
ax.hlines(horizontal_value3, x_min, x_max, color='green', linestyle='dotted',
          linewidth=2, label=f'WK 1 Fcst: {week1_fcst} cfs')
ax.text(x_max, horizontal_value3, '1-Week Fcst', va='center', ha='left',
        color='green')

# Week 2 Forecast Line
ax.hlines(horizontal_value4, x_min, x_max, color='blue', linestyle='dotted',
          linewidth=2, label=f'WK 2 Fcst: {week2_fcst} cfs')
ax.text(x_max, horizontal_value4, '2-Week Fcst', va='center', ha='left',
        color='blue')

# Set Graph Attributes
ax.set(title="Observed Flow and Forecasts", xlabel="Date", ylabel="Flow[cfs]")
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.grid()  # Add gridlines
plt.legend(loc='upper left')  # Add legend

# Print Most Recent Observed Flow and Date
print('The most recent observation was on', data.index[-1], 'and the flow was',
        data.iloc[-1]['flow'], 'cfs.')

# Print My Forecast and a Message
print('My week 1 forecast for', fcst_date, 'is', week1_fcst, 'cfs.')
print('My week 2 forecast for', week2_fcst_date, 'is', week2_fcst, 'cfs.')
