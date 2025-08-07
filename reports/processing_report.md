# 🧼 Data Harmonization Report (2010–2022)  
*Standardization and merging of raw meat consumption and socioeconomic datasets for modeling and visualization*

**Author:** Maura E. Ramirez-Quezada  
**Deliverable:** [`meat_processed_merged_data.csv`](Data/processed/meat_processed_merged_data.csv)  
**Scope:** Standardization and merging of raw socioeconomic and consumption datasets for further modeling and visualization

---

## 🎯 Objective

This report summarizes the data processing stage of the project. The goal was to consolidate real-world datasets on meat consumption and socioeconomic indicators into a unified, time-aligned, and analysis-ready dataset. The resulting table will serve as the foundation for downstream modeling, exploratory analysis, and visualizations.

The codebase uses `pandas` with modular utilities (`data_loader.py`, `data_preprocessing.py`) to ensure reproducibility and consistent preprocessing across all sources.

---

## 📁 Datasets Processed

| Source     | File Name                                            | Raw Span    | Used Span   |
|------------|------------------------------------------------------|-------------|-------------|
| FAO        | `faostat_meat_kg_per_capita.csv`                    | 2010–2022   | 2010–2022   |
| World Bank | `worldbank_gdp_per_capita.csv`                      | 1960–2024   | 2010–2022   |
| World Bank | `worldbank_urban_population.csv`                    | 1960–2024   | 2010–2022   |
| OWID       | `global-meat-production.csv`                        | 1961–2023   | 2010–2022   |

---
**We selected the 2010–2022 range because it is the only period with full coverage across all datasets, allowing consistent modeling without relying on extrapolation or heavy imputation.**



## 🔧 Dataset-Specific Processing
---
### 🧼 FAO – Food Balance Sheets

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | 11,864 rows × 15 columns                                                                                 |
| **Variables selected**  | Retained: `Area`, `Year`, `Item`, `Value`, representing country, year, meat type, and consumption (kg/capita) |
| **Variables dropped**   | Removed: `Area Code`, `Item Code`, `Element Code`, and other metadata not needed for this study          |
| **Filtering applied**   | - Years filtered to 2010–2022 to align with other datasets  <br> - `"Meat, Other"` excluded due to ambiguous definition |
| **Column renaming**     | Renamed for consistency: `Area → Country`, `Value → meat_consumption`                                   |
| **Transformation**      | Pivoted `Item` column to separate columns per meat type (`Bovine Meat`, `Pigmeat`, etc.), preserving analytical granularity |
| **Final shape**         | 2,383 rows × 6 columns                                                                                    |
| **Missing data**        | `Pigmeat` column includes 46 missing values inherited from the source. Retained for now; to be handled during EDA |

---

### 💰 World Bank – GDP per Capita

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | Wide format: one column per year, covering 1960–2024                                                     |
| **Variables selected**  | Filtered to include only rows with `Indicator Code == "NY.GDP.PCAP.CD"`                                  |
| **Filtering applied**   | Years filtered to 2010–2022 to ensure overlap with other datasets                                        |
| **Column renaming**     | Renamed: `Country Name → Country`, value column → `GDP_per_capita`                                       |
| **Transformation**      | Reshaped from wide to long format: `Country`, `Year`, `GDP_per_capita`                                   |
| **Final shape**         | 3,458 rows × 3 columns                                                                                    |
| **Missing data**        | None within selected time range                                                                          |

---

### 🏙️ World Bank – Urban Population (%)

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | Wide format: one column per year, covering 1960–2024                                                     |
| **Variables selected**  | Filtered to rows with `Indicator Code == "SP.URB.TOTL.IN.ZS"`                                            |
| **Filtering applied**   | Years restricted to 2010–2022 to match range across datasets                                             |
| **Column renaming**     | Renamed: `Country Name → Country`, value column → `urban_population`                                     |
| **Transformation**      | Reshaped to long format with columns: `Country`, `Year`, `urban_population`                             |
| **Final shape**         | 3,458 rows × 3 columns                                                                                    |
| **Missing data**        | None within selected time range                                                                          |

---

### 🏭 OWID – Global Meat Production

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | Long format: data from 1961 to 2023                                                                      |
| **Variables selected**  | Retained: `Entity`, `Year`, `Meat, total | ... tonnes`                                                  |
| **Filtering applied**   | Years filtered to 2010–2022 to ensure full overlap with other datasets                                  |
| **Column renaming**     | Renamed: `Entity → Country`, production column → `Production`                                            |
| **Transformation**      | No pivoting required; dataset already structured in long format                                          |
| **Final shape**         | 14,613 rows × 3 columns                                                                                   |
| **Missing data**        | No missing values detected in selected range                                                             |


- Retained columns: `Entity`, `Year`, `Meat, total | ... tonnes`
- Renamed `Entity → Country`, `...tonnes → Production`
- Filtered to 2010–2022

**Final shape:**  14,613 rows × 3 columns

---

## 🔗 Merging Strategy

- All datasets were harmonized to use `Country` (object) and `Year` (int) as keys
- Country names were standardized using `country_converter`, with a custom dictionary for unresolved cases (e.g., “USA” vs “United States”)
- Duplicates or overlapping entries were checked prior to merging
- Datasets were merged using inner joins on [`'Country'`, `'Year'`], applied sequentially to preserve consistency and ensure complete records across all sources.
- The logic was implemented in `data_preprocessing.py` via a modular function
- Optional datasets (education, emissions) were not merged at this stage

---

## ✅ Final Output Summary

| Metric                  | Value              |
|--------------------------|--------------------|
| Final dataset shape      | 2,609 rows × 9 columns |
| Years covered            | 2010–2022          |
| Countries included       |  187        |
| Columns                  | `'Country'`, `'Year'`, `'Bovine Meat'`, `'Mutton & Goat Meat'`, `'Pigmeat'`,`'Poultry Meat'`, `'GDP_per_capita'`, `'urban_population'`, `'Production'`|
| Columns with missing data| `Pigmeat` only  |
| Output file              | `Data/processed/meat_processed_merged_data.csv`|

---

## 🧭 Notes
- Only `Pigmeat` includes known missing values (46 entries inherited from source). Other columns were validated for completeness across the selected range.
- No feature scaling, outlier removal, or imputation was performed at this stage.
- This dataset is now ready for use in modeling pipelines, EDA, or dashboard visualizations.
- For questions about specific filters or merge behavior, refer to the preprocessing module logic.