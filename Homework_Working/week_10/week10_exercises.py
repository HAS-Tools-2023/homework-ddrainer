# %%
# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# %%
# Tuesday Exercises

### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean 
# of every colum of the dataframe
# If you have time try doing it with and without 
# a for loop (You can either use the function inside
# your for loop or put a for loop inside your function)

def average_columns(my_array):
    ncol=my_array.shape[1]
    col_mean=np.zeros(5)
    for i in range(ncol):
        col_mean[i]= np.mean(my_array[:,i])
    return(col_mean)

average_columns(data)
# %%
#define a function that can take the mean of a set of nubmers
# and return one value
"""Function to take the mean of an input of numbers,
which can be a list of numbers, or an array, or just
a part of an array
"""

def take_mean(some_numbers):
    mean = np.mean(some_numbers)
    return mean

# Examples
print(take_mean([10,10,10,7,10,5]))
print(take_mean(data))
print(take_mean(data[1]))
print(take_mean(data[0,1]))
print(take_mean(data[:,1]))

# %%
# write a for loop that will loop over each column of data, 
# take the mean and store in array that has a number for each column
data = np.random.rand(4, 5)
columns = data.shape[1]

output = np.zeros(columns)

for i in range(columns):
    output[i] = np.mean(data[:, i])

print(output)

#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for
# three different species of iris

iris_df = pd.read_csv('iris_df.csv', index_col='species')


# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint use the function np.unique() and apply it to the index of the dataframe

print(np.unique(iris_df.index))

# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#Hint use .loc to the rows that have the name 'versicolor'

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

ax=versicolor_df.plot.scatter(x='petal length (cm)', y='sepal length (cm)',
                        marker='x')
ax.set_title("Versicolor Sepal Length vs. Petal Length")

# %%
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. 
# Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. 
# (BONUS: Try to write the code so you only need to type each iris name one time)

# Repeat what you did in 4 three times
versicolor_df = iris_df[iris_df.index == 'versicolor']
setosa_df = iris_df[iris_df.index == 'setosa']
virginica_df = iris_df[iris_df.index == 'virginica']

fig, ax = plt.subplots()
ax.scatter(versicolor_df['petal length (cm)'], versicolor_df['sepal length (cm)'],
                        marker='x', color='tomato')
ax.scatter(setosa_df['petal length (cm)'], setosa_df['sepal length (cm)'],
                        marker='x', color='darkcyan')
ax.scatter(virginica_df['petal length (cm)'], virginica_df['sepal length (cm)'],
                        marker='x', color='darkviolet')
ax.set_title("Sepal Length vs. Petal Length")

# Type each species one time


# %%
# 6. Write a function that will do 'ax.scatter' for a given iris type 
# and desired color of points and use this to function to modify the code you make in 5

#HINT no for loop needed, the function should have two arguments and you will call it 3 times. 
#Copy your code from #5 down here and replace your ax.scatter calls with your function. 

versicolor_df = iris_df[iris_df.index == 'versicolor']
setosa_df = iris_df[iris_df.index == 'setosa']
virginica_df = iris_df[iris_df.index == 'virginica']

# Input is species dataframe and color
def plot_iris(species_data, color):
    fig, ax = plt.subplots()
    ax.scatter(species_data['petal length (cm)'], species_data['sepal length (cm)'],
                        marker='x', color=color)
    ax.set_title("Sepal Length vs. Petal Length")

plot_iris(versicolor_df, 'tomato')
plot_iris(setosa_df, 'darkcyan')
plot_iris(virginica_df, 'darkviolet')