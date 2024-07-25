import geopandas as gpd
import pandas as pd

# Load the shapefile using geopandas
shape = gpd.read_file("/Users/nc7172/Documents/GitHub/blender_gis_nyc_trees/gis_data/vector_files/nyc_chs_2009_survey/CHS_2009_DOHMH_2010B.shp")

# Convert the GeoDataFrame to a regular DataFrame
df = pd.DataFrame(shape)

# Filter the DataFrame based on the values in FIRST_BORO and select specific columns
filtered_df = df[df['FIRST_BORO'].isin(['Bronx', 'Man'])][['FIRST_BORO', 'FIRST_UHF_', 'exercs2']]

filtered_df = filtered_df.sort_values(by='exercs2')

print(filtered_df)
