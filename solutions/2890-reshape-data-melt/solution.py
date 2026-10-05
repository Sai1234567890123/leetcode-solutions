import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the DataFrame from wide to long format using pandas.melt.
    
    Parameters:
        report (pd.DataFrame): DataFrame containing product quarterly sales.
        
    Returns:
        pd.DataFrame: Reshaped DataFrame with columns ['product', 'quarter', 'sales'].
    """
    return report.melt(
        id_vars=['product'],
        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name='quarter',
        value_name='sales'
    )
