import pandas as pd
import numpy as np
import urllib
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LinearRegression

#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your fo loop or put a for loop inside your function)

def take_mean(numbers):
    mean_value = np.mean(numbers)
    return mean_value

mean_array = np.zeros(5)

for i in range(data.shape[1]):
    mean_array[i] = take_mean(data[:,i])






#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
d = datasets.load_iris()
iris_df = pd.DataFrame(d['data'], columns=d['feature_names'])
iris_df.index = pd.Series(
    pd.Categorical.from_codes(d.target, d.target_names),
    name='species'
)
iris_df.head()

# %%
# 1. How do you view the "unique" species in the `iris_df` index?

# %%
# 2. How do you "locate" only rows for the `versicolor` species?

# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 


# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?



# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)



# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color and use this to function to modify the code you make in 5


