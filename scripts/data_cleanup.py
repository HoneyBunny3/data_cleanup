import geopandas as gpd
import pandas as pd
import os

# **IMPORT LIBRARIES AND LOAD DATA**
# File paths
data_dir = os.path.join("..", "data", "raw")
output_dir = os.path.join("..", "data", "cleaned")
shapefile_path = os.path.join(data_dir, "trecs__basemap__utm__poly__v1__building_footprints.shp")

# Check if file exists
if not os.path.exists(shapefile_path):
    print(f"Error: File not found at {shapefile_path}")
    exit()

# Load the data
print("Loading data...")
try:
    data = gpd.read_file(shapefile_path)
except Exception as e:
    print(f"Error loading shapefile: {e}")
    exit()

# Display basic information
print("Data loaded successfully!")
print(data.info())
print(data.head())

# **FILL MISSING VALUES**
print("Filling missing values...")
data['geo_domain'] = data['GeoDomain'].fillna('Unknown')
data['building_number'] = data['Building'].fillna('N/A')

# Drop rows with missing geometry (if geometry is crucial)
data = data.dropna(subset=['geometry'])

# Verify changes
print("Missing values handled:")
print(data.isnull().sum())

# **REMOVE DUPLICATES**
print("Removing duplicates...")
duplicates_count = data.duplicated().sum()
print(f"Found {duplicates_count} duplicate rows.")
data = data.drop_duplicates()
print(f"Duplicates removed. Remaining rows: {len(data)}")

# **STANDARDIZE COLUMN NAMES**
print("Standardizing column names...")

# Rename columns in place
data = data.rename(columns={
    "GeoDomain": "geo_domain",
    "Building": "building_number",
    "Building_A": "building_abbreviation",
    "Floor": "floor",
    "notes": "notes"
})

# Drop any leftover duplicates from renaming
data = data.loc[:, ~data.columns.duplicated()]

print("Standardized column names:")
print(data.columns)

# **ADD TRANSFORMATIONS**
print("Adding transformations...")
data['area_sqft'] = data.geometry.area * 10.7639  # Convert area to square feet
print("Transformation added (area in square feet):")
print(data[['building_number', 'area_sqft']].head())

# **SAVE CLEANED DATA**
print("Saving cleaned data...")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cleaned_file_path = os.path.join(output_dir, "cleaned_building_footprints.geojson")
try:
    data.to_file(cleaned_file_path, driver="GeoJSON")
    print(f"Cleaned data saved to {cleaned_file_path}")
except Exception as e:
    print(f"Error saving cleaned data: {e}")