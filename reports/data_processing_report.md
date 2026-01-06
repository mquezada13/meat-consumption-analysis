# 🧼 Data Harmonization Report (2010–2022)  
*Standardization and merging of raw meat consumption and socioeconomic datasets for modeling and visualization*

**Author:** Maura E. Ramirez-Quezada  
**Deliverable:** [`meat_processed_merged_data.csv`](Data/raw/meat_processed_merged_data.csv)  & [`meat_processed_merged_cleaned_data.csv`](Data/processed/meat_processed_merged_data.csv)
**Scope:** Standardization and merging of raw socioeconomic and consumption datasets for further modeling and visualization

---

## 🎯 Objective

This report summarizes the data processing stage of the project. The goal was to consolidate real-world datasets on meat consumption and socioeconomic indicators into a unified, time-aligned, and analysis-ready dataset. The resulting table will serve as the foundation for downstream modeling, exploratory analysis, and visualizations.

The codebase uses `pandas` with modular utilities (`data_loader.py`, `data_preprocessing.py`) to ensure reproducibility and consistent preprocessing across all sources.

---

## 📁 Datasets Processed

| Source     | File Name                                            | Raw Span    | Used Span   |
|------------|------------------------------------------------------|-------------|-------------|
| FAO        | `faostat_meat_kg_per_capita.csv`                    | 2010–2022   | 2010–2022    |
| World Bank | `worldbank_gdp_per_capita.csv`                      | 1960–2024   | 2010–2022    |
| World Bank | `worldbank_urban_population.csv`                    | 1960–2024   | 2010–2022    |
| OWID       | `global-meat-production.csv`                        | 1961–2023   | 2010–2022    |

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
| **Data types**          | `float64` (meat types), `int64` (`Year`), `object` (`Country`)                                           |

---

### 💰 World Bank – GDP per Capita

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | 266 countries × 70 columns (years from 1960 to 2024), wide format                                        |
| **Variables selected**  | Filtered to rows with  `Indicator Name == 'GDP per capita (current US$)'`                                                |
| **Filtering applied**   | Years filtered to 2010–2022 to ensure overlap with other datasets                                        |
| **Column renaming**     | Renamed: `Country Name → Country`, value column → `GDP_per_capita`                                       |
| **Transformation**      | Reshaped from wide to long format: `Country`, `Year`, `GDP_per_capita`                                   |
| **Final shape**         | 3,458 rows × 3 columns                                                                                   |
| **Missing data**        | None within selected time range                                                                          |
| **Data types**          | `object` (`Country`), `int64` (`Year`), `float64` (`GDP_per_capita`)                                     |

---

### 🏙️ World Bank – Urban Population (%)

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | 266 countries × 70 columns (years from 1960 to 2024), wide format                                        |
| **Variables selected**  | Filtered to rows with `Indicator Name == 'Urban population (% of total population)'`                                            |
| **Filtering applied**   | Years restricted to 2010–2022 to match range across datasets                                             |
| **Column renaming**     | Renamed: `Country Name → Country`, value column → `urban_population`                                     |
| **Transformation**      | Reshaped to long format with columns: `Country`, `Year`, `urban_population`                              |
| **Final shape**         | 3,458 rows × 3 columns                                                                                   |
| **Missing data**        | None within selected time range                                                                          |
| **Data types**          | `object` (`Country`), `int64` (`Year`), `float64` (`urban_population`)                                   |

---

### 🏭 OWID – Global Meat Production

| **Stage**               | **Description**                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------|
| **Raw shape**           | 14,614 rows × 4 columns                                                                                  |
| **Variables selected**  | Retained: `Entity`, `Year`, `Meat, total... tonnes`                                                      |
| **Filtering applied**   | Years filtered to 2010–2022 to ensure full overlap with other datasets                                   |
| **Column renaming**     | Renamed: `Entity → Country`, production column → `Production`                                            |
| **Transformation**      | No pivoting required; dataset already structured in long format                                          |
| **Final shape**         | 14,613 rows × 3 columns                                                                                  |
| **Missing data**        | No missing values detected in selected range                                                             |
| **Data types**          | `object` (`Country`), `int64` (`Year`), `float64` (`Production`)                                         |

---

## 🔗 Merging Strategy

- All datasets were harmonized to use `Country` (object) and `Year` (int) as merge keys.
- Country names were standardized using the `country_converter` library, supported by a custom dictionary for unresolved cases (e.g., `"USA"` → `"United States"`).
- Dataframes were verified for duplicates or inconsistent entries before merging.
- Merging was implemented sequentially using **inner joins** on `['Country', 'Year']` to ensure that all rows contain complete information across datasets.
- The merging logic was encapsulated in a function within `data_preprocessing.py`, which iteratively joins pairs of cleaned datasets into a unified master DataFrame.

---

## ✅ Final Output Summary

