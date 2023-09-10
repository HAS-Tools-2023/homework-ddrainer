# Import necessary packages
import os
import numpy as np
import earthpy as et

# Avg monthly precip (inches) of Boulder, CO for 1-d array
avg_month_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=avg_month_precip_url)

# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

# Path relative to working directory
avg_month_precip_path = os.path.join("data", "earthpy-downloads","avg-monthly-precip.txt")

# Check path
if os.path.exists(avg_month_precip_path):
    print("This is a valid path.")
else:
    print("This path does not exist.")

# Import data into array if path exists
if os.path.exists(avg_month_precip_path):
    avg_month_precip = np.loadtxt(avg_month_precip_path)
    print(avg_month_precip)
else:
    print("This path does not exist.")

# %%
# Set x equal to 5 and y equal to 10
x = 5
y = 10

# Execute code based on comparison of x to y
if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")
# %%
# Set fname based on which text string contains "precip"
if "precip" in "avg_monthly_temp":
    fname = "avg_monthly_temp"
    print(fname)

elif "precip" in "avg_monthly_precip":
    fname = "avg_monthly_precip"
    print(fname)  

else:
    print("Neither textstring contains the word precip.")
# %%

# Create 5 objects
list_of_values = [1, 2, 3, 4, 5]

# Print each object separately
print(list_of_values)

# Cycle through each object and print
for avalue in list_of_values:
    print("the current value is:", avalue+1)
# %%
# Create list of integers
num_list = [12, 5, 136, 47]

# For each item in list, add 10 and print new value
for x in num_list:
    x += 10
    print("The value of the variable 'x' is:", x)
# %%
