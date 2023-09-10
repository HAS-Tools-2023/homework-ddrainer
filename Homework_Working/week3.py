#%%
mylist=['a', 'b', 'c', 'd']
print(mylist[1] + mylist[0] + mylist[3])

# %%
print(mylist[1],mylist[0],mylist[3])

# %%
test=mylist[1]+mylist[0]+mylist[3]
print(test)
# %%
import numpy as np
# %%  1.)
# Write code to translate a boolean value
# to a string using a conditional statment.
#  Specifically, if the `testval` 
# is `True` then print "Yes" and if it is
# `False` then print "No"
testval = bool(np.random.choice([0, 1]))
# TODO: Your code here
print(testval)
if testval:
        print("Yes")
else: 
        print("no")
message = None
# ...
print(message)
# %%
