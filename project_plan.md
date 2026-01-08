# 🌍 Project Plan – What Drives Meat Consumption?

## Objective of project_plan.md

This document outlines the **conceptual structure and analytical flow** of the project.
It serves as a roadmap describing the reasoning behind each phase, from raw data
processing to final model interpretation.

The project is organized into **three main phases**:

- [1 – Data Processing](#1---data-processing)
- [2 – Exploratory Data Analysis](#2---data-exploration)
- [3 – Modeling, Evaluation & Interpretation](#3---data-modeling)

---

## 1 – Data Processing

### Data Collection

This project integrates real-world datasets from reputable public sources:

- [FAO – Food Balance Sheets](https://www.fao.org/faostat/en/#data/FBS)  
- [World Bank – GDP per capita](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)  
- [World Bank – Urban Population (%)](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS)  
- [OWID – Global Meat Production](https://ourworldindata.org/grapher/global-meat-production?v=1&csvType=full&useColumnShortNames=false)  
- [OWID – Education Data](https://ourworldindata.org/education)  

### Core Variables

- **Target variable**
  - Total meat consumption per capita (kg/person/year)

- **Candidate predictive features**
  - GDP per capita
  - Urban population (%)
  - Meat production (initially considered)
  - Additional socioeconomic indicators (as available)

Environmental impact indicators are considered **out of scope for prediction** and are
treated only as a potential descriptive extension.

---

### Data Cleaning & Integration

- Inspect and compare meat consumption sources
- Normalize country and year identifiers
- Transform World Bank datasets to long format
- Merge all sources into a unified master dataset
- Validate numerical consistency and missing values
- Save the cleaned dataset in `/data/processed/`

This phase produces a **single, analysis-ready dataset** used in all subsequent steps.

---

## 2 – Exploratory Data Analysis

The goal of this phase is to **understand structure, heterogeneity, and distributional
properties** of global per-capita meat consumption before any modeling.

EDA is explicitly used to **inform modeling decisions**, not merely to visualize data.

### Key Questions

- Which meat types dominate global per-capita consumption?
- How is total meat consumption distributed across countries?
- Which countries lie in the extreme high-consumption tail?
- Which countries represent the modal (most common) consumption range?
- How has global average meat consumption evolved over time?

---

### Methods

- Distributional analysis (histograms, density plots)
- Aggregation at country and year level
- Identification of modal ranges and extreme outliers
- Visual inspection of feature–target relationships

---

### Outcomes

This phase reveals that:
- Meat consumption is highly skewed across countries
- GDP per capita shows strong non-linear saturation effects
- Urban population exhibits a weaker, noisier relationship
- Production displays negligible explanatory structure

These findings directly motivate:
- log transformations
- exclusion of irrelevant features
- non-linear modeling strategies

---

## 3 – Modeling, Evaluation & Interpretation

The objective of this phase is to **quantify and explain** the relationship between
socioeconomic factors and per-capita meat consumption using progressively more
flexible models.

The focus is on **interpretability, robustness, and empirical justification** rather
than maximizing predictive performance alone.

---

### 3.1 Problem Definition

- **Task:** Supervised regression
- **Target variable:**  
  - Total meat consumption per capita  
  - Modeled in log space to reduce skewness
- **Final predictors:**  
  - GDP per capita  
  - Urban population (%)

Meat production is excluded based on EDA diagnostics.

---

### 3.2 Modeling Dataset

- Data are aggregated at the **country level**
- Values are averaged over the 2010–2022 period
- Each observation corresponds to one country

This approach:
- reduces temporal noise
- avoids leakage
- aligns with EDA findings

---

### 3.3 Modeling Strategy

Models are evaluated in increasing order of flexibility:

1. **Linear models**
   - Ordinary Least Squares
   - Ridge Regression
   - Lasso Regression

2. **Log-transformed models**
   - Same linear family, applied in log space

3. **Polynomial feature expansion**
   - Second-order terms to test curvature explicitly

4. **Tree-based model**
   - Random Forest Regressor

Each step is justified empirically and compared using consistent metrics.

---

### 3.4 Evaluation Metrics

Model performance is assessed using:
- R²
- RMSE
- MAE

Comparisons emphasize:
- generalization
- residual structure
- interpretability
- robustness to extreme values

---

### 3.5 Model Interpretation

The final model is interpreted using:
- residual diagnostics
- actual vs predicted plots with error bands
- partial dependence plots (1D and 2D)
- feature importance analysis

These tools are used to understand **how** and **why** predictors influence meat
consumption, not only whether predictions are accurate.

---

### 3.6 Expected Outcomes

At the end of this phase, the project delivers:
- a justified final predictive model
- empirical evidence for feature relevance
- clear documentation of modeling decisions
- a transparent narrative connecting EDA to modeling choices

The resulting model is intended as a **descriptive and predictive tool**, not a causal
estimator.
