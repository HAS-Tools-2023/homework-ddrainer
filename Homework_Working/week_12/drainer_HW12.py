# %%
# Import packages

import matplotlib.pyplot as plt
import pandas as pd
import json
import urllib.request as req
import urllib

# %%
# Define functions
"""Pull data from a Rest API for USGS Streamflow.

Keyword arguments:
stationID -- specific to the gauge
start_date -- first day of data you want
end_date -- last day of data you want
"""


def pull_data(stationID, start_date, end_date):
    url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no="+ stationID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no', 'datetime',
                                                   'flow', 'code'],parse_dates=['datetime'],
                                                   index_col=['datetime'])
    return data


"""Calculate mean streamflow for a period.

Keyword arguments:
dataframe -- should be a datafram of streamflow data
period -- either W, M, or D
data_col -- the column of the flow data in the dataframe
start_date -- beginning date for mean calculation
end_date -- end date for mean calculation
"""

def calc_mean(dataframe, period, data_col, start_date, end_date):
    df = dataframe[start_date:end_date]  # Filter data based on dates input
    mean_flow = df.resample(period).mean(data_col)  # Calculate from input
    return mean_flow


# Get data from Rest API for streamflow using function & save variable
site = '09506000'
start = '2018-01-01'
end = '2023-11-19'

data = pull_data(site, start, end)  # save API query to variable

# %%
# Plot Monthly Average flow for selected time to compare to previous years


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
# Plot Weekly Average flow for selected time for better resolution

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
# Get Precipitation Data to look for visual correlation w/streamflow data

my_token = '7ebaa414907445589854ffb4c4059d23'

base_url = 'https://api.synopticdata.com/v2/stations/timeseries'

# Specific arguments for the data that we want
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': my_token}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Request data
response = req.urlopen(fullUrl)

# Read data
responseDict = json.loads(response.read())

# Set variables for dataframe
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

units = responseDict['UNITS']

precip_accum_data_23 = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(dateTime))
data_daily_23 = precip_accum_data_23.resample('D').max()

# Plot accumulated precipitation
plt.plot(data_daily_23, color='purple', label='2023')

plt.xticks(rotation=45)
plt.xlabel('Date'), plt.ylabel('Accum Precip'), plt.title('Daily Max\n Accumulated Precip')
plt.grid()
plt.legend()

# %%
# Get preciptation for 2021 and 2022, last full years for comparison

url = 'https://daymet.ornl.gov/single-pixel/api/data?lat=34.56368003515758&lon=-111.86310056727073&vars=prcp&years=&start=2022-01-01&end=2022-12-31&format=json'
response = req.urlopen(url)

# Read json and designate variables
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

# make a dataframe from the data
precip_data_22 = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})

url = 'https://daymet.ornl.gov/single-pixel/api/data?lat=34.56368003515758&lon=-111.86310056727073&vars=prcp&years=&start=2021-01-01&end=2021-12-31&format=json'
response = req.urlopen(url)

# Read json and designate variables
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

# make a dataframe from the data
precip_data_21 = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})

# Plot the data on the same axes
fig, ax = plt.subplots()
ax.bar(precip_data_21['yearday'], precip_data_21['precip'], label='2021',
       color='orange', width=4, alpha=0.9)
ax.bar(precip_data_22['yearday'], precip_data_22['precip'], label='2022',
       color='green', width=4, alpha=0.5)

ax.set(title="Daily Precipitation", xlabel="Day of the Year",
       ylabel="mm/day")

ax.legend()
ax.grid()

# %%
# Plot Data and Make Forecasts based on a good "SWAG"

# Set dates
monthly_start = '2023-10-19'
monthly_end = '2023-11-19'
weekly_start = '2023-11-12'
weekly_end = '2023-11-19'

####################
# Get Weekly Data of interest
monthly_data = data[monthly_start:monthly_end]
last_week = data[weekly_start:weekly_end]
weekly_mean = calc_mean(monthly_data, 'W', 'flow', monthly_start, monthly_end)
weekly_mean.loc[weekly_end]['flow']

# Calculate Avgs for last week and last 4 weeks
last_week_avg = last_week['flow'].mean()
monthly_avg = monthly_data['flow'].mean()

# Make a Forecast based on intuition
week1_fcst = int((weekly_mean.loc[weekly_end]['flow']) + \
    abs(last_week_avg-monthly_avg)*.75)
week2_fcst = int((monthly_data.loc[weekly_end, 'flow']) + \
    abs(last_week_avg-monthly_avg)*.75)

# Plot Data with Avg comapred to observed flow
fig, ax = plt.subplots()
ax.plot(monthly_data['flow'], color='orange',
        label='Observed Flow')
ax.plot(weekly_mean['flow'], color='gray',
        label='Weekly Mean')
ax.plot(hline=last_week_avg)
ax.plot(hline=monthly_avg)
ax.plot(hline=week1_fcst)
ax.plot(hline=week2_fcst)

# Set limits for horizontal line for avgs
x_min, x_max = ax.get_xlim()
horizontal_value = last_week_avg
horizontal_value2 = monthly_avg
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
