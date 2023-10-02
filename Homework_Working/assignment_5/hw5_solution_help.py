# %%

# The following examples are broken...

for month in flow_data[;,1] == 9: # you're going to get an array of True/False where it's checking if the month is equal to 9
    for flow in flow_data[:0] < 50:
        print(flow_data)

for i in range(len(flow_data)):
    if (flow_data[i,1]) == 9,
        


# %%

while flow_data[:,1] == 9:
    if flow_data[:,0] < 50:
        print(flow, date)



# no class on Tuesday, 26 Sep or on Thursday, 5 Oct


# %%
# Exercise 1

import numpy as np

a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
d = np.zeros(len(a))


for i in range(len(a)):
    d[i] = max(a[i], b[i])

print(d)

# Exercise 2
# %%
e = np.zeros(len(d))

while i in range(len(d)-1):
    e[i] = sum(d[i],d[i+1])

print(e)


# %%
# test stuff
import numpy as np

np.tile(np.arange(2015,2020),5)

print(np.repeat(np.arange(2015,2020),12))

print(np.tile(np.arange(1,13),5))

# %%
