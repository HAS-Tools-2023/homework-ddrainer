import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Read in the data
file = 'streamflow_demo.txt'

data = pd.read_table(file, sep='\t', skiprows=30, names=[
                     'agency_cd', 'site_no', 'datetime', 'flow', 'code'])

data[['year', 'month', 'day']] = data['datetime'].str.split('-', expand=True)
data['date'] = pd.to_datetime(data['datetime'])
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
#%%
# Get monthly values
monthly_flow = data.groupby(['month'])[['flow']].describe()
#sorting = data.sort_values(by='flow', ascending=False)

#%%
# original plotting code
#Plotting overall view of parameters
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(monthly_flow['flow']['min'])
axs[0, 0].set_ylabel('Flow (cfs)')
axs[0, 0].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[0, 1].plot(monthly_flow['flow']['25%'])
axs[0, 1].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[1, 0].plot(monthly_flow['flow']['50%'])
axs[1, 0].set_ylabel('Flow (cfs)')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_xticks([0, 2, 4, 6, 8, 10, 12])
axs[1, 1].plot(monthly_flow['flow']['75%'])
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_xticks([0, 2, 4, 6, 8, 10, 12])
fig.suptitle('Monthly Min Flow and Quartile (25%, 50%, 75%)')

# %%
# Modification 1: Pulling repeated values out as variables
ylab='flow (cfs)'
xlab='month'
xtic = [0, 2, 4, 6, 8, 10, 12]
# Note two alternate approaches to creating this array of xtics would be: 
# xtics = np.linspace(0,12,7)
#xtics=np.arange(0,14,2)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(monthly_flow['flow']['min'])
axs[0, 0].set_ylabel(ylab)
axs[0, 0].set_xticks(xtic)
axs[0, 1].plot(monthly_flow['flow']['25%'])
axs[0, 1].set_xticks(xtic)
axs[1, 0].plot(monthly_flow['flow']['50%'])
axs[1, 0].set_ylabel(ylab)
axs[1, 0].set_xlabel(xlab)
axs[1, 0].set_xticks(xtic)
axs[1, 1].plot(monthly_flow['flow']['75%'])
axs[1, 1].set_xlabel(xlab)
axs[1, 1].set_xticks(xtic)
fig.suptitle('Monthly Min Flow and Quartile (25%, 50%, 75%)')

#%%
# Modification 2: Combining lines of code for the axes settings
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(monthly_flow['flow']['min'])
axs[0, 0].set(ylabel=ylab, xticks=xtic)
axs[0, 1].plot(monthly_flow['flow']['25%'])
axs[0, 1].set_xticks(xtic)
axs[1, 0].plot(monthly_flow['flow']['50%'])
axs[1, 0].set(ylabel=ylab, xlabel=xlab, xticks=xtic)
axs[1, 1].plot(monthly_flow['flow']['75%'])
axs[1, 1].set(xlabel=xlab, xticks=xtic)
fig.suptitle('Monthly Min Flow and Quartile (25%, 50%, 75%)')


# %%
# Modification 3: putting this in a loop
#Grab out the column names from your dataframe
col_names=monthly_flow.columns

#Pick the column numbers that you want to plot
pick_list = [3,4,5,6]
print('Plotting the following columns:')
print(col_names[pick_list])


fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.6, wspace=0.4)
ax = ax.flatten()
for i in range(4):
    plot_col=pick_list[i]
    print('iteration', i, 'plotting column', plot_col, col_names[plot_col] )
    ax[i].plot(monthly_flow[monthly_flow.columns[plot_col]])
    ax[i].set(ylabel=ylab, xlabel=xlab, xticks=xtic,
              title=col_names[plot_col][1])
fig.suptitle('Monthly Flow Quantiles')




# %%
