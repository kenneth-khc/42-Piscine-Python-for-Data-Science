import pandas as pd
from pandas import DataFrame
from pandas.errors import EmptyDataError


def load(path: str) -> DataFrame:
    """Loads .csv into a DataFrame, writes its dimensions and returns it"""
    try:
        df = pd.read_csv(path)

    except (FileNotFoundError, EmptyDataError, PermissionError) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)

    except Exception as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)

    else:
        print(f"Loading dataset of dimensions {df.shape}")
        return df
