# %%
# Tong and Dave's Bonus Points Script
# Description: Assigning bonus points based on how close the individual
#              forecast is to the actual flow value of a randomly selected day.

# Import necessary modules
import numpy as np
import sys
#sys.path.insert(1, '../')
sys.path.append('../../evaluation_scripts')
import pandas as pd
from dataretrieval import nwis
from datetime import datetime
import eval_functions as ef

# Set up initial variables
file = 'weekly_streamflow.csv'  # File containing weekly streamflow data
forecast_week = 13  # Evaluation week
station_id = '09506000'  # USGS station id for Camp Verde

# Calculate start and end dates for the forecast week
week_date = ef.weekDates(forecast_week)
start_formatted = week_date[2]
stop_formatted = week_date[3]

# Retrieve a DataFrame of streamflow data for the specified week
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_formatted, end=stop_formatted,
                          parameterCd='00060')

# Select a random day from the retrieved data
random_day = np.random.randint(0, len(obs_day))  # index of random date
random_date = obs_day.index[random_day]  # date of the random day

# Retrieve the flow data for that specific day
flow = obs_day.iloc[random_day]

print(flow)

# Listing everyone's first names
first_names = ef.getFirstNames()
print('Everyone:', first_names)

# Listing everyone who already attained points this week
points = ['Dave', 'Claire', 'Lauren', 'Jessica', 'Jessi']
print('Those who already attained points:', points)
print()

# Listing everyone who did not attain points yet this week
no_points = [name for name in first_names if name not in points]
print('Those who have not attained points yet:', no_points)

# Read in the forecast results for this week
fcst_results = pd.read_csv('../../weekly_results/forecast_week13'
                           '_results.csv', index_col='name')

# Grab out just the people who are not receiving points already
no_points_results = fcst_results.loc[no_points]

# Calculate the average of the 1 and 2 week forecasts
# and calculate the difference between the average and the observed flow
# for the random day selected
fcst_avg = ((no_points_results['1week_forecast'] +
             no_points_results['2week_forecast'])/2)
fcst_diff = abs(fcst_avg - flow[0]).sort_values(ascending=True)

# Choose the top 3 differences to get bonus points
bonus_names = fcst_diff.iloc[0:3,].index

print("People Getting bonus points:", bonus_names)

# Write out the bonus points
ef.write_bonus(bonus_names, first_names, forecast_week)