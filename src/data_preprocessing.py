import pandas as pd
import country_converter as coco

def standardize_country_names(df, country_col='Country', manual_dict=None, return_unmatched=False):
    """
    Standardizes country names using the country_converter library and a manual dictionary of exceptions.

    Parameters:
    - df: pandas DataFrame
    - country_col: name of the column containing country names
    - manual_dict: optional dictionary with manual name mappings
    - return_unmatched: if True, returns unmatched names after conversion

    Returns:
    - df: DataFrame with standardized country names in the same column
    - unmatched (optional): set of names not matched by coco
    """

    # Step 1: Use country_converter
    df = df.copy()
    df[country_col] = coco.convert(names=df[country_col].tolist(), to='name_short')

    # Step 2: Apply manual corrections
    if manual_dict:
        df[country_col] = df[country_col].replace(manual_dict)

    return df



def comparing_name_country(dataset1, dataset2, colname='Country', name1='Dataset1', name2='Dataset2'):
    """
    Compares country names between two datasets and returns which countries are missing from the second one.

    Parameters:
    - dataset1, dataset2: pandas DataFrames to compare
    - colname: name of the column containing country names (default is 'Country')
    - name1, name2: labels for dataset1 and dataset2 to use in the printed output

    Returns:
    - missing_names: set of country names that are in dataset1 but not in dataset2
    """

    def clean_column(col):
        return col.apply(lambda x: x[0] if isinstance(x, list) else x)

    # Make sure the column has only hashable values 
    dataset1 = dataset1.copy()
    dataset2 = dataset2.copy()
    dataset1[colname] = clean_column(dataset1[colname])
    dataset2[colname] = clean_column(dataset2[colname])

    # Extract unique country names
    d1 = set(dataset1[colname].unique())
    d2 = set(dataset2[colname].unique())

    # Compute difference
    missing_names = d1 - d2

    print(f"\n{name1} countries not in {name2} ({len(missing_names)}):")
    print(missing_names)

    return missing_names



# Merging function
def mergingfunc(dataset1, dataset2, colname='Country'):

    def clean_column(col):
        return col.apply(lambda x: x[0] if isinstance(x, list) else x)

    # Make sure the column has only hashable values 
    dataset1 = dataset1.copy()
    dataset2 = dataset2.copy()
    dataset1[colname] = clean_column(dataset1[colname])
    dataset2[colname] = clean_column(dataset2[colname])

    merged = pd.merge(dataset1, dataset2, on=['Country', 'Year'], how='inner')
    return merged
