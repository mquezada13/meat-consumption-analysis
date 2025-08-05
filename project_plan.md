# 🌍 Project Plan – What Drives Meat Consumption?

## 🌟 Objective

Understand and predict meat consumption per capita across countries using socioeconomic and demographic data. Combine this with environmental metrics to visualize the global impact of meat-heavy diets.

---

## 🥉 Phase 1: Data Collection

### Target variable:
- Meat consumption per capita (kg/person/year)

### Predictive features (by country):
- GDP per capita
- Urban population (%)
- Education level (e.g. % tertiary education)
- Total calorie intake per person
- Food prices (if available)

### Environmental impact assessment (analytical component, not predictive):

- Use published environmental impact factors (e.g. kg CO₂, liters of water, m² of land per kg of food) to estimate national-level impact

- Combine with country-level meat consumption data to compute per capita environmental footprints

- This analysis is meant to inform and visualize—not predict—environmental consequences

---

## 🔗 Suggested Data Sources (Used in this Project)

### 🥩 Meat consumption data
- [FAO – Food Balance Sheets](https://www.fao.org/faostat/en/#data/FBS) (main target variable)

### 🌍 Socioeconomic indicators
- [World Bank Open Data](https://data.worldbank.org/) (main features)
  - GDP per capita (NY.GDP.PCAP.CD)  
  - Urban population (% of total) (SP.URB.TOTL.IN.ZS)
- [Our World in Data – Education](https://ourworldindata.org/education) (main feature)
  - Tertiary education enrollment (%), alternative to UNESCO

### 🔍 Additional analysis & visualization
- [Our World in Data – Meat and Environment](https://ourworldindata.org/environmental-impacts-of-food) (for environmental impact analysis)
- [Our World in Data – Global Meat Production](https://ourworldindata.org/grapher/global-meat-production?v=1&csvType=full&useColumnShortNames=false) (for context and trends)

### 🟡 Alternatives
- [Kaggle – Meat Consumption per Capita](https://www.kaggle.com/datasets/scibearia/meat-consumption-per-capita) (optional, pre-processed dataset)




---

## 🧪 Phase 2: Data Cleaning & Integration

- Inspect and compare meat consumption sources (FAO, Kaggle, OECD)
- Select and format the target variable
- Normalize country and year columns across all datasets
- Transform World Bank data to long format
- Merge all sources into a master dataset
- Save cleaned data in `/data/processed/`

---

## 📊 Phase 3: Exploratory Data Analysis (EDA)

- Global distribution of meat consumption
- Correlation heatmaps
- Scatter plots: GDP vs Meat Consumption, Urbanization vs Meat Consumption
- Identify outliers or special cases

---

## 🤖 Phase 4: Modeling

- Goal: Predict meat consumption per capita
- Algorithms: Random Forest, XGBoost, Ridge Regression
- Metrics: RMSE, MAE, R²

### Bonus:
- Feature importance (SHAP, Permutation)
- Country clustering by consumption patterns

---

## 🌎 Phase 5: Visualization & Communication

- Choropleth map (world) of meat consumption
- Barplots comparing countries
- Environmental impact plots (e.g. CO₂ vs meat intake)
- (Optional) Streamlit dashboard with filters

---

## 🗂️ To Do (Tracking)

- [x] Collect and organize all datasets  
- [ ] Inspect and compare target datasets (FAO, Kaggle, OECD)  
- [ ] Choose final dataset for target variable  
- [ ] Clean and transform predictors (GDP, education, urbanization)  
- [ ] Merge into single dataset  
- [ ] Run initial EDA  
- [ ] Train baseline model  
- [ ] Add visuals  
- [ ] Write README
