# utils/data_loader.py

import os
import pandas as pd

def load_raw_data(data_dir='../Data/raw'):
    """
    Loads all raw datasets into a dictionary of pandas DataFrames.

    Parameters:
    - data_dir: path to the directory where raw .csv files are stored.

    Returns:
    - dict: dictionary of DataFrames, with keys like 'faostat', 'gdp', etc.
    """
# file dictionary
    files = {
        'faostat': os.path.join(data_dir,'faostat_meat_kg_per_capita.csv'),
        'gdp': os.path.join(data_dir,'worldbank_gdp_per_capita.csv'),
        'urban':os.path.join(data_dir,'worldbank_urban_population.csv'),
        'education':os.path.join(data_dir,'share-of-the-world-population-with-at-least-basic-education.csv'),
        'enviroment':os.path.join(data_dir,'food_enviroment_impact.csv'),
        'production':os.path.join(data_dir,'global-meat-production.csv')
    }

    #l configuration dictionary
    config = {
        'faostat': {},
        'gdp': {'header':2},
        'urban':{'header':2},
        'education':{},
        'enviroment':{},
        'production':{}
        }

    dfs = {
        key: pd.read_csv(path, **config.get(key, {}))
        for key, path in files.items()
    }

    return dfs


# Loading the processed data

def load_processed_data(path='../Data/processed/meat_processed_merged_data.csv'):
    return pd.read_csv(path, header =1)
