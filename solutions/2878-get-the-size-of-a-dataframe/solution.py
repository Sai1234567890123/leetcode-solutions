import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    """
    Returns the number of rows and columns of the input DataFrame as a list [rows, columns].
    
    `players.shape` returns a tuple (n_rows, n_columns) in O(1) time.
    We convert this tuple directly to a list to match the return type specification.
    """
    return list(players.shape)
