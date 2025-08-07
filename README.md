<p align="left">
<img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>

***
 #  🌿 What Drives Meat Consumption?
***

## Table of Contents
- [Motivation](#motivation)
- [Introduction](#introduction)
- [Repository Structure](#repository-structure)
- [Project Phases](#project-phases)
- [Suggested Data Sources](#suggested-data-sources)

## Motivation

As a vegetarian deeply interested in data-driven decision-making, I often encounter questions about the real impact of dietary choices on health, the environment, and society. Motivated by this, I decided to use real-world data and machine learning to investigate a fundamental question:

**What drives meat consumption across countries and populations?**

This project combines domain curiosity with technical skills to explore consumption patterns and build predictive models — aiming to contribute both to public understanding and to practical data science development.
## Introduction
The meat industry has a significant impact on public health, the environment, and global food systems. This project explores meat consumption patterns across different countries and regions using real-world data. The goal is to understand what drives meat consumption and build predictive models to forecast future trends, while also analyzing the environmental footprint. 

## Repository Structure
The folder structure of this project is summarized below.  

meat-conssuption-analysis:
    README.md
    project_plan.md
    requirements.txt
    notebooks/
        01_data_processing.ipynb
        02_data_exploration.ipynb
        03_model_training.ipynb
        04_visualizations.ipynb
    Data/
        raw/
            faostat_meat_kg_per_capita.csv
            worldbank_gdp_per_capita.csv
            worldbank_urban_population.csv
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

For a more detailed plan of each step and script used, refer to [`project_plan.md`](project_plan.md).

## Project Phases

This project is structured in four main phases:

1. **Data Processing**
***
- Initial inspection and cleaning of the input datasets found in [`Data/raw`](/Data/raw/).
- Merging features and defining the target variable.
- Final processed dataset is stored in [`Data/processed`](Data/processed).

📓 Notebooks:
- [`01_data_processing.ipynb`](notebooks/01_data_exploration.ipynb)

📦 Modules:
- [`data_loader.py`](src/data_loader.py)
- [`data_processing.py`](src/data_preprocessing.py)

>  *Users interested in practicing full data  cleaning and processing are encouraged to go through these notebooks. Otherwise, the processed data is ready to use.*
***



2. **Data processing**
3. **Data Modelling** 
4. **Visualization**


## 📄 Reports

- [Data Processing Report](reports/processing_report.md)

## Suggested Data Sources
This project analyzes meat consumption per capita using global datasets from FAOSTAT, the World Bank, and Our World in Data (OWID). Variables include GDP, urbanization, education, environmental impact, and meat production.

### 🥩 Meat Consumption Data
- [FAO – Food Balance Sheets](https://www.fao.org/faostat/en/#data/FBS)  
  *Main target variable: annual meat consumption (kg per capita)*

### 🌍 Socioeconomic Indicators
- [World Bank – GDP per capita](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)  
- [World Bank – Urban Population (%)](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS)  
- [OWID – Global Meat Production](https://ourworldindata.org/grapher/global-meat-production?v=1&csvType=full&useColumnShortNames=false)  

### 🌱 Environmental & Educational Context
- [OWID – Environmental Impact of Food](https://ourworldindata.org/environmental-impacts-of-food)  
- [OWID – Education Data](https://ourworldindata.org/education)  

### 🟡 Optional / Alternative Sources
- [Kaggle – Meat Consumption per Capita](https://www.kaggle.com/datasets/scibearia/meat-consumption-per-capita)  
  *Optional pre-processed dataset for quick prototyping*
## Additional Information
**Author:** Maura E. Ramirez-Quezada

**Contact** elizza.rmz91@gmail.com
