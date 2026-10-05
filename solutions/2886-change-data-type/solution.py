import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Cast the 'grade' column from float to standard integer type
    students['grade'] = students['grade'].astype(int)
    return students
