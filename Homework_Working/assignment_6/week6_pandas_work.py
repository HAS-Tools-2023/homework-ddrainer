#%%
# Pandas Exercise One
# Solution will be available next Tuesday

import numpy as np
import pandas as pd

data = np.ones((7,3))
data_frame = pd.DataFrame(data, columns=['data1', 'data2', 'data3'], index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(data_frame)
# %%
# Change all rows with vowels to 3

first_df = data_frame #make a copy to anew dataframe

first_df.loc['a'] = 3 #set row a to all 3
first_df.loc['e'] = 3 #set row e to all 3

print(first_df)

# %%
# Multiply first 4 rows by 7

first_df.iloc[:4] =first_df.iloc[:4] * 7

print(first_df)

# %%
# Create a checkerboard pattern of 1s and 0s using loc

first_df.loc[['a','c','e','g'], ['data1','data3']] = 0 # Set every other row in column data1 and data3 to 0
first_df.loc[['b','d','f'], ['data2']] = 0 # Set every other row in column data2 to 0

first_df.loc[['a','c','e','g'], ['data2']] = 1
first_df.loc[['b','d','f'], ['data1','data3']] = 1

print(first_df)


# %%
# Create a checkerboard pattern of 1s and 0s using iloc

first_df.iloc[1::2, ::2] = 1 # Set odd rows, even columns to 1
first_df.iloc[::2, 1::2] = 1 # Set even rows, odd columns to 1
first_df.iloc[::2, ::2] = 0 # Set even rows, even columns to 0
first_df.iloc[1::2, 1::2] = 0 # Set odd rows, odd columsn to 0

print(first_df)


#%%
# Pandas Exercise Two
# Fill the NA values with 999

import pandas as pd
import numpy as np

data_frame = pd.DataFrame([[1, np.nan, 2],
                          [2, 3, 5],
                          [np.nan, 4, 6]])

print(data_frame)

fixed_df = data_frame.fillna(999)

print(fixed_df)
# %%
