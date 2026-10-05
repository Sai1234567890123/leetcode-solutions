import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate the two DataFrames vertically (stacking rows).
    # axis=0 specifies vertical concatenation (along rows).
    # ignore_index=True resets the index of the resulting DataFrame to a default integer index (0, 1, 2, ...),
    # which is often desired when combining tables and prevents duplicate index values from the original DataFrames.
    result_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    return result_df
