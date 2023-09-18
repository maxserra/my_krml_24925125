import pandas as pd

def convert_to_date(df, cols: list):
    """Convert specified columns cols from df into datetime. This is an inplace operation.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    cols : list
        List of columns to be converted

    Returns
    -------
    pd.DataFrame
        Pandas dataframe with converted columns
    """

    for col in cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])
    return df