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
### FAO – Food Balance Sheets

**Initial shape:** 11,864 rows × 15 columns  
**Relevant variables retained:** `Area`, `Year`, `Item`, `Value` — representing country, year, meat type and consumption (kg per capita).

- Unused fields (e.g., country code, item code, element code) were dropped as they are redundant for this study.
- Filtered to 2010–2022 to match the overlapping availability across all sources.
- The `"Meat, Other"` category was excluded due to its ambiguity and inconsistent definition across countries.
- Columns were renamed to standardize for merging: `Area → Country`, `Value → meat_consumption`.
- The `Item` column (meat type) was pivoted into separate columns to retain granularity across categories.
  This approach was preferred over aggregation, as it enables richer analysis by meat type.

**Post-pivot shape:** 2,383 rows × 6 columns  
**Note:** The` Pigmeat` column contains 46 missing values inherited from the source data. These were kept as-is, as further handling will be determined during the exploratory analysis phase.
---
### World Bank – GDP per Capita

- Original format: wide (one column per year)
- Selected only entries with `'Indicator Code' == "NY.GDP.PCAP.CD"`
- Years filtered to 2010–2022
- Reshaped into long format (`Country`, `Year`, `GDP_per_capita`)
- Renamed columns to match standard keys

**Final shape:** 3,458 rows × 3 columns

---

### World Bank – Urban Population (%)

- Same structure as the GDP dataset
- Selected `'Indicator Code' == "SP.URB.TOTL.IN.ZS"`
- Reshaped to long format (`Country`, `Year`, `urban_population`)
- Filtered to 2010–2022
- Renamed columns for consistency

**Final shape:** 3,458 rows × 3 columns

---

### OWID – Global Meat Production

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