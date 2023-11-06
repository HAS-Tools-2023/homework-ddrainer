# %%
# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator

# %%
# Tuesday Exercises

# Exercise 1:
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean
# of every column of the dataframe
# If you have time try doing it with and without
# a for loop (You can either use the function inside
# your for loop or put a for loop inside your function)


def average_columns(my_array):
    """Function to take the mean every column of the
    dataframe using a for loop.

    Keyword arguments:
    my_array -- input array of numbers
    """
    ncol = my_array.shape[1]
    col_mean = np.zeros(5)
    for i in range(ncol):
        col_mean[i] = np.mean(my_array[:, i])
    return (col_mean)


average_columns(data)

# %%
# define a function that can take the mean of a set of nubmers
# and return one value


def take_mean(some_numbers):
    """Function to take the mean of an input of numbers,
    which can be a list of numbers, or an array, or just
    a part of an array

    Keyword arguments:
    some_numbers -- input of numbers or an array
    """
    mean = np.mean(some_numbers)
    return mean

# Examples


print(take_mean([10, 10, 10, 7, 10, 5]))
print(take_mean(data))
print(take_mean(data[1]))
print(take_mean(data[0, 1]))
print(take_mean(data[:, 1]))

# %%
# write a for loop that will loop over each column of data,
# take the mean and store in array that has a number for each column
data = np.random.rand(4, 5)
columns = data.shape[1]

output = np.zeros(columns)

for i in range(columns):
    output[i] = np.mean(data[:, i])

print(output)

# %% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset.
# This dataset comes with the sklearn pacakge so we can just
# load it in directly.
# It describes measurements of sepal & petal width/length for
# three different species of iris

iris_df = pd.read_csv('iris_df.csv', index_col='species')


# %%
# 1. How do you view the "unique" species in the `iris_df` index?
# hint use the function np.unique() and apply it to the index of the dataframe

print(np.unique(iris_df.index))

# %%
# 2. How do you "locate" only rows for the `versicolor` species?
# Hint use .loc to the rows that have the name 'versicolor'

iris_df.loc['versicolor']

# %%
# 3. Calculate the mean for every column of the dataframe grouped by species.
# look back at our pandas examples Use groupby.mean

species_mean = iris_df.groupby(iris_df.index).mean()

print(species_mean)

# %%
# 4. Make a scatter plot of the `sepal length (cm)`
# versus the `petal length (cm)` for the `versicolor`` species?
# hint first grab out just the rows you want to plot
# Then use scatter plot function to plot the columns you want (plotting notes)

versicolor_df = iris_df[iris_df.index == 'versicolor']

ax = versicolor_df.plot.scatter(x='petal length (cm)', y='sepal length (cm)',
                                marker='x')
ax.set_title("Versicolor Sepal Length vs. Petal Length")

# %%
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure.
# Color them 'tomato', 'darkcyan', and 'darkviolet', respectively.
# (BONUS: Try to write the code so you only need to type each
# iris name one time)

# Repeat what you did in 4 three times
versicolor_df = iris_df[iris_df.index == 'versicolor']
setosa_df = iris_df[iris_df.index == 'setosa']
virginica_df = iris_df[iris_df.index == 'virginica']

fig, ax = plt.subplots()
ax.scatter(versicolor_df['petal length (cm)'],
           versicolor_df['sepal length (cm)'],
           marker='x', color='tomato', label='versicolor')
ax.scatter(setosa_df['petal length (cm)'], setosa_df['sepal length (cm)'],
           marker='x', color='darkcyan', label='setosa')
ax.scatter(virginica_df['petal length (cm)'],
           virginica_df['sepal length (cm)'],
           marker='x', color='darkviolet', label='virginica')
ax.set_title("Sepal Length vs. Petal Length")
ax.legend(loc='upper left', frameon=False)
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Sepal Length (cm)')

# %%
# Type each species one time

