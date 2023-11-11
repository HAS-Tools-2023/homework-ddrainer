#Setup- before you start create a new 'mapping' environment following the instructions from class and make sure you have the following packages installed
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
from matplotlib.ticker import ScalarFormatter


# %%
# Exercise 1: 
# 1. Open the arizona_huc8_shapefil and the arizona_shapefile following the example we did in class. 

# Reading it using geopandas
file =  os.path.join('../../data/', 'arizona_huc8_shapefile', 'WBDHU8.shp')
shapefile1 = gpd.read_file(file)

file =  os.path.join('../../data/', 'arizona_shapefile', 'tl_2016_04_cousub.shp')
shapefile2 = gpd.read_file(file)

# 2. Explore their properties and attributes and be able to explain (1) what type of geometry each is, (2) how many features there are, (3) what attributes each feature has. 

type(shapefile1)
type(shapefile2)

shapefile1.head()
shapefile2.head()

shapefile1.columns
shapefile2.columns
shapefile1.shape #seeing how many entries there are

# 3. Plot each dataset. You can plot them separately but also try plotting subsets and plotting them on top of each other. 

fig, ax = plt.subplots(figsize=(10, 10))
shapefile2.plot(ax=ax)
plt.show()

fig, ax = plt.subplots(figsize=(10, 10))
shapefile1.plot(ax=ax)
plt.show()


#%%
# Exercise 2: 
# 1. Open the WBD_15_HU2_GDB geodatabase and select a different layer to plot than the one I showed (i.e. not HUC6)

file = os.path.join('../../data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')

#This will list all the layers in that file
fiona.listlayers(file)
HUC8 = gpd.read_file(file, layer="WBDHU8")

fig, ax = plt.subplots(figsize=(10, 10))
HUC8.plot(ax=ax)
ax.set_title("HUC Boundaries")
plt.show()

# 2. Create a geodatabase with the two points of interest I showed (i.e. UA and the stream gauge) as well as two additional points of your choosing
# Add some points
# UA:  32.22877495, -110.97688412
# Stream gauge:  34.44833333, -111.7891667
# Luke AFB: 33.535, -112.383056
# DMAFB: 32.163611, -110.849444
# Yuma MCAS: 32.656667, -114.606111
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])

point_list2 = np.array([[-112.383056, 33.535],
                       [-110.849444, 32.163611],
                       [-114.606111, 32.656667]])

#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

point_geom2 = [Point(xy) for xy in point_list2]
point_geom2

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC8.crs)
point_df2 = gpd.GeoDataFrame(point_geom2, columns=['geometry'],
                            crs=HUC8.crs)


# 3. Make a map of your selected datasets. If you have time experiment with changing the markers and lines/fill colors on your plot

fig, ax = plt.subplots(figsize=(10, 10))
HUC8.plot(ax=ax)
shapefile2.plot(ax=ax, color='green', alpha=0.6)
point_df.plot(ax=ax, color='red', marker='^', label='Cities')
point_df2.plot(ax=ax, color='yellow', marker='*', label='Military Bases')
#ax.set_title("HUC8 Boundaries")

# Setup x y axes with labels and add graticules
ax.set(xlabel="Longitude (Degrees)", ylabel="Latitude (Degrees)",
       title="Arizona Map and Watershed Boundaries\n Units: Degrees - Latitude / Longitude")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')
ax.legend()
plt.show()

# Reproject the data
HUC8_robin = HUC8.to_crs('+proj=robin')
shapefile2_robin = shapefile2.to_crs('+proj=robin')
point_df_robin = point_df.to_crs('+proj=robin')
point_df2_robin = point_df2.to_crs('+proj=robin')

# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))

HUC8_robin.plot(ax=ax,
                      color='g')
shapefile2_robin.plot(ax=ax, color='b', alpha=0.4)
point_df_robin.plot(ax=ax, color='red', marker='^', label='Cities')
point_df2_robin.plot(ax=ax, color='yellow', marker='*', label='Military Bases')

ax.set(title="Robinson Coordinate Reference System",
       xlabel="X Coordinates (meters)",
       ylabel="Y Coordinates (meters)")

for axis in [ax.xaxis, ax.yaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)