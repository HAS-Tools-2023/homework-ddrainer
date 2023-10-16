# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name and path to where you have stored the data
filename = '../../data/streamflow_week7.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../../data/streamflow_week7.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Plot 3

mybins = np.linspace(0, np.log10(np.max(data["flow"])), num=15)
plt.hist(np.log10(data["flow"]), bins=mybins, label="Streamflow")
plt.title('Streamflow')
plt.ylabel('Count')
plt.legend(loc="upper left")

# %%
# Plot 2

ax=data.plot.scatter(x='month', y='flow',
c='year', colormap='viridis', marker='x')
ax.set_title("Monthly stream Flow")

ax=data.plot.scatter(x='month', y='flow',
c='year', colormap='magma', marker='x')
ax.set_title("Monthly stream Flow")

ax.grid(color='r')
# %%
# Plot 1
# Need to make changes to this graph (Drainer)

x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
y1=np.sin(x)
y2=np.cos(x)
ax = plt.axes()
ax.plot(x, y1, linestyle='dotted', label='sinx')
ax.plot(x, y2, linestyle='dashed', color='green', label='cosx')
ax.set_title('cos(x) vs. sin(x)')
ax.legend(loc='upper right')
ax.set_facecolor(color='darkorange') # Add my stuff here

#%%
# Random practice

fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x), linestyle='dotted', label='sin(x)')
ax[1].plot(x, np.cos(x), linestyle='dashed', color='green', label='cos(x)')


# %%
# Practice Plotting

plt.plot(x, np.sin(x), color='blue', label='sin(x)')
plt.plot(x, np.cos(x), color='green', label='cos(x)')
plt.plot(x, np.sin(x)-1, color='orange', label='sin(x)-1')
plt.plot(x, np.sin(x)+1, color='black', label='sin(x)+1')
plt.plot(x, np.cos(x)-1, color='yellow', label='cos(x)-1')

plt.xlim(0,8)
plt.ylim(-1,1)
plt.axis('equal')
plt.title('A bunch of curves')
plt.legend()

# %%
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');

#%%
# Simple Scatter Plots

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black')

# %%
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)
# %%
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)
# %%
plt.scatter(x, y, marker='o')

# %%
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()
# %%

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)


# %%
def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()

contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy', alpha=0.5)
plt.colorbar()

# %%
# histograms

plt.style.use('seaborn-white')

data = np.random.randn(1000)

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x3, **kwargs)

# %%
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')


# %%
