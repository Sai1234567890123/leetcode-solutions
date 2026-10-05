import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Use the .head() method to select the first N rows of a DataFrame.
    # When N=3, it returns the first 3 rows.
    # If the DataFrame has fewer than 3 rows, it will return all available rows.
    return employees.head(3)
