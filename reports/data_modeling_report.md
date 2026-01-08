# 🌍 Modeling Drivers of Per-Capita Meat Consumption

## Phase 3 — Modeling, Evaluation, and Interpretation

This section presents the full modeling workflow used to predict **per-capita total meat consumption** at the country level.  
All modeling decisions are explicitly motivated by exploratory diagnostics and empirical performance, not by model preference.

---

## 3.1 Modeling Objective

The goal is to model **average per-capita total meat consumption** using country-level socioeconomic indicators.

### Target
- `total_meat`: sum of bovine, pig, poultry, and mutton & goat meat (kg/capita/year)
- Modeled in **log space** to reduce skewness and heteroscedasticity

### Candidate Features
- GDP per capita  
- Urban population share (%)  
- Production (initially considered, later excluded)

All features are averaged at the **country level (2010–2022)** to focus on structural differences rather than year-to-year fluctuations.

---

## 3.2 Feature Diagnostics and Selection

### Correlation Screening

Initial correlation analysis shows:

- GDP per capita: moderate positive correlation with meat consumption  
- Urban population: similar magnitude, but noisier  
- Production: **very weak correlation**

### Raw Feature–Target Relationships

![GDP-Urban Population - Production vs Total Meat Consumption](../figures/features_vs_meat_raw.png)  

**Key observations**

- **GDP per capita** shows a clear non-linear, saturating relationship  
- **Urban population** shows a positive but highly dispersed trend  
- **Production** exhibits a degenerate distribution and no meaningful structure

### Decision: Exclude Production

Production is excluded from all baseline and final models due to:
- negligible correlation
- extreme scale imbalance
- lack of conceptual alignment with per-capita consumption
- risk of injecting background noise

This decision is data-driven and visually justified.

---

## 3.3 Baseline Linear Models (Raw Scale)

Linear, Ridge, and Lasso regressions are trained using raw features.

### Performance Summary (Raw Target)

| Model | R² | MSE | MAE |
|------|----|-----|-----|
| Linear | < 0 | High | High |
| Ridge | < 0 | High | High |
| Lasso | < 0 | High | High |

### Diagnostic Plots

![Linear / Ridge / Lasso: Actual vs Predicted](../figures/linear_raw_actual_vs_predicted.png)

**Conclusion**

All linear models severely underfit:
- predictions collapse toward the mean
- strong underestimation at high consumption
- clear violation of linear assumptions

These failures are structural, not implementation errors.

---

## 3.4 Log-Transformed Feature Space

To better align with linear assumptions, log transformations are applied:

- `log_total_meat = log1p(total_meat)`
- `log_GDP_per_capita = log1p(GDP_per_capita)`

Urban population is kept in linear scale.

![Log GDP vs Log Total Meat Consumption](../figures/log_gdp_vs_log_meat.png)

Log transformation:
- reduces skewness
- stabilizes variance
- improves monotonicity

---

## 3.5 Linear Models (Log Target)

Linear, Ridge, and Lasso models are retrained in log space.

### Performance Summary (Log Target)

| Model | R² | MSE | MAE |
|------|----|-----|-----|
| Linear | ~0.63 | ↓ | ↓ |
| Ridge | ~0.63 | ↓ | ↓ |
| Lasso | ~0.59 | ↓ | ↓ |

![Linear / Ridge / Lasso (Log Target): Actual vs Predicted](../figures/linear_log_actual_vs_predicted.png)

**Interpretation**

- Log transformation substantially improves performance
- However, residual structure remains non-random
- Linear models still cannot capture saturation effects

---

## 3.6 Polynomial Feature Expansion

Second-order polynomial features are tested to model curvature explicitly.

![Polynomial Fit: Log GDP vs Log Total Meat](../figures/poly_log_gdp.png)  
![Polynomial Fit: Urban Population vs Log Total Meat](../figures/poly_urban.png)

### Results

| Model | R² (Poly) |
|------|-----------|
| Linear | ~0.62 |
| Ridge | ~0.62 |
| Lasso | ~0.59 |

Cross-validation confirms **no systematic improvement** over the log-linear case.

### Conclusion

Polynomial expansion does not meaningfully enhance predictive power.  
The remaining structure is not well captured by global parametric forms.

---

## 3.7 Random Forest Model

A **Random Forest Regressor** is trained using:
- `log_GDP_per_capita`
- `Urban_population`
- `log_total_meat` as target

No feature scaling is required.

### Performance

| Metric | Value |
|------|------|
| R² | ~0.71 |
| MSE | ↓ |
| MAE | ↓ |

![Random Forest: Actual vs Predicted](../figures/rf_actual_vs_predicted.png)

**Single-Feature Random Forest Diagnostics**

To assess marginal explanatory power, Random Forest models were trained on individual predictors.
GDP alone captures the dominant saturation structure. Urban population alone yields weaker, noisier predictions, confirming its secondary role.

![GDP per Capita vs total meat](../figures/pdp_gdp.png)
![Urban population vs total meat ](../figures/pdp_urban.png)
---

## 3.8 Model Diagnostics

### Residual Analysis

![Random Forest: Residuals vs Predicted](../figures/rf_residuals.png)

Residuals:
- centered around zero
- no strong systematic trends
- mild heteroscedasticity at extremes

### Robust Error Band

![Random Forest: Actual vs Predicted with Error Band](../figures/rf_actual_vs_predicted_band.png)

The P10–P90 residual band shows:
- stable predictive uncertainty
- increasing dispersion only at extreme values

---

## 3.9 Partial Dependence Analysis

### Individual Effects

![PDP: GDP per Capita (left), Urban Population (right)](../figures/pdp_gdp_urban.png)

**GDP**
- strong non-linear increase
- rapid growth at low income
- clear saturation at high income


**Urban population**
- weaker effect
- non-monotonic
- diminishing influence at high urbanization

### Joint Effects


![2D PDP: GDP × Urban Population](../figures/pdp_2d.png)

GDP per capita dominates across the full range.  
Urban population acts as a **secondary, conditional modifier**, mainly at intermediate GDP levels.

---

## 3.10 Feature Importance

![Random Forest Feature Importance](../figures/rf_feature_importance.png)

- GDP per capita: dominant contributor  
- Urban population: secondary but non-negligible  

This is fully consistent with EDA, PDPs, and model diagnostics.

---

## 3.11 Modeling Summary

- Raw linear models fail due to non-linearity and saturation
- Log transformation improves performance but does not eliminate structural bias
- Polynomial expansion yields no systematic gains
- Random Forest captures non-linearities and interactions effectively
- GDP per capita is the primary driver of per-capita meat consumption
- Urban population plays a secondary, context-dependent role
- Production is empirically irrelevant and excluded

---

## 3.12 Limitations and Outlook

- Country-level averages mask within-country inequality
- No causal interpretation is claimed
- Future extensions may include:
  - education levels
  - food prices
  - dietary composition
  - population-weighted targets

The current model is best interpreted as a **descriptive and predictive tool**, not a causal estimator.
