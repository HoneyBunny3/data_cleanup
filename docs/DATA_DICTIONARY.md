### Data Dictionary for Cleaned Dataset

| **Column Name**         | **Data Type**    | **Description**                                                                                 |
|--------------------------|------------------|-------------------------------------------------------------------------------------------------|
| `geo_domain`            | String           | The geographical domain to which the building belongs (e.g., UTM).                              |
| `building_number`       | String           | The unique identifier for each building.                                                        |
| `building_abbreviation` | String           | The abbreviated name or code for the building.                                                  |
| `floor`                 | String           | Information about the floor level, if available.                                                |
| `notes`                 | String           | Additional notes or comments about the building.                                                |
| `created_us`            | String           | The username of the user who created the building entry.                                        |
| `created_da`            | DateTime         | The date when the building entry was created.                                                   |
| `last_edite`            | String           | The username of the last editor who modified the building entry.                                |
| `last_edi_1`            | DateTime         | The date when the building entry was last modified.                                             |
| `GlobalID`              | String           | A globally unique identifier (GUID) for each building.                                          |
| `Shape_STAr`            | Float            | The calculated area of the building shape in the dataset’s spatial units (likely square meters).|
| `Shape_STLe`            | Float            | The calculated perimeter of the building shape in the dataset’s spatial units (likely meters).  |
| `geometry`              | Geometry         | The spatial geometry of the building footprint.                                                 |
| `area_sqft`             | Float            | The calculated area of the building in square feet.                                             |

---