species1 = 'versicolor'
species2 = 'setosa'
species3 = 'virginica'

species1_df = iris_df[iris_df.index == species1]
species2_df = iris_df[iris_df.index == species2]
species3_df = iris_df[iris_df.index == species3]

fig, ax = plt.subplots()
ax.scatter(species1_df['petal length (cm)'], species1_df['sepal length (cm)'],
           marker='x', color='tomato', label=species1)
ax.scatter(species2_df['petal length (cm)'], species2_df['sepal length (cm)'],
           marker='x', color='darkcyan', label=species2)
ax.scatter(species3_df['petal length (cm)'], species3_df['sepal length (cm)'],
           marker='x', color='darkviolet', label=species3)
ax.set_title("Sepal Length vs. Petal Length")
ax.legend(loc='upper left', frameon=False)
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Sepal Length (cm)')

# or this

fig, ax = plt.subplots()
ax.scatter(iris_df[iris_df.index == species1]['petal length (cm)'],
           iris_df[iris_df.index == species1]['sepal length (cm)'],
           marker='x', color='tomato', label=species1)
ax.scatter(iris_df[iris_df.index == species2]['petal length (cm)'],
           iris_df[iris_df.index == species2]['sepal length (cm)'],
           marker='x', color='darkcyan', label=species2)
ax.scatter(iris_df[iris_df.index == species3]['petal length (cm)'],
           iris_df[iris_df.index == species3]['sepal length (cm)'],
           marker='x', color='darkviolet', label=species3)
ax.set_title("Sepal Length vs. Petal Length")
ax.legend(loc='upper left', frameon=False)
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Sepal Length (cm)')

# %%
# 6. Write a function that will do 'ax.scatter' for a given iris type
# and desired color of points and use this to function to modify the code
# you make in 5

# HINT no for loop needed, the function should have two arguments and you
# will call it 3 times. Copy your code from #5 down here and replace your
# ax.scatter calls with your function.

versicolor_df = iris_df[iris_df.index == 'versicolor']
setosa_df = iris_df[iris_df.index == 'setosa']
virginica_df = iris_df[iris_df.index == 'virginica']

# Input is species dataframe and color


def plot_iris(species_data, color):
    """Plots 3 individual graphs

    ***Keword arguments:
    species_data -- the dataframe that holds only one species
    color -- the plots color
    """
    fig, ax = plt.subplots()
    ax.scatter(species_data['petal length (cm)'],
               species_data['sepal length (cm)'], marker='x', color=color)
    ax.set_title("Sepal Length vs. Petal Length")


plot_iris(versicolor_df, 'tomato')
plot_iris(setosa_df, 'darkcyan')
plot_iris(virginica_df, 'darkviolet')


def plot_iris_v2(species1, species2, species3, color1, color2, color3):
    """Plots 1 graph of 3 species

    ***Keyword arguments:
    species1 -- specific species of iris
    species2 -- specific species of iris
    species3 -- specific species of iris
    color1 -- color of plot for species1
    color2 -- color of plot for species2
    color3 -- color of plot for species3
    """
    fig, ax = plt.subplots()
    ax.scatter(iris_df[iris_df.index == species1]['petal length (cm)'],
               iris_df[iris_df.index == species1]['sepal length (cm)'],
               marker='x', color=color1, label=species1)
    ax.scatter(iris_df[iris_df.index == species2]['petal length (cm)'],
               iris_df[iris_df.index == species2]['sepal length (cm)'],
               marker='x', color=color2, label=species2)
    ax.scatter(iris_df[iris_df.index == species3]['petal length (cm)'],
               iris_df[iris_df.index == species3]['sepal length (cm)'],
               marker='x', color=color3, label=species3)
    ax.set_title("Sepal Length vs. Petal Length")
    ax.legend(loc='upper left', frameon=False)
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Sepal Length (cm)')


