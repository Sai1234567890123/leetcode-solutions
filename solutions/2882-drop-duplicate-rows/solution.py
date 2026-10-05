import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicate rows based on the 'email' column, keeping the first occurrence.
    
    :param customers: pd.DataFrame containing customer details.
    :return: pd.DataFrame with duplicate emails removed.
    """
    # drop_duplicates with subset=['email'] identifies duplicates strictly on the email column.
    # keep='first' ensures that the first occurrence is retained (default behavior).
    return customers.drop_duplicates(subset=['email'], keep='first')
