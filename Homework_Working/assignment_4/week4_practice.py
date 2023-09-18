
#%%
import numpy as np

# %%

# list -> ordered data
x =[1, "apple", 43]
x[1]

y = x


y[2]="orange"
print(y)
print(x)

# Be careful...changing y also changed x!

#%%

# x=np.array([1,2,3])
# x[2]
# y=np.array([[1,2,3],[4,5,6]])
# print(y)


x = np.random.randint(10, size=(4,5))
print(x)
print(x[1, 2])


x = np.zeros((2,9))
print(x)

x=np.ones((2,9))
print(x)

print(x.ndim)
print(x.size)
print(x.dtype)


#%%
x = np.array([1,2,3])
y = np.array([4,5,6])

print(x*y)
# does not do matrix multiplication

# print(x.shape)
# columns, rows


# class.method()

#Arrays
## Must use numpy
## like lists, but must be Homogenous data!!!
## Can do math on them!
## Multi-dimenstional!




# %%
import numpy as np
x = np.arange(0, 3**3)
#print(x[:5]) #print first 5 
#print(x[22:])

array_length = x.size

print(x[array_length - 5:])

# %%
import numpy as np
x=np.arange(10)
x.reshape(5,2)
# %%
y=np.arange(100)
print(y)

# %%
