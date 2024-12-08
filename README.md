# Data Cleanup Project

## Overview
This repository showcases a comprehensive data cleanup and transformation project. The aim is to demonstrate the process of preparing raw and messy datasets for analysis and decision-making. The project highlights techniques such as handling missing values, removing duplicates, transforming data formats, and other essential cleanup tasks.

## Objectives
- Explore and understand messy datasets.
- Perform data cleanup using the Python library `pandas`.
- Transform data into a usable format suitable for analysis and visualization.
- Showcase proficiency in data preparation, a critical step in the data analytics lifecycle.

## Dataset
The dataset used in this project represents **UTM building footprint geometry** as of November 2020. It includes information such as:
- Geographical domain
- Building numbers
- Building abbreviations
- Floor information
- Associated notes

The dataset was created by the **TRecs LIS team** through fieldwork efforts like drone and LiDAR scans. It supports accurate mapping for University print and web campus maps and is visible in the **UTM campus maps** and **TRecs ArcGIS Online (AGOL)** platforms.

The dataset uses the **NAD_1983_2011_StatePlane_Texas_Central_FIPS_4203_Ft_US** coordinate system and is authorized for use as public domain. The data comes from the Technology Resources collection and is part of the Basemap collection.

## Key Features
1. **Data Import**: Scripts to load data from shapefiles into Python.
2. **Exploratory Data Analysis (EDA)**: Identifying common issues such as missing values, duplicates, and data inconsistencies.
3. **Data Cleaning**: Fixing issues such as:
   - Handling missing values.
   - Removing duplicates.
   - Renaming columns.
   - Converting data types.
4. **Data Transformation**: Applying techniques like:
   - Normalization and standardization.
   - Encoding categorical variables.
   - Aggregating and restructuring data.
5. **Export Clean Data**: Saving the cleaned dataset for further use in analysis tools.

## Repository Structure
```
data_cleanup/
│
├── data/               # Directory for raw and cleaned datasets
│   ├── raw/            # Raw datasets
│   └── cleaned/        # Cleaned datasets
│
├── docs/               # Documentation files
│   ├── DATA_DICTIONARY.md
│
├── notebooks/          # Jupyter notebooks for EDA and cleanup steps
├── scripts/            # Python scripts for automation
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Tools and Technologies
- **Python**: For scripting and data manipulation.
- **Libraries**:
  - `pandas` for data cleaning and manipulation.
  - `numpy` for numerical operations.
  - `geopandas` for geographic data handling.
  - `matplotlib` for basic visualizations.

## Data Dictionary
A detailed data dictionary for the cleaned dataset can be found [here](docs/DATA_DICTIONARY.md).

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data_cleanup.git
   cd data_cleanup
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Explore the scripts and notebooks to understand and replicate the data cleanup process.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Dataset provided by the [TRecs LIS team](https://geodata.lib.utexas.edu/)

---