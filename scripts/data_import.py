import geopandas as gpd
import os

# File paths
data_dir = os.path.join("..", "data", "raw")
output_dir = os.path.join("..", "data", "cleaned")
shapefile_path = os.path.join(data_dir, "trecs__basemap__utm__poly__v1__building_footprints.shp")

# Load the shapefile
print("Loading data...")
data = gpd.read_file(shapefile_path)

# Show the first few rows
print(data.head())

# Save to cleaned folder as GeoJSON (or another format of your choice)
cleaned_path = os.path.join(output_dir, "cleaned_building_footprints.geojson")
data.to_file(cleaned_path, driver="GeoJSON")
print(f"Data saved to {cleaned_path}")