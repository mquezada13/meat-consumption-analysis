# 🌍 Project Plan – What Drives Meat Consumption?

## Objective of project_plan.md
To visualize a map of the general structure of our project. 
Three main phases are fully specified in this section

- [1 – Data Processing](#1---data-processing)
- [2 - Data Exploration](#2---data-exploration)
- [3 – Data Modeling](#3---data-modeling)
- [4 - Visualization]



##  1 - Data Processing
### Data Collection

This project integrates real-world datasets from reputable sources, including:

  * [FAO – Food Balance Sheets](https://www.fao.org/faostat/en/#data/FBS)  
  * [World Bank – GDP per capita](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)  
  * [World Bank – Urban Population (%)](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS) 
  * [OWID – Global Meat Production](https://ourworldindata.org/grapher/global-meat-production?v=1&csvType=full&useColumnShortNames=false) 
  * [OWID – Environmental Impact of Food](https://ourworldindata.org/environmental-impacts-of-food)  
  * [OWID – Education Data](https://ourworldindata.org/education)  

**Key features of interest are:**

- **Target variable:**
  - Meat consumption per capita (kg/person/year)
- **Predictive features (by country):**
  - GDP per capita
  - Urban population (%)
  - Total calorie intake per person
  - Food prices (if available)
  - Meat production
  - Basic education
- **Environmental impact assessment (analytical component, not predictive):**
  - Use published environmental impact factors (e.g. kg CO₂, liters of water, m² of land per kg of food) to estimate national-level impact
  - Combine with country-level education data to compute per capita environmental footprints
  - This analysis is meant to inform and visualize,  not predict—environmental consequences

###  Data Cleaning & Integration
- Inspect and compare meat consumption sources (FAO, World Bank, OWID)
- Select and format the target variable
- Normalize country and year columns across all datasets
- Transform World Bank data to long format
- Merge all sources into a master dataset
- **Save cleaned data in** [`/data/processed/`](data/processed/)

## 2 - Data Exploration

The goal of this phase is to understand the structure, distribution, and heterogeneity
of global per-capita meat consumption before any predictive modeling.

This stage focuses on identifying dominant consumption patterns, variability across
countries, and potential outliers that may influence downstream modeling decisions.

### Key questions addressed:
- Which meat types dominate global per-capita consumption?
- How is meat consumption distributed across countries?
- Which countries lie in the extreme high-consumption tail?
- Which countries represent the modal (most common) consumption range?
- How has global average meat consumption evolved over time?

### Methods:
- Univariate and multivariate visualizations (histograms, line plots)
- Distributional analysis of per-capita consumption
- Identification of modal ranges and extreme outliers
- Descriptive statistics aggregated by country and year

### Outcome:
This phase informs feature selection, transformation choices, and robustness strategies
for the modeling stage, ensuring that predictive models are not driven by extreme or
unrepresentative observations.


## 3 – Data Modeling

The objective of this phase is to quantify the relationship between socioeconomic
factors and per-capita meat consumption across countries using interpretable
and well-established regression techniques.

This modeling phase intentionally relies on foundational methods to ensure
transparency, robustness, and clear interpretability, rather than maximizing
predictive performance.

---

### 3.1 Problem Definition

- **Task:** Supervised regression  
- **Target variable:**  
  - Total meat consumption per capita (kg/person/year)
- **Predictor variables:**  
  - GDP per capita  
  - Urban population (%)  
  - Meat production  
  - Additional socioeconomic features as available

The modeling task focuses on explaining cross-country differences in meat
consumption rather than forecasting future values.

---

### 3.2 Modeling Dataset

- Data will be aggregated at the **country level** by averaging values over
  the 2010–2022 period.
- Each observation corresponds to a single country.
- This approach reduces temporal noise and avoids information leakage while
  remaining consistent with insights obtained during the exploratory analysis.

---

### 3.3 Modeling Strategy

The following models will be evaluated:

1. **Baseline model**
   - Ordinary Least Squares (Linear Regression)

2. **Regularized linear models**
   - Ridge Regression
   - Lasso Regression

These models allow for direct interpretation of coefficients and assessment of
feature relevance.

---

### 3.4 Key Considerations

- The target variable exhibits strong skewness and heterogeneity across countries.
- Extreme high-consuming countries (e.g. Tonga) will be retained but analyzed
  separately to assess their influence on model stability.
- Model performance will be evaluated both including and excluding extreme outliers
  as a robustness check.

---

### 3.5 Evaluation Metrics

Model performance will be assessed using:
- R² (coefficient of determination)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

Comparisons across models will focus on both predictive accuracy and stability
of learned relationships.

---

### 3.6 Expected Outcomes

At the end of this phase, the analysis will:
- Identify which socioeconomic variables are most strongly associated with
  per-capita meat consumption
- Quantify the explanatory power of linear models
- Assess the impact of extreme outliers on model results
- Provide a transparent and interpretable baseline for potential future extensions






