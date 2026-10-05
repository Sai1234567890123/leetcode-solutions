import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column named 'bonus'
    # This column's values are calculated by taking the 'salary' column
    # and multiplying each element by 2.
    # Pandas automatically handles this as a vectorized operation,
    # applying the multiplication to every row efficiently.
    employees['bonus'] = employees['salary'] * 2
    
    # Return the modified DataFrame which now includes the 'bonus' column.
    return employees
