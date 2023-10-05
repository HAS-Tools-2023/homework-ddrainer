#%%
import pandas as pd

# Sample DataFrame
data2 = {'column_name': [10, 15, 20, 25, 30],
        'specific_value': [16, 20, 35, 6, 22]}

df = pd.DataFrame(data2)

# %%
specific_value = df['specific_value'].iloc[0]  # Get the specific value from the DataFrame

print(specific_value)


# Calculate the minimum and maximum allowed values
min_value = specific_value - (0.10 * specific_value)
max_value = specific_value + (0.10 * specific_value)

# Filter rows where 'column_name' values are within the specified range
filtered_df = df[(df['column_name'] >= min_value) & (df['column_name'] <= max_value)]

print(max_value)
# %%