plot_iris_v2('versicolor', 'setosa', 'virginica', 'tomato',
             'darkcyan', 'darkviolet')

# %%
# Thursday Exercises

# Exercise 1
# modify the following to create a pandas dataframe where
# the column 'datetime' is a datetime object. You should do this two ways:
# (1) by modifying the read.table function arguments directly.
# (2) keeping the read.table line I have below the same and
# modifying the dataframe after the fact.
# How can you check to confirm that what you did worked?

# Method 1
data = pd.read_table('streamflow_demo.txt', sep='\t',
                     skiprows=30, names=['agency_cd', 'site_no','datetime',
                                         'flow', 'code'],
                                            parse_dates=['datetime'],
                                            index_col='datetime')

# Check it to see if it worked
data.info()
data.head()
data.index

# %%
# Method 2
data2 = pd.read_table('streamflow_demo.txt', sep='\t', skiprows=30,
                      names=['agency_cd', 'site_no', 'datetime',
                             'flow', 'code'])

data2['datetime'] = pd.to_datetime(data2['datetime'])
data2 = data2.set_index('datetime')

# Check it to see if it worked
data2.info()
data2.head()
data2.index

# %%
# Exercise 2:

# 2.1: Read the 'daymet.csv' file in as a data frame using
# the 'date' column as the index and making sure to treat
# that column as a datetime object.

daymet_df = pd.read_csv('daymet.csv', index_col='date', parse_dates=['date'])

# %%
# 2.2: Explore this dataset and report what variables
# it contains, what date ranges are covered and the frequency of the data.

daymet_df.info()  # everything with dates from index(9/25/92-9/25/22)
daymet_df.columns  # gives you all column names
daymet_df.index  # gives you the index values

# %%
# 2.3  Make a scatter plot of day length (dayl) vs
# maximum temperature.

fig, ax = plt.subplots()
fig.set_size_inches(10, 7)
ax.scatter(daymet_df['dayl (s)'], daymet_df['tmax (deg c)'],
           marker='x', s=10, color='tomato', label='Daily Max Temp')
ax.set_title('Max Temp vs. Day Length')
ax.legend(loc='upper left', frameon=False)
ax.set_xlabel('Day Length (sec)')
ax.set_ylabel('Max Temp (°C)')

# %%
# 2.4 Make a plot with lines for the monthly average of `tmax`
# for all months after Jan 2015.  Add shading to the plot extending
# to the monthly minimum and maximum of `tmax` for the same period.

# Hint - Use the pandas resample function for datetime objects and
# the plt.fill type for the shading.

# I found this fancy option to sort by dates using something called
# and "f-string". This is cool. :)

# Specify the desired month and year
year = 2015
month = 1

# Use f-string to filter data
# specify desired date, formatted 2 digits, padding with leading zeros
# then resample based on that info, resample again for mean
desired_date = f'{year}-{month:02d}'
result = daymet_df.resample('D').last().loc[desired_date:]

monthly_mean = result.resample('M').mean()['tmax (deg c)']
monthly_min = result.resample('M').min()['tmax (deg c)']
monthly_max = result.resample('M').max()['tmax (deg c)']

tick_locations = [monthly_mean.index[i] for i in
                  range(0, len(monthly_mean.index), 3)]

# Plot the data from the above results
fig, ax = plt.subplots()
fig.set_size_inches(15, 7)
ax.plot(monthly_mean, label='Mean Max Temp')
ax.fill_between(monthly_max.index, monthly_min, monthly_max, color='r',
                alpha=0.2, label='Max Temp Range')
ax.set_title('Mean Monthly Max Temp & Range')
ax.legend(loc='upper left')
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.set_xticks(tick_locations)
plt.xticks(rotation=45)
ax.set_xlabel('Month & Year')
ax.set_ylabel('Max Temp (°C)')
ax.grid(which='both', axis='both', linestyle='-', linewidth=1)


# %%
