import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Pivots the weather DataFrame so that each row represents a month,
    and each unique city becomes a column with temperature values.
    """
    # Use pandas pivot method:
    # - index: column to become the new DataFrame's index (rows)
    # - columns: column to be reshaped into new column headers
    # - values: column to populate the cell values
    return weather.pivot(index='month', columns='city', values='temperature')
