import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Directly multiply the 'salary' column by 2.
    # Pandas Series operations are vectorized, which means this operation
    # is applied to all elements of the 'salary' column efficiently
    # without explicit looping in Python.
    employees['salary'] = employees['salary'] * 2
    
    # Return the modified DataFrame.
    return employees
