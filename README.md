<p align="left">
<img src="https://img.shields.io/badge/STATUS-V1%20DONE%20%F0%9F%8C%BF-purple">
</p>

# 🌿 What Drives Meat Consumption?

## Overview

This project investigates **what drives per-capita meat consumption across countries** using real-world socioeconomic data.  
The objective is to **build interpretable predictive models** that explain cross-country variation in meat consumption, with a strong emphasis on analytical reasoning, model diagnostics, and transparent decision-making.

The project is structured as a **professional end-to-end data science case study**, prioritizing model justification and interpretability over purely descriptive analysis or performance chasing.

---

## Motivation

As a vegetarian interested in data-driven reasoning, I frequently encounter claims regarding the impact of dietary choices on health, the environment, and society.  
This project approaches the topic from a **descriptive and predictive perspective**, without normative judgments, using data to understand *structural patterns* rather than to promote specific behaviors.

The goals are:
- To identify which socioeconomic factors explain most of the variation in meat consumption across countries.
- To demonstrate applied data science skills using real, imperfect, multi-source datasets.

---

## Research Questions

The analysis is organized around the following questions:

1. **Can per-capita meat consumption be predicted using country-level socioeconomic indicators?**
2. **Which variables explain most of the cross-country variation?**
3. **How do linear and non-linear models compare in terms of performance and interpretability?**
4. *(Optional extension)* How do predicted consumption levels relate to environmental impact metrics?

---

## Repository Structure



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

            data_loader.py

        reports/

            data_processing_report.md

            data_modeling_report.md

            data_exploration_report.md

***

For a detailed step-by-step plan, see [`project_plan.md`](project_plan.md).

---

## Project Phases

### 1. Data Processing
- Cleaning, harmonizing, and merging multiple country-level datasets.
- Feature selection and target construction.
- Final dataset stored in `data/processed/`.

📓 Notebook:
- `01_data_processing.ipynb`

📦 Modules:
- `data_loader.py`
- `data_preprocessing.py`

---

### 2. Exploratory Data Analysis
- Distributional analysis and outlier detection.
- Feature–target relationship inspection.
- Identification of non-linearity, saturation effects, and scale issues.

📓 Notebook:
- `02_data_exploration.ipynb`

EDA is used explicitly to **inform modeling choices**, not only for visualization.

---

### 3. Modeling, Evaluation, and Interpretation
- Linear, regularized, polynomial, and tree-based models.
- Log-transformed target to address skewness and heteroscedasticity.
- Cross-validation and residual diagnostics.
- Model comparison based on performance *and* interpretability.

**Visualization & Communication**

- Diagnostic plots (actual vs predicted, residuals).
- Partial Dependence Plots (PDPs).
- Feature importance analysis.
- Clear narrative linking EDA, modeling decisions, and results.

📓 Notebook:
- `03_data_modeling.ipynb`

📄 Report:
- `reports/modeling_report.md`

**Final model:** Random Forest Regressor  
Selected due to its ability to capture non-linear saturation effects and feature interactions.

---

## Key Findings

- **GDP per capita** is the dominant driver of per-capita meat consumption, exhibiting strong non-linear saturation.
- **Urban population** plays a secondary, context-dependent role.
- **Production** shows negligible explanatory power and is excluded.
- Linear models fail structurally; log-transformed models improve but remain limited.
- Random Forest models capture non-linearities and interactions effectively.

---

## Scope and Limitations

- Country-level aggregation masks within-country heterogeneity.
- No causal interpretation is claimed.
- Results should be interpreted as **descriptive and predictive**, not causal.

---

## Possible Extensions

- Environmental impact modeling
- Population-weighted targets
- Additional socioeconomic indicators (education, prices, dietary composition)

These are intentionally left as **optional extensions**, not part of the core analysis.

---

## Author

**Maura E. Ramirez-Quezada**  
Contact: elizza.rmz91@gmail.com
