# %%
# Import Packages

import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from shapely.geometry import box
import contextily as ctx

# %%
# Get layers and plot

# Get stream gauges for AZ
file = os.path.join('../../../data/gagesii_shapefile',
                    'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)  # read file into gpd dataframe

gages.STATE.unique()  # Get states
gages_AZ = gages[gages['STATE'] == 'AZ']  # Filter for AZ

gages_AZ_NAD83 = gages_AZ.to_crs(epsg=4269)  # Change the CRS to match

# Get Arizona State Boundaries
file = os.path.join('../../../data/', 'arizona_shapefile',
                    'tl_2016_04_cousub.shp')
arizona = gpd.read_file(file)  # read file into gpd dataframe

# Get watershed boundary
file = os.path.join('../../../data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
HUC8 = gpd.read_file(file, layer="WBDHU8")  # read file into gpd dataframe

# Get Railways
file = os.path.join('../../../data/TRAN_Arizona_State_Shape/Shape',
                    'Trans_RailFeature.shp')
rail = gpd.read_file(file)  # read file into gpd dataframe

# Get AZ international boundary
file = os.path.join('../../../data/GOVTUNIT_Arizona_State_Shape/Shape',
                    'GU_InternationalBoundaryLine.shp')
intl_boundary = gpd.read_file(file)  # read file into gpd dataframe

# Get major rivers
file = os.path.join('../../../data/USA_Hydrography', 'USA_Hydrography.shp')
rivers = gpd.read_file(file)  # read file into gpd dataframe

# Create a custom polygon to clip rivers
polygon = box(-116, 39, -107, 29)  # Set bounding box
poly_gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs=gages_AZ_NAD83.crs)

rivers_clipped = rivers.clip(polygon)  # New rivers object

# Remove fill from polygons for easier manipulation
HUC8['geometry'] = HUC8['geometry'].boundary
arizona['geometry'] = arizona['geometry'].boundary

# Add UA and Class Streamgauge Points
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])
point_geom = [Point(xy) for xy in point_list]
point_geom

point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC8.crs)
point_df.to_crs(epsg=4269)  # convert to correct crs

# Plot everything on a Topo Base Map
fig, ax = plt.subplots(figsize=(10, 15))
HUC8.plot(ax=ax, color='green', alpha=0.4, facecolor='lightgreen',
          linewidth=1, linestyle='dotted', label='HUC8 Boundaries')
intl_boundary.plot(ax=ax, color='red', label='Int Boundary', linewidth=4)
rail.plot(ax=ax, color='black', linestyle='dashed', linewidth=0.5,
          label='Railways')
arizona.plot(ax=ax, color='darkblue', facecolor='none', linewidth=1.5,
             label='Arizona')
gages_AZ_NAD83.plot(markersize=45, ax=ax, marker='^', label='Gauges',
                    color='purple')
rivers_clipped.plot(ax=ax, color='cyan', linewidth=2, linestyle='dotted',
                    label='Major Rivers')
point_df.plot(ax=ax, color='red', marker='*', markersize=100,
              label='Points of Interest')
ctx.add_basemap(ax, source=ctx.providers.OpenTopoMap,
                crs=arizona.crs)  # Add Topo basemap
ax.set(title='AZ Watershed', xlabel='Longitude', ylabel='Latitude')
ax.legend()
