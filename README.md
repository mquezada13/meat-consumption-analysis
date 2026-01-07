<p align="left">
<img src="https://img.shields.io/badge/STATUS-IN%20DEVELOPMENT-green">
</p>

# 🌿 What Drives Meat Consumption?

## Overview

This project investigates **what drives meat consumption per capita across countries** using real-world socioeconomic and environmental data.  
The primary goal is to **build interpretable predictive models** that explain cross-country variation in meat consumption, while maintaining a strong focus on analytical reasoning, model evaluation, and clear communication.

The project is designed as a **professional data science case study**, emphasizing decision-making over purely descriptive analysis.

---

## Motivation

As a vegetarian interested in data-driven decision-making, I frequently encounter claims about the impact of dietary choices on health, the environment, and society. This project approaches the topic from a **descriptive and predictive perspective**, without normative judgments, using data to understand *patterns* rather than to advocate for specific behaviors.

The objective is twofold:
- To explore and model meat consumption patterns across countries.
- To demonstrate applied data analysis and machine learning skills using real, imperfect datasets.

---

## Research Questions

The project is organized around the following core questions:

1. **Can meat consumption per capita be predicted using socioeconomic indicators?**
2. **Which factors explain most of the variation across countries?**
3. **How interpretable are different modeling approaches in this context?**
4. *(Extension)* Do higher predicted consumption levels correlate with higher environmental impact?

---

## Repository Structure

The folder structure of this project is summarized below.  
***

meat-conssuption-analysis/

    README.md

    project_plan.md

    requirements.txt

    notebooks/

        01_data_processing.ipynb

        02_data_exploration.ipynb

        03_data_modeling.ipynb

        04_visualizations.ipynb

    Data/

        raw/

            faostat_meat_kg_per_capita.csv

            worldbank_gdp_per_capita.csv

            worldbank_urban_population.csv

            share-of-the-world-population-with-at-least-basic-education.csv

            food_enviroment_impact.csv

            global-meat-production.csv

        processed/

            meat_processed_merged_data.csv

    src/

        data_preprocessing.py

        model_utils.py

        visualization.py

        data_loader.py

    reports/

        data_eprocessing_report.md

***
For a detailed step-by-step plan, see [`project_plan.md`](project_plan.md).

---

## Project Phases

### 1. Data Processing
- Cleaning and harmonizing country-level datasets.
- Feature selection and target definition.
- Final merged dataset stored in `data/processed/`.

📓 Notebook:
- `01_data_processing.ipynb`

📦 Modules:
- `data_loader.py`
- `data_preprocessing.py`

---

### 2. Exploratory Data Analysis
- Examination of feature distributions and outliers.
- Analysis of relationships between meat consumption and socioeconomic indicators.
- Identification of modeling implications (e.g. non-linearity, scaling, collinearity).

📓 Notebook:
- `02_data_exploration.ipynb`

This phase explicitly informs **model selection and feature engineering**, rather than serving as descriptive visualization only.

---

### 3. Predictive Modeling *(in progress)*
- Supervised regression models to predict meat consumption per capita.
- Baseline models (e.g. linear regression) and more flexible approaches (e.g. regularized models, tree-based methods).
- Model evaluation using appropriate metrics (RMSE, R²).
- Emphasis on **interpretability and generalization**, not leaderboard optimization.

📓 Notebook:
- `03_model_training.ipynb`

---

### 4. Interpretation & Visualization *(planned)*
- Feature importance and model explainability.
- Comparative analysis across regions.
- Clear visual communication of results.

📓 Notebook:
- `04_visualizations.ipynb`

---

## Data Sources

This project uses publicly available global datasets:

### 🥩 Meat Consumption
- FAOSTAT – Food Balance Sheets  
  *Annual meat consumption (kg per capita)*

### 🌍 Socioeconomic Indicators
- World Bank – GDP per capita  
- World Bank – Urban population (%)
- Our World in Data – Education indicators
- Our World in Data – Global meat production

### 🌱 Environmental Context *(extension)*
- Our World in Data – Environmental impacts of food production

---

## Scope and Limitations

- This project focuses on **prediction and explanation**, not causal inference.
- Country-level aggregation limits individual-level conclusions.
- Environmental analysis is treated as a correlational extension.

---

## Author

**Maura E. Ramirez-Quezada**

Contact: elizza.rmz91@gmail.com
