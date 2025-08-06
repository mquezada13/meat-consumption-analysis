# 🌿 What Drives Meat Consumption?
**Project in progress**

**Author:** Maura E. Ramirez-Quezada
**Status:** In development
**Libraries:** pandas, numpy, matplotlib, pycountry*(to be expanded)*

--
## Project description
The meat industry has a significant impact on public health, the environment, and global food systems. This project explores meat consumption patterns across different countries and regions using real-world data. The goal is to understand what drives meat consumption and build predictive models to forecast future trends, while also analyzing the environmental footprint.

## Repository structure
For a detailed plan of the project, see [`project_plan.md`](project_plan.md).  
The datasets and file structure used in the code are outlined here for clarity and reproducibility:


meat-conssuption-analysis:
    README.md
    project_plan.ms
    requirements.txt
    notebooks/
        01_data_exploration.ipynb
        02_model_training.ipynb
        03_visualizations.ipynb
    Data/
        raw/
            faostat_meat_kg_per_capita.csv
            worldbank_gdp_per_capita.csv
            worldbank_urban_population.csv'
            share-of-the-world-population-with-at-least-basic-education.csv'
            food_enviroment_impact.csv
            global-meat-production.csv
        processed/
            meat_processed_merged_data.csv
    src/
        data_preprocessing.py
        model_utils.py
        visualization.py
        data_loader.py




The proyect is structured in three main phasess:
- **Block 1 – Data Exploration**  
  Initial inspection, cleaning, and analysis of all input datasets.  
  Includes unification of input features and definition of the target variable. 
  Notebook: - [`01_data_exploration.ipynb`](notebooks/01_data_exploration.ipynb)
  Modules: `data_loader.py` and `data_processing.py`

- **Block 2 – Model Training**  
  Building a machine learning model to predict meat consumption.  
  Notebook: `02_model_training.ipynb`

- **Block 3 – Visualizations**  
  Presenting key results and visual insights through interactive or static plots.  
  Notebook: `03_visualizations.ipynb`


### Block 1 – Data Exploration/processing

In this notebook, we load and explore the raw datasets related to global meat consumption.  
The goal is to understand the structure, completeness, and key variables of each dataset.  
We also identify necessary preprocessing steps and visualize the available data to guide the next stages of analysis.

**Full notebook:** [01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)

---

#### FAOSTAT Dataset
- Covers meat consumption (kg per capita per year) in ~190 countries from 2010 to 2022.
- Includes five meat types (bovine, pigmeat, poultry, etc.).
- Filtered rows by `Element = "Food supply quantity (kg/capita/yr)"`.
- Excluded `"Meat, Other"` category.

#### GDP Dataset
- **GDP per capita** (Gross Domestic Product per person) is used as a proxy for average income levels.
- Covers 266 countries from 1960 to 2024.
- Selected data from `2010` to `2022` only.
- Dropped irrelevant column `Unnamed: 69`.

#### Urban Population Dataset
- **Urban population (%)** represents the share of people living in urban areas.
- Used to evaluate whether urbanization correlates with meat consumption.
- Covers 266 countries from 1960 to 2024.
- Selected data from `2010` to `2022` only.
- Dropped column `Unnamed: 69`.

#### Education Dataset
- Shows the share of population with basic education in 25 countries from 1820 to 2100.
- All features are retained for analysis and visualization.

#### Environmental Impact Dataset
- Provides GHG emissions (kg CO₂e per kg of product) by food type in the year 2010.
- This dataset is optional and used only for impact visualization.
- All entries are usable if included.

#### Meat Production Dataset
- Displays annual meat production for 254 countries from 1961 to 2023.
- Optional for visualizing production trends or global meat supply.
- All entries are retained if used.
### Data processing
