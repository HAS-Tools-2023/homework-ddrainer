# %%
# EXERCISE 1:
# Write a function that takes the month as input and returns the number of non-leap year days in that month as output

def get_days(month):
    if month == [1 or 3 or 5 or 7 or 8 or 10 or 12]:
        answer = 31
        return(answer)
    elif month == [4 or 6 or 9 or 11]:
        answer = 30
        return(answer)
    else:
        answer = 28
        return(answer)

#answer
def days_in_month(month):
    if month==2:
        return(28)
    elif month==4 or month==6 or month==9 or month ==11:
        return(30)
    elif month>= and month<=12:
        return(31)
    else:
        print('Not a valid month please enter an integer between 1 and 12')

get_days(3)

#%%
# EXERCISE 2:
# Write a function that takes takes your streamflow dataframe and one other user defined variable as an input and returns some metric of interest

# Example

# Import the modules we will use
import os
import pandas as pd
import numpy as np

# %%
# Set the file name & path and read data
filename = '../../data/streamflow_week8.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week8.txt'

# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=31,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'])

data = data.set_index('datetime')

annual_mean_all = data['flow'].resample('Y').mean()
annual_mean_all = pd.DataFrame(annual_mean_all)

def yearly_max(data, year):
    get_annual_avg = annual_mean_all[annual_mean_all.index.year == year]
    return(print('The annual average for', year, 'is ', get_annual_avg))
    
yearly_max(data, 2020)

# Answer
# Be very generalized, must use 
# For homework, use something I already used and build a function off of it
def monthly_max(dataframe, month, year):
    monthly_vals = dataframe[(dataframe.index.month == month) & 
                             (dataframe.index.year == year)]
    maxval=np.max(monthly_vals['flow'])
    print('Calculating max for month:', month, 'year', year)
    return(maxval)

monthly_max(dataframe=data, month=5, year=2019) #specify each argument to input them out of order
monthly_max(data, 2, 2021) #put them in the right order, don't need to specify the argument

#%%
## Exercise 3:
# Write a function to create one of your figures from the previous homework
