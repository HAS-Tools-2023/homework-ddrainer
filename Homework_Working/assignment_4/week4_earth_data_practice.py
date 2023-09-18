#%%
#import necessary packages

import os
import earthpy as et

#Create new path 
os.path.join("earth-analytics", "data")

## 'earth-analytics/data'
# %%
# Check that a directory exists on your computer
my_path = os.path.join("earth-analytics", "data")

# Boolean output (True or False)
os.path.exists(my_path)# Check that a directory exists on your computer
my_path = os.path.join("earth-analytics", "data")

# Boolean output (True or False)
os.path.exists(my_path)
# %%
# get current working directory
os.getcwd()

# %%
#change working directory
os.chdir("c:\\Users\\dave8\\Desktop\\HAS_tools\\homework-ddrainer\\Homework_Working")
os.getcwd()

# %%
#change working directory back
os.chdir("c:\\Users\\dave8\\Desktop\\HAS_tools\\homework-ddrainer\\Homework_Working\\assignment_4")
os.getcwd()

# %%
# Find home directory
et.io.HOME

# %%
# Check if the home directory exists (of course it does!)
os.path.exists(et.io.HOME)

# %%
# Create a path to the home/earth-analytics directory on your computer
os.path.join(et.io.HOME, "earth-analytics")
# %%
# Get current working directory
os.getcwd()

# %%
# Check to see if path exits
my_ea_path = os.path.join(et.io.HOME, "earth-analytics")

# Does the path exist?
os.path.exists(my_ea_path)


# %%
# Make a new directory in current working directory

my_ea_path_2 = os.path.join(os.getcwd(), "earth-analytics")
os.mkdir(my_ea_path_2)

# %%
# change working directory to new path
os.chdir(os.path.join(my_ea_path_2))

os.getcwd()

# %%
import numpy as np

# Monthly avg precip for Jan through Mar in Boulder, CO
avg_monthly_precip = np.array([0.70, 0.75, 1.85])

print(avg_monthly_precip)

# %%
# Monthly precip for Jan through Mar in 2002 and 2013
precip_2002_2013 = np.array([
    [1.07, 0.44, 1.50],
    [0.27, 1.13, 1.72]
])

print(precip_2002_2013)
# %%
# Import necessary packages
import os
import numpy as np
import earthpy as et

# Download .txt with avg monthly precip (inches)
monthly_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=monthly_precip_url)

# Download .csv of precip data for 2002 and 2013 (inches)
precip_2002_2013_url = 'https://ndownloader.figshare.com/files/12707792'
et.data.get_data(url=precip_2002_2013_url)

# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

# Import average monthly precip to numpy array
fname = os.path.join("data", "earthpy-downloads",
                     "avg-monthly-precip.txt")

avg_monthly_precip = np.loadtxt(fname)

print(avg_monthly_precip)

# Import monthly precip for 2002 and 2013 to numpy array
fname = os.path.join("data", "earthpy-downloads",
                     "monthly-precip-2002-2013.csv")

precip_2002_2013 = np.loadtxt(fname, delimiter = ",")

print(precip_2002_2013)
# %%
et.Data.get_data(url=monthly_precip_url)

# %%
import numpy as np
np.random.seed(5)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
values = np.random.randint(1, 10, size=125)
compute_reciprocals(values)
# %%
big_array = np.random.randint(1, 100, size=1000000)
%timeit compute_reciprocals(big_array)
# %%
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)  # floor division
# %%

theta = np.linspace(0, np.pi, 3)

print("theta      = ", theta)
print("sin(theta) = ", np.sin(theta))
print("cos(theta) = ", np.cos(theta))
print("tan(theta) = ", np.tan(theta))
# %%
from scipy import special

# %%
# Gamma functions (generalized factorials) and related functions
x = [1, 5, 10]
print("gamma(x)     =", special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x, 2)   =", special.beta(x, 2))
# %%
# Error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x)  =", special.erf(x))
print("erfc(x) =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))
# %%