| Metric                    | Value                            |
|---------------------------|----------------------------------|
| Final dataset shape       | 2,609 rows × 9 columns           |
| Years covered             | 2010–2022                        |
| Countries included        | 187                              |
| Columns                   | `'Country'`, `'Year'`, `'Bovine Meat'`, `'Mutton & Goat Meat'`, `'Pigmeat'`, `'Poultry Meat'`, `'GDP_per_capita'`, `'urban_population'`, `'Production'` |
| Columns with missing data | `Pigmeat` only (46 source-level missing values) |
| Output file               | `Data/processed/meat_processed_merged_data.csv` |

---

---

## 🔍 Data Quality Assessment (DQA) & Cleaning Decisions

This section documents the main data quality issues identified after merging the datasets, along with the decisions taken to ensure the final table is suitable for analysis and modeling. The goal is to distinguish between (i) **true missingness** due to incomplete reporting and (ii) **structural missingness** where missing values reflect real-world constraints (e.g., cultural or geographic factors), not measurement error.

### Dataset Overview
- **Coverage:** 187 countries, 13 years (2010–2022)
- **Unit of analysis:** Country-year
- **Key variables:** meat consumption by type (kg/capita), GDP per capita, urbanization, total meat production

### 1) Structural Missingness in Meat-Type Consumption

#### Pigmeat: culturally restricted consumption
Missing values in the `Pigmeat` column are concentrated in countries where pork consumption is culturally restricted (e.g., predominantly Muslim countries). In these cases, missing values are likely to represent **structural zeros** rather than missing measurement.

- Countries flagged with missing `Pigmeat` values include:
  - Afghanistan, Kuwait, Mauritania, Pakistan, Saudi Arabia, Tunisia, United Arab Emirates

**Decision**
- These entries are treated as **structural zeros** (0 kg/capita) for modeling purposes, and this assumption is explicitly revisited during interpretation to avoid misleading conclusions.

#### Bovine Meat: geography-driven constraints (example case)
A missing value was identified for `Bovine Meat` in **Kiribati**, which is plausibly explained by geographic and logistical constraints that strongly shape dietary patterns (e.g., limited cattle production/availability, reliance on fish-based diets).

**Decision**
- Missingness consistent with geographic constraints is treated as **structural** and handled consistently with the modeling strategy (e.g., structural zeros where appropriate). The rationale is recorded to support transparent interpretation.

---

### 2) Missingness in Socioeconomic Indicators (data availability gaps)

#### GDP per capita missingness
- **Cuba** shows missing GDP per capita values for **2021–2022**.
- **South Sudan** shows missing GDP per capita values for **2019–2022**.

These gaps reduce the suitability of those country-year records for model training and evaluation, particularly since the project prioritizes avoiding heavy imputation for core predictors.

**Decisions**
- **Cuba:** records for 2021–2022 were removed (limited impact due to short gap).
- **South Sudan:** records with missing values were removed. If a country’s remaining coverage becomes insufficient for meaningful longitudinal analysis, it is excluded from modeling datasets to maintain consistency.

---

### 3) Consumption Distribution Groups (for readable analysis)

Due to the large number of countries, direct visualization across all country-year records can be difficult to interpret. For exploratory analysis and reporting, countries were also grouped into five broad consumption-level categories based on total meat consumption (kg/person/year):

1. Low  
2. Medium-low  
3. Medium  
4. High  
5. Extremely high  

This grouping is used strictly for interpretability in analysis and visualization, not as a modeling label.

**High-level observation (descriptive)**
Across all consumption groups, `Poultry Meat` tends to be the most widely consumed category, while `Mutton & Goat Meat` is consistently the least common. These patterns appear broadly stable over 2010–2022, with moderate shifts in prevalence depending on year and region.

---

### 4) Extremes in Total Consumption (sanity checks)

As a sanity check for plausibility and scale, the project also reviewed the highest- and lowest-consuming countries for the most recent year available (2022).

**Top 5 meat-consuming countries in 2022 (kg/person/year)**
- Tonga (147.51)
- Israel (113.18)
- Argentina (112.08)
- Australia (111.40)
- Mongolia (108.47)

**Bottom 5 meat-consuming countries in 2022 (kg/person/year)**
- Burundi (3.63)
- Bangladesh (4.25)
- Rwanda (4.97)
- Madagascar (5.21)
- Niger (5.25)

These checks are not used to draw causal conclusions, but to confirm the target variable range and identify potential outliers for robust modeling choices (e.g., transformations or robust metrics).

---

### Summary of DQA Decisions
- Distinguished **structural missingness** (e.g., culturally restricted consumption) from incomplete reporting.
- Avoided heavy imputation for core predictors; removed limited missing country-year records where necessary.
- Documented edge cases (e.g., geography-driven constraints) to support transparent interpretation.
- Added consumption-level grouping to support readable exploratory analysis.

---


## 🧭 Notes

- All data processing was performed using `pandas`, and data loading/merging was modularized via `data_loader.py` and `data_preprocessing.py`.
- Column names were standardized across all datasets before merging.
- No feature scaling, outlier removal, or imputation was performed at this stage.
- All numerical columns were validated for consistency over the 2010–2022 period.
- This dataset is now ready for exploratory analysis, modeling pipelines, or dashboard visualizations.